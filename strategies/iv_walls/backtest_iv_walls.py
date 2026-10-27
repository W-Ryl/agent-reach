"""IV-walls backtest on S&P 500 daily OHLC + VIX.

Walls for day t are built only from information known before day t opens:
    sigma_day = VIX(t-1) / 100 / sqrt(252)
    upper     = Close(t-1) * (1 + z * sigma_day)
    lower     = Close(t-1) * (1 - z * sigma_day)

Part 1 measures how often the walls "hold" (high stays under upper, low stays
above lower). Part 2 fades a wall touch: short at the upper wall / long at the
lower wall, stop k * sigma beyond the wall, exit at the close. With daily bars
this is exact for a single trade, because a short is stopped iff the high
reaches upper + stop (the entry is always touched first). Days where both
walls are touched are counted as both trades.

Usage: python backtest_iv_walls.py sp500.csv vix.csv
"""
import sys
import numpy as np
import pandas as pd


def load(sp_path, vix_path):
    sp = pd.read_csv(sp_path)
    sp["Date"] = pd.to_datetime(sp["Date"]).dt.normalize()
    sp = sp[["Date", "Open", "High", "Low", "Close"]]
    vix = pd.read_csv(vix_path)
    vix["Date"] = pd.to_datetime(vix["DATE"])
    vix = vix[["Date", "CLOSE"]].rename(columns={"CLOSE": "VIX"})
    df = sp.merge(vix, on="Date").sort_values("Date").reset_index(drop=True)
    df = df[df["Date"] >= "1990-01-01"]
    # drop bad bars where the index printed no range
    df = df[(df.High > df.Low) & (df.Open != df.Close)].reset_index(drop=True)
    df["PrevClose"] = df.Close.shift(1)
    df["PrevVIX"] = df.VIX.shift(1)
    return df.dropna().reset_index(drop=True)


def walls(df, z):
    sig = df.PrevVIX / 100 / np.sqrt(252)
    return df.PrevClose * (1 + z * sig), df.PrevClose * (1 - z * sig), df.PrevClose * sig


def hold_stats(df, z):
    up, lo, _ = walls(df, z)
    up_hold = df.High <= up
    lo_hold = df.Low >= lo
    return {
        "z": z,
        "upper_holds_%": 100 * up_hold.mean(),
        "lower_holds_%": 100 * lo_hold.mean(),
        "both_hold_%": 100 * (up_hold & lo_hold).mean(),
        "close_inside_%": 100 * ((df.Close <= up) & (df.Close >= lo)).mean(),
    }


def fade(df, z, k, cost_pts=0.5):
    """P&L in index points per trade; cost_pts = round-trip slippage + fees (ES ~0.5pt)."""
    up, lo, sig_pts = walls(df, z)
    stop = k * sig_pts
    trades = []
    s = df.High >= up
    pnl_s = np.where(df.High >= up + stop, -stop, up - df.Close)
    trades.append(pd.DataFrame({"Date": df.Date[s], "side": "short", "pnl": pnl_s[s] - cost_pts, "risk": stop[s]}))
    l = df.Low <= lo
    pnl_l = np.where(df.Low <= lo - stop, -stop, df.Close - lo)
    trades.append(pd.DataFrame({"Date": df.Date[l], "side": "long", "pnl": pnl_l[l] - cost_pts, "risk": stop[l]}))
    t = pd.concat(trades).sort_values("Date")
    t["R"] = t.pnl / t.risk
    return t


def summarize(t, label):
    if t.empty:
        return {"set": label, "trades": 0}
    wins = t.R > 0
    gp, gl = t.R[wins].sum(), -t.R[~wins].sum()
    eq = t.R.cumsum()
    return {
        "set": label,
        "trades": len(t),
        "win_%": round(100 * wins.mean(), 1),
        "avg_R": round(t.R.mean(), 3),
        "PF": round(gp / gl, 2) if gl else np.inf,
        "total_R": round(t.R.sum(), 1),
        "maxDD_R": round((eq.cummax() - eq).max(), 1),
    }


def main(sp_path, vix_path):
    df = load(sp_path, vix_path)
    print(f"Data: {df.Date.min().date()} to {df.Date.max().date()}, {len(df)} days\n")

    print("PART 1 - how often do the walls hold? (z = width in daily implied sigmas)")
    print(pd.DataFrame([hold_stats(df, z) for z in [0.5, 1.0, 1.28, 1.645, 2.0]]).round(1).to_string(index=False))

    print("\nRolling 30-day 'respected' count for z=1.0 (the reel's '27 of 30' claim):")
    up, lo, _ = walls(df, 1.0)
    both = ((df.High <= up) & (df.Low >= lo)).astype(int)
    roll = both.rolling(30).sum().dropna()
    print(f"  median {roll.median():.0f}/30, 10th pct {roll.quantile(.1):.0f}/30, 90th pct {roll.quantile(.9):.0f}/30, "
          f"share of windows >= 27/30: {100*(roll>=27).mean():.1f}%")

    print("\nPART 2 - fade the wall, stop k*sigma beyond it, exit at close, 0.5pt costs")
    print("In-sample 1990-2009 vs out-of-sample 2010-2018, plus a neighbourhood grid:")
    rows = []
    for z in [0.75, 1.0, 1.25, 1.5]:
        for k in [0.25, 0.5, 1.0]:
            t = fade(df, z, k)
            ins, oos = t[t.Date < "2010-01-01"], t[t.Date >= "2010-01-01"]
            a, b = summarize(ins, "IS"), summarize(oos, "OOS")
            rows.append({"z": z, "k": k,
                         "IS_trades": a["trades"], "IS_win%": a.get("win_%"), "IS_avgR": a.get("avg_R"), "IS_PF": a.get("PF"),
                         "OOS_trades": b["trades"], "OOS_win%": b.get("win_%"), "OOS_avgR": b.get("avg_R"), "OOS_PF": b.get("PF"),
                         "OOS_maxDD_R": b.get("maxDD_R")})
    print(pd.DataFrame(rows).to_string(index=False))

    print("\nSide split for z=1.0, k=0.5 (OOS 2010-2018):")
    t = fade(df, 1.0, 0.5)
    t = t[t.Date >= "2010-01-01"]
    for side in ["short", "long"]:
        print(" ", summarize(t[t.side == side], side))

    print("\nNull test - same rules on shuffled daily returns (no structure), z=1.0, k=0.5:")
    rng = np.random.default_rng(0)
    res = []
    for _ in range(200):
        idx = rng.permutation(len(df))
        sh = df.copy()
        # rebuild a synthetic path keeping each day's own bar shape relative to its prev close
        rel = df[["Open", "High", "Low", "Close"]].div(df.PrevClose, axis=0).values[idx]
        vix = df.PrevVIX.values[idx]
        closes = [df.PrevClose.iloc[0]]
        O, H, L, C = [], [], [], []
        for r in rel:
            pc = closes[-1]
            O.append(r[0]*pc); H.append(r[1]*pc); L.append(r[2]*pc); C.append(r[3]*pc); closes.append(r[3]*pc)
        sh["Open"], sh["High"], sh["Low"], sh["Close"] = O, H, L, C
        sh["PrevClose"], sh["PrevVIX"] = closes[:-1], vix
        res.append(fade(sh, 1.0, 0.5).R.mean())
    real = fade(df, 1.0, 0.5).R.mean()
    print(f"  real avg R {real:.3f}; shuffled avg R mean {np.mean(res):.3f}, 95th pct {np.quantile(res,.95):.3f}")
    print("  (shuffling keeps each day's VIX with its own bar, so it only tests whether day ORDER matters;"
          " the wall/VIX relationship itself survives the shuffle)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
