"""Try the 'hedge fund research' repos on our IV-walls problem.

1. arch: GARCH(1,1) forecast of tomorrow's volatility vs VIX for building walls.
2. arch.bootstrap.SPA: did the best of our fade variants beat zero, or just get lucky?
3. MAPIE: conformal prediction bands for the day's high/low with a target 90% coverage.

Usage: python quant_tools_demo.py sp500.csv vix.csv
"""
import sys
import warnings
import numpy as np
import pandas as pd
from arch import arch_model
from arch.bootstrap import SPA
from sklearn.ensemble import GradientBoostingRegressor

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from backtest_iv_walls import load, fade

warnings.filterwarnings("ignore")


def garch_sigma(df, refit_every=250, window=2500):
    """One-step-ahead daily sigma (fraction), refit yearly on a rolling window; no look-ahead."""
    r = 100 * np.log(df.Close / df.PrevClose)
    out = pd.Series(np.nan, index=df.index)
    for start in range(window, len(df), refit_every):
        fit = arch_model(r.iloc[start - window:start], vol="GARCH", p=1, q=1, dist="t").fit(disp="off")
        p = fit.params
        end = min(start + refit_every, len(df))
        var = fit.conditional_volatility.iloc[-1] ** 2
        for i in range(start, end):
            eps = r.iloc[i - 1] - p["mu"]
            var = p["omega"] + p["alpha[1]"] * eps ** 2 + p["beta[1]"] * var
            out.iloc[i] = np.sqrt(var) / 100
    return out


def coverage(df, sig, z):
    up, lo = df.PrevClose * (1 + z * sig), df.PrevClose * (1 - z * sig)
    ok = sig.notna()
    return (100 * (df.High <= up)[ok].mean(), 100 * (df.Low >= lo)[ok].mean(), 100 * (z * sig)[ok].mean())


def main(sp, vx):
    df = load(sp, vx)
    vix_sig = df.PrevVIX / 100 / np.sqrt(252)
    g = garch_sigma(df)
    print("1) Walls from VIX vs GARCH vs 50/50 blend (same days, z=1.28)")
    print("   source      upper holds  lower holds  avg half-width %")
    for name, s in [("VIX", vix_sig.where(g.notna())), ("GARCH", g), ("blend", 0.5 * vix_sig + 0.5 * g)]:
        u, l, w = coverage(df, s, 1.28)
        print(f"   {name:<10}  {u:10.1f}  {l:11.1f}  {w:14.2f}")

    print("\n2) SPA test (Hansen 2005) on the 12 fade variants' daily P&L vs doing nothing")
    days = pd.DataFrame(index=df.Date)
    for z in [0.75, 1.0, 1.25, 1.5]:
        for k in [0.25, 0.5, 1.0]:
            t = fade(df, z, k, cost_pts=0)
            days[f"z{z}_k{k}"] = t.groupby("Date").R.sum().reindex(df.Date).fillna(0).values
    bench = np.zeros(len(days))
    losses = -days.values  # SPA works on losses: lower is better
    spa = SPA(-bench, losses, reps=1000, seed=0)  # benchmark loss = 0
    spa.compute()
    print(f"   best variant avg R/day {days.mean().max():.4f}; SPA p-values (lower/consistent/upper): "
          f"{spa.pvalues.round(3).to_dict()}")
    print("   -> high p-value = no evidence any variant beats doing nothing")

    print("\n3) MAPIE conformal band for tomorrow's high (as % above prior close), target 90%")
    try:
        from mapie.regression import TimeSeriesRegressor
    except ImportError:
        TimeSeriesRegressor = None
    X = pd.DataFrame({
        "vix": df.PrevVIX,
        "rng1": ((df.High - df.Low) / df.PrevClose).shift(1),
        "rng5": ((df.High - df.Low) / df.PrevClose).shift(1).rolling(5).mean(),
        "ret1": np.log(df.Close / df.PrevClose).shift(1),
    })
    y = (df.High / df.PrevClose - 1) * 100
    ok = X.notna().all(axis=1)
    X, y, dates = X[ok].values, y[ok].values, df.Date[ok].values
    n_fit = int(len(X) * 0.5)
    n_cal = int(len(X) * 0.7)
    model = GradientBoostingRegressor(max_depth=3, n_estimators=200).fit(X[:n_fit], y[:n_fit])
    # split-conformal upper bound: q90 of calibration residuals (one-sided)
    resid = y[n_fit:n_cal] - model.predict(X[n_fit:n_cal])
    q = np.quantile(resid, 0.9)
    upper = model.predict(X[n_cal:]) + q
    cov = 100 * (y[n_cal:] <= upper).mean()
    vix_upper = 1.28 * df.PrevVIX[ok].values[n_cal:] / np.sqrt(252)
    print(f"   test {pd.Timestamp(dates[n_cal]).date()}..{pd.Timestamp(dates[-1]).date()}: conformal upper wall holds "
          f"{cov:.1f}% with avg distance {upper.mean():.2f}%  |  VIX z=1.28 wall holds "
          f"{100*(y[n_cal:]<=vix_upper).mean():.1f}% at {vix_upper.mean():.2f}%")
    print(f"   (MAPIE wraps exactly this split/adaptive-conformal recipe; installed: {TimeSeriesRegressor is not None})")


if __name__ == "__main__":
    main(*sys.argv[1:3])
