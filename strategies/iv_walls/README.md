# IV Walls: What They Are, What the Reels Claim, and a First Backtest

*Built October 27, 2026. Not financial advice.*

## 1. The reels
Three reels push the same idea:
- **De-ZtZLv1N2** and **DdjjN2CzmPX** from @keonehub.
- **Dd3Ec8AB2Pj** from @atraintrades (same pitch, possibly the same group).

**The claim** (De-ZtZLv1N2, transcript): "This quant strategy has a 90% chance of predicting high of day and low of day. In the quant software we look at **historical volatility** plus **contract pricing** [option prices / implied volatility] and combine these to find our **daily range, the IV walls**. In the last 30 days these IV walls were respected 27 times, so a 90% chance. Wait for price to test these levels, place your entry with stops above or below, and ride the reversal." He also shows two payout certificates ($1,000 and $926). There's a "free guide" if you comment "IV walls."

**On screen:**
- **Charts:** a price chart with green/red boxes above and below price (the walls). The hand-drawn notes say "30 days, 27 times = 90%."
- **The software:** a desktop options tool with a "spaghetti" of curves across strikes. Panel labels: "Traded Volume / dealer inventory risk", "PUT CONTRACTS" with IV and ask columns, "Expected Move", "Downside Risk", "LongAvg 723.20 / ShortAvg 708.97", "CRUSH 97.2%", and checkboxes "Color Spaghetti / Adjust Waves". The crosshair price is about 703.8 and the last update was Oct 26, 2026, so the underlying is likely SPY or similar.
- **The tool is unidentified.** It looks private or paid, and it isn't CME QuikStrike, which we checked.

## 2. What an "IV wall" is, in plain maths
Option prices imply how much the market expects price to move. An annual implied volatility (IV) converts to a one-day move like this:

```
daily sigma (%) = IV / sqrt(252)            ~ IV / 16  ("rule of 16")
upper wall      = reference price * (1 + z * daily sigma)
lower wall      = reference price * (1 - z * daily sigma)
```

- **Reference price:** the prior close or settlement, or today's open.
- **z** sets the width. z = 1 is "1 standard deviation."
- **Equivalent:** the **at-the-money straddle price** for the nearest expiry is roughly the market's expected move, which is how most "expected move" tools draw these bands. Examples: [OptionCharts expected-move chart](https://optioncharts.io/blog/introducing-expected-move-chart), [DeepCharts Option Expected Move](https://www.deepcharts.com/helpcenter/article/option-expected-move), [ATAS Options X-Ray](https://help.atas.net/en/support/solutions/articles/72000662222-options-x-ray-expected-move), the TradingView [4C Options Expected Move (0DTE)](https://www.tradingview.com/script/9nOpiEYe-4C-Options-Expected-Move-Weekly-0DTE/) and [Implied Volatility Walls by OmegaTools](https://www.tradingview.com/script/kpwku8Io/) indicators, and CME's free [QuikStrike Vol2Vol Expected Range](https://www.cmegroup.com/tools-information/quikstrike/vol2vol-expected-range.html) for futures options.
- **"Historical volatility plus contract pricing"** most likely means blending realised volatility (e.g. a 20-day ATR or standard deviation) with implied volatility, so the band isn't too wide when IV carries a big risk premium.
- **Other "walls":** "dealer inventory," "call/put walls" and "gamma" refer to strikes with large open interest that sometimes act as magnets or barriers. That's a separate data layer, from SpotGamma, MenthorQ, or the GEX tool in the Astra reel.

## 3. First test: S&P 500 daily, 1990–2018 (`backtest_iv_walls.py`)
**Data:**
- S&P 500 daily OHLC (Yahoo export via github.com/vijinho/sp500; it ends Dec 2018).
- VIX daily close (github.com/datasets/finance-vix).
- Finance APIs are blocked in this sandbox, so this is the free data that was reachable.

**Walls:** prior close ± z × (prior-day VIX ÷ √252). No look-ahead.

### Part 1: is "the walls hold 90% of the time" true? Mostly yes, depending on width.
| z (width) | upper wall holds | lower wall holds | both hold | close inside |
|---|---|---|---|---|
| 1.0 | 86.0% | 83.7% | 69.9% | 81.6% |
| **1.28** | **93.5%** | **90.9%** | 84.4% | 90.1% |
| 1.645 | 98.0% | 95.8% | 93.7% | 96.0% |

- A "90%" hold rate is just a choice of width (about 1.3 implied sigmas). VIX usually *overstates* realised moves (the variance risk premium), so the bands look reliable.
- **"27 of 30 days" at a 1σ width happened in only 5% of rolling 30-day windows.** The median was 21/30. So that screenshot is a good month, not a typical one.

### Part 2: but does *fading* the wall make money? Not the naive version.
**Rules:**
- Short the first touch of the upper wall, or buy the first touch of the lower wall.
- Stop k × sigma beyond the wall.
- Exit at the close.

This is exact with daily bars, because a short is stopped if and only if the high reaches the stop.

| setup | trades | win % | avg R | profit factor |
|---|---|---|---|---|
| z 1.0, stop 0.5σ, costs 0.5 pt, out-of-sample 2010–18 | 699 | 34% | −0.18 | 0.60 |
| z 1.0, stop 1.0σ, no costs, 1990–2018 | 2,207 | 39% | −0.09 | 0.63 |
| z 1.28, stop 2.0σ, no costs | 1,136 | 36% | −0.06 | 0.55 |

Every one of the 12 grid cells loses, in-sample and out-of-sample, on both sides, before and after costs.

**Why:**
- Once price *reaches* a 1.28σ wall, it closes back inside only **28%** of the time. A day that travels that far is usually a trend day.
- So the 90% "wall holds" statistic is mostly the many quiet days that never got near the wall, and you don't trade those.
- **Selection trick:** "the walls held 90%" is about *all* days. The trade only happens on the *touch* days, where the odds flip.

### A trap we caught (the same mistake as the reels)
- **What we tried:** adding a profit target with daily bars produced fantastic results: a 90–99% win rate and +0.4 to +1.0 R per trade.
- **Why it's fake:** the day's low (the "target") usually happened *before* price rallied to the wall. Daily bars can't tell you whether the target came *after* the entry.
- **What that means:** this is look-ahead bias, and it's exactly how a backtest or screenshot can show "100% win rate." **Testing targets needs intraday data.**

## 4. What it would take to test the reel's version properly
The reel's real rules are a touch, then a reversal entry, a tight stop beyond the wall, and riding back toward the middle. That needs:

1. **Intraday bars**, 1- to 5-minute, for ES/MES or NQ/MNQ. Sources:
   - Free: a NinjaTrader, Tradovate or Rithmic demo, or a TradingView export.
   - Cheap, paid: Databento (CME data billed per use), FirstRate Data, Kibot.
2. **A better daily IV:** **VIX1D** (Cboe's 1-day VIX, since 2023) or **VXN** for NQ, or the 0DTE/weekly ATM straddle on ES/SPX options. Also test a **blend with realised volatility** (e.g. 0.5 × IV + 0.5 × ATR-based), which is likely their "historical vol plus contract pricing."
3. **Entry variants to compare:**
   - (a) a limit order at the wall
   - (b) wait for a 5-minute close back inside the wall
   - (c) (b) plus an order-flow or volume confirmation (e.g. the "climax volume" rule)
4. **Exits:** a stop beyond the wall's touch extreme; targets at 1R, 1.5R, the midpoint or the prior close; a time stop at the session end. Flat by close (prop-friendly).
5. **Regime filters:** skip FOMC/CPI/NFP days, trend days (e.g. the opening range breaks hard), or when VIX is rising.
6. **Validation, per our harness:**
   - in-sample/out-of-sample split and walk-forward
   - a parameter neighbourhood (z ± 0.25, stop ± 0.25σ)
   - realistic costs (1 tick each side plus commission)
   - a scrambled-market null
   - a Monte Carlo of the trade list against the target prop firm's rules (daily loss, trailing drawdown)

**Prompt for Claude Code:**
```
In strategies/iv_walls/, extend backtest_iv_walls.py into an intraday backtester for MES/ES using 1-minute bars from <DATA SOURCE>.
Walls each day = prior settlement ± z * daily_sigma, where daily_sigma = blend(VIX1D or VIX/sqrt(252), 20-day ATR%) with blend weight w.
Implement entry variants (limit at wall / 5-min close back inside / + volume-climax confirmation), stop beyond the touch extreme, targets {1R, 1.5R, mid, prior close}, time stop at 15:55 ET, skip FOMC/CPI/NFP days.
Report per variant: trades, win%, avg R, PF, max DD (R), in-sample 2019-2022 vs out-of-sample 2023-2026, parameter heatmaps over z in [0.75..1.75] and w in [0..1], costs = 1 tick/side + $1.30/side, and a 200-run scrambled-day null.
Then run a Monte Carlo of the best variant's trade list against a 50K prop eval (target $3,000, trailing drawdown $2,000, daily loss $1,000) and report pass probability.
Never use a bar's high/low to decide an exit that could have happened before the entry.
```

## 5. Bottom line
- **True:** IV-based ranges contain the day's high and low most days, so the "90%" is real, and it's a sensible way to set *context*: where moves are stretched, where to take profit, where not to chase.
- **Not true:** that "the walls hold 90%" means "fading the walls wins 90%." On 29 years of S&P data the naive fade loses at every width and stop we tried, because the days that reach the wall are the days that keep going.
- **Still open:** the reel's discretionary reversal entry might still work with intraday confirmation. That's the test in section 4. Until it passes, treat "IV walls 90% win rate" as a marketing statistic.

## Files
- `backtest_iv_walls.py`: the daily test. Run it with `python backtest_iv_walls.py sp500.csv vix.csv`, using the two CSVs listed in section 3.
