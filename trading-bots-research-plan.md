# Claude Trading Bots: What the 36 Reels Say + Deep-Research Plan & Prompt

*Built October 22, 2026, from 36 Instagram posts (38 links, 2 duplicates). For the 30 videos, the speech was transcribed and on-screen content was read frame by frame. For the 6 photo carousels, captions and the first slide were read. Nothing below is financial advice.*

---

## 0. Quick answers

- **The "19-year-old kid"** is from **Japan, not China**. The on-screen card in @msbintel's reel (DerbR1flH4p) reads *"19-YEAR-OLD STUDENT · JAPAN"*. You may have mixed it up with @bestapps.ai's **"This Chinese guy just open-sourced a model that predicts the future"** (Dd-FFigDPFC). That post is about **Kronos**, a forecasting model from Tsinghua University. Both are covered in section 3.
- **"Bloomberg terminal":** none of the reels names Bloomberg. The closest are two free open-source alternatives:
  - **Fincept Terminal** (DYsTJT0R12f, DeCAlxLjSFl), pitched as a "completely free AI financial intelligence platform."
  - **OpenAlice** (DZDH5NJRMPf), "your one-person Wall Street."

  The real Bloomberg Terminal is a reference point in the research prompt.
- **"The predictive thing"** is one of two tools:
  - **Kronos**: give it 400 candles and it forecasts the next 120.
  - **Pythia** (DeW3OJfgXP9): forecasts world events and prediction-market outcomes, with probabilities and reasoning.

  Prediction markets themselves (**Polymarket, Kalshi**) come up in 7 reels.
- **Prop firms:** 4 reels are directly about prop firms:
  - Moon Dev building a bot for a **$10k USDC crypto prop account** (Propr, which runs on Hyperliquid).
  - @algo.jitnems claiming a "94.18% chance of passing a 50k eval."
  - @itsmikepoarch running bots on **PROP_25K / PROP_50K futures accounts**.
  - The "IV walls" reels: "prop firms will instantly start sending you payouts."
- **Honest pattern across all 36:** about half are **"comment X and I'll DM you the setup"** lead funnels with unverified screenshots ($68 → $750k, $89 → $55k, $1k → $100k). The most credible reels are the *skeptical* ones: @fidetolabs, the "Thursday ES" overfitting reel, @bennnytrades' 4 robustness steps, and @fanonomics on AI herding. They all say the same thing: **most backtests that look amazing are luck or leakage.**

---

## 1. Every post, what it says, and what's on screen

### A. Claude- and LLM-driven trading agents

| # | Post | Creator | What they say (speech + caption) | On screen / tools | Credibility |
|---|---|---|---|---|---|
| 1 | DerbR1flH4p | @msbintel | A 19-year-old student in **Japan** built a trading bot with **Claude Code in 2 days**. $68 → about $7,000 in a day, and about **$750,000** after a couple of months. It watches **50+ markets at once**, pulls **live BTC prices from Binance every second**, and hunts tiny short-lived **price gaps**. "That's the real edge. Not a smarter guess, just faster comparisons." The gaps disappear fast and you can lose everything. | Card: "19-YEAR-OLD STUDENT · JAPAN · Claude Code · BUILT A TRADING BOT IN 2 DAYS". Flow: **Claude** (wrote the strategy and logic) → **Binance** (feeds the live data, "Aggregate Trade Streams" API docs shown) → **24/7 trade ready** when a price gap matches its rules. "HE CLAIMS" overlay. "Results like his are rare. You can lose everything." | Low. See section 3. |
| 2 | Dd951zjohCk | @bob.curtis.creator | "Claude becomes a trader." Connect Claude to **Liquid** (stocks, crypto, forex, commodities, *prediction markets*) and **Quiver Quant** (insider trades, **politician/Congress trades**, institutional activity). Give it a strategy such as "watch investor X's disclosed trades," compare against your portfolio, get recommendations, run it as a **Routine**, and **paper trade first**. | Claude.ai with a **custom MCP connector** dialog (`http://127.0.0.1:...`), Quiver Quant "Congress Trading" dataset, Liquid logo, a Claude **Skills** folder (SKILL.md), and a portfolio table (GOOGL, NVDA, PLTR, AVGO, MSTR, TSLA). | Medium. A real, legit architecture: alerts and recommendations, with a human deciding. |
| 3 | DesfvSBMToO | @fanonomics | **Robinhood now gives AI agents (like Claude) their own trading account**: a separate "MCP account" you fund, and the agent places orders itself. In **Alpha Arena Season 1** (Oct 18 – Nov 3, 2025), 6 AIs got $10k each; 4 lost more than 40%. An MIT-style study found that smarter models trade more alike, so **herding**: one fake headline makes all the bots sell together. The **Bank of England** (Sarah Breeden, "Agents of change," 30 June 2026) is asking about an AI **kill switch**. ChatGPT headline-trading returns **shrank as more people used it**. | Robinhood Help Center "Open an MCP account." Alpha Arena bars: Qwen, DeepSeek, Claude, Gemini, Grok, GPT-5. Paper: *"Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets"* (Ross, So, De Simone, Pozniak & Lo). Two "build me a trading bot" chats produce almost the same RSI code. | **High.** An important counter-argument. |
| 4 | Dex3FYyjCWj | @moondevonyt (Moon Dev) | "Do you make bots for prop firms? Now I am." He bought a **$10,000 USDC prop account** and runs a **simulator off his own Hyperliquid account**, using **Claude Code** to build the bot. "I'll probably fail." | Prop-firm checkout ("Propr | Trading" browser tab): **Explorer 1-Step Turbo, $50 one-time, 10,000 USDC, profit target 9%, max drawdown 3% (static), daily loss limit 3%, profit split 80%, no time limit.** A Pro tier at $85 has a 12% target and 5% max DD. Claude Code terminal "moon-dev-trading-bots", a Hyperliquid positioning scan (BTC/ETH/SOL), "order mapping is right on all four types." | Medium. A real attempt, live-streamed, outcome unknown. |
| 5 | DdxRdW6DdTL | @moondevonyt | "The most interesting thing from **JEV AI applied to Polymarket**… it costs nothing, **$0.00025**, and it's fast." | Terminal "Polymarket-Trading-Bots": **"JEV SAYS – NOTHING, under the 58% line – p(up) 47%, chopping tape"**, 485 ms, $0.000250 per call, model "typesafe/jev-1.13". Polymarket **"BTC Up or Down" 5-minute markets**. It holds flat (no trade) with a countdown. | Medium. It shows a *discipline* gate (no trade below a 58% edge). |
| 6 | DeOj9lDORjf | @yuhgosla | "**Kalshi** Trading Bot, **Krypt Trader**": free and open source. Agents connected through **MCP tooling** forecast every Kalshi market, then send forecasts to **"the council"**, which votes. Each agent has a different personality and risk profile (e.g. "Fed Whisperer," "Sharp Money"). A walkable 3D office. | Agent Hub, Research Lab, Trading Desk, Optimizer, Backtest Chamber, Win/Loss Vault. Agents labeled by model (e.g. "Fed Whisperer · Sonnet", gpt, opus). Session P&L about +$891. | Low–medium. A fun UI; the edge is unproven. |
| 7 | DZDH5NJRMPf | @startscalr_sohum | "Someone finally open-sourced a **one-person Wall Street machine**. All you need is **Claude Code**. It's called **OpenAlice**": research, analysis, automation and a "heartbeat" feature. | GitHub **TraderAlice/OpenAlice** (AGPL-3.0): equities, crypto, commodities, forex, macro. Unified Trading Account (multiple brokers), **Trading-as-Git** (stage, commit, push orders), a **guard pipeline** (pre-execution safety checks), cron/heartbeat/webhook automation, and an MCP server. Requires Node.js 22+, pnpm, and the Claude Code CLI. | **High.** A real repo. Brokers include CCXT, Alpaca and IBKR. Trades need your approval. |
| 8 | DYsTJT0R12f | @startscalr_sohum | "Someone open-sourced their entire financial intelligence platform… connect with **Claude Code**… **37 AI agents** (Buffett, Graham, Lynch…) debate… **100+ data connectors**, real-time trading, global intelligence, your own **AI quant lab**." | **Fincept Terminal** README: DCF models, portfolio optimization, VaR/Sharpe. Data from **DBnomics, Polygon, Kraken, Yahoo Finance, FRED, IMF, World Bank**. Real-time trading via Kraken/HyperLiquid WebSocket and brokers (Zerodha, Angel One, Upstox, Fyers, Dhan, AliceBlue, Shoonya, Alpaca, IBKR…). QuantLib suite (18 modules), node editor, ML models, HFT. LLMs: OpenAI, Anthropic, Gemini, Groq, DeepSeek, MiniMax, OpenRouter, Ollama. | **High.** A real repo, and the "free Bloomberg" option. |
| 9 | DeCAlxLjSFl (carousel) | @techskills | "People are quietly printing cash with free GitHub repos": **Claude Ads, Fincept Terminal, Vibe-Trading (HKUDS)**, Camofox Browser, Hyperframes, Open Generative AI. | Only the first slide is visible. | Repo list. |
| 10 | Dak-8k6oNeA | @astongilltrading | "**3PO**," a **self-learning AI quant**. It finds and reads research papers and books (393 items in 24 h, shown as a "brain vault" star map), then a **strategy factory** builds strategies. Each must pass **out-of-sample screening → Monte Carlo → walk-forward → deflated Sharpe → demo account** before going into a **portfolio** with **risk gates**. It also talks back with a voice. | Localhost dashboard "Knowledge Base": 393 research items, 244 graveyard, 839 vault notes, 784 backtests. Portfolio HQ (-$2,188 shown), "RISKGATE" radar. | Medium. The pipeline is textbook-correct; the results aren't shown. |
| 11 | Dct-7ZKyI2J | @deethiopian | Her **futures AI agent**'s August: it took a month to make what it usually makes in a week, and only traded 10 of 21 days. What saved her: (1) **strategy filters** blocking bad days, (2) a **news agent** that marks days "good" or "cautious," with **half size (contracts) on cautious days** (normal is 25 contracts), (3) **historical data** shows August is always choppy. | Selfie video, text cues only. | Medium. Honest about a bad month. |
| 12 | Dc4o1ecxT_O | @itsmikepoarch | His bot runs **200+ strategies live**. A "fleet" tab lets you sort by P&L or win rate and assign strategies to accounts. "Back-tested billions of strategies." A paid product with a 2-week trial. | **"Phantom Trader A.I."** on futures: 6C, 6J, 6E, NG, CL, ZB, ZN, ES, YM, RTY, MNQ, MGC, SIL, on 1–15 min bars. **Account names PROP_25K_… and PROP_50K_…** (futures prop-firm accounts). "Core day P&L" about $500–826. | Medium-low. A sales funnel, but it shows prop-firm automation in practice. |
| 13 | DcYD0IRSdTd | @fidetolabs | "Day 3: Building a self-improving AI trading agent." A backtesting dashboard "for evaluating a strategy, **not for data-mining, which is useless**." | Dashboard with an equity curve, heatmap, distribution. | High (a mindset reel). |
| 14 | Dd8zpBVEinT | @fidetolabs | **Look-ahead bias from news timestamps.** 5,908 articles on 8 companies; **37% were published after the market close**. File them by printed date and the strategy shows a **Sharpe of 3.18**. File them by the first day you could actually trade on them and it's **0.98**. A self-improving agent running 1,000 variations "converges on whichever one leaks hardest." | Text animation. | **High.** A crucial pitfall for LLM and news bots. |
| 15 | DeMZ0ujNQ8l | @fidetolabs | Agent memory: the agent forgets everything between runs, so keep **one dated notes file** that the agent reads first. Only a human can change lines. Example lesson: "counting words in filings is a late signal; use required disclosure fields, which come years earlier." | Text animation. | High (a method). |

### B. The "6 Grok bots" / JEV multi-agent hype cluster

| # | Post | Creator | Claim | On screen |
|---|---|---|---|---|
| 16 | DeRXZptsGOC | @ashtonv.ai | "**Grok might have killed day trading**": **6 Grok bots in one group chat**. $87 → $8,000 and $90 → $14,000. Roles: **Scout** (big moves), **News**, **Chart** (entry, exit, stop), **Skeptic** (argues against every trade: buy, wait or skip). Runs on its "own cloud computer 24/7." | X posts (@0xMarioNawfal "350 Grok bots… one-person AI trading desk"). Grok "New group, max 6 bots per group." Order ticket "**BLOCKED BY SKEPTIC**", risk to reward 1.4:1. |
| 17 | Dd-Ue0-vBZl | @seb.ai | 6 Grok bots: **$1,000 → $101,607 in 10 days**. Every night **JEV** picks which tokens to focus on, and 6 bots trade the same coin overnight. "Almost $15k on the final night." | "GROKBOT × JEV" dashboard, X post with a daily balance list. |
| 18 | DeOFgvvPw8v | @seb.ai | **$89 → $55,698 while he slept.** One bot finds trades, one sizes them, one buys, one **bets on prediction markets**, and one stops the others from chasing pumps. The caption admits **he added $1,000 along the way** and 4 losing trades (-$717). | "FOMO · GROK" dashboard. |
| 19 | DeOPnJDltkN (carousel) | @seb.ai | "I rebuilt the team": Scout, News, Sentiment, Charts, Risk, Decision (BUY, WAIT or SKIP). "$89 → $68,024." | Pixel-art office slide. |
| 20 | DeS3-nUmnPK (carousel) | @seb.ai | **$100 → $52,437 in 8 nights.** A crawler plus JEV plus 4 Grok bots (momentum, breakouts, whales, risk). **"No public wallet, source code, or independent verification was provided."** | Pixel-art slide. |
| 21 | DeIgSE4PPuZ | @seb.ai | A "trading terminal" with its own **24/7 web crawler**: **$63 → $740 → $2,810 → $8,980** in 3 nights. Agents: Scout, **Skeptic** (caught 2 projects recycling old announcements), Quant (entry), Risk (how much could go wrong), then **ChatGPT reviewed the evidence**. **He manually approved entries.** 76 new token launches found on night 3. | Red "trading terminal" dashboard, X thread. |
| 22 | DeQaNsBFCHr (carousel) | @seb.ai | "**Claude** reportedly turned **$80 into $4,218**." Four rules: trade only the strongest time windows; **size by confidence**; strict risk limits set before entry; **log every trade**. | Slide: position size $250 (1.2% of equity), **risk limit 2.0% ($84 max loss)**, BTC/ETH/SOL/AVAX scan, EMA-cross + RSI strategy code, trade log. |

*Pattern:* a handful of creators recycle the same few X screenshots into dozens of posts. The useful idea is the **role structure** (Scout → News/Sentiment → Chart → **Skeptic/Risk veto** → Decision). The dollar figures are not useful; they appear to be micro-cap/meme-coin luck, with deposits added mid-run.

### C. Turn research papers into bots

| # | Post | Creator | Method | Tools on screen |
|---|---|---|---|---|
| 23 | DdDAfdphoYX | @lucas_lalk | Go to **papers.ssrn.com** (search "intraday trading": 10,000 results). Copy a paper, paste it into **Astral** ("build me this exact strategy"), and it codes and backtests it. "Most of the time results won't be good, but sometimes…" | SSRN results, e.g. "Intraday Index Predictability and Options Trading Profitability," "Forecasting Intraday Trading Volume: A Kalman Filter Approach." The Astral AI chart workspace shows stop-loss and take-profit, total return, Sharpe, max drawdown. |
| 24 | DdZYy4nMDkB | @quant_labde | Go to **Quantpedia** ("Encyclopedia of Algorithmic and Quantitative Trading Strategies"), copy a strategy link, have **DeepSeek** write **MQL5** code, compile it in **MetaEditor**, then run it in **MT5**'s Strategy Tester. | Quantpedia strategy list (Asset Class Trend Following, Momentum, Sector Momentum, FX Carry, Low Volatility). MT5 on **Vantage International**, NAS100/SP500/DJ30 "OpenRangeBreakout" EA. MQL5 marketplace bots selling for $199–$1,999. |
| 25 | DeTi6DdBxCD | @nishantaqc | 4 quant résumé projects: (1) **options pricing and Greeks** (Black-Scholes, binomial, Monte Carlo, vol surface); (2) **pairs trading** (cointegration, *include costs, out-of-sample*); (3) a **limit order book / market-maker simulator** (Jane Street, Citadel Securities, Optiver); (4) an **ML alpha signal** with walk-forward and no leakage. | n/a. A good learning curriculum. |

### D. Validation and anti-overfitting (the most valuable reels)

| # | Post | Creator | Lesson |
|---|---|---|---|
| 26 | DeUW_vslUI8 | (unknown) | **"Quant 101."** 850 days of **ES futures**, about 8,500 strategy variants. Best: **"buy ES every Thursday at 10:10am, sell 5 min later"**, with Sharpe 2.4 in-sample and 1.8 out-of-sample. Then: **(1)** move the entry ±10 min or change the day → **negative** (96% of neighbours have no edge; "a real edge is a hill, this is a needle"); **(2)** add 2 ticks of slippage plus commission → 2.4 becomes 1.6, and 1.8 becomes 1.1; **(3)** run the same 8,500 tests on a **scrambled zero-edge market** → best Sharpe 2.3, which is **what luck looks like**; **(4)** of the top 100, 54 lost money out of sample. First version had a Sharpe of 4.8 because of a look-ahead bug (used the day's close at 10am). **Four questions:** works on new data? survives next door? survives costs? beats a fake market? |
| 27 | DeADSs7tPf7 | @bennnytrades | 4 steps before deploying: **(1) parameter stability heatmap** (a broad plateau, not a spike); **(2) Monte Carlo on *every* parameter set**; **(3) cluster analysis** of the results; **(4) in-sample/out-of-sample split plus walk-forward validation.** |
| 28 | Dew84C8Rkkl | @algo.jitnems | "Automated quant strategy RINSES prop firms." "Sniper Range Bot V2" on **MNQ** (micro Nasdaq futures): a 1-year backtest showing **$45k P&L, 73% win rate on a 150k account**. Monte Carlo with 10,000 paths shows **9,418/10,000 = 94.18% chance of passing a $50k eval**, expectancy about $300 per trade. Waitlist ("to prevent alpha decay"). | Funnel. The Monte Carlo-on-eval-rules *method*, however, is exactly right for prop-firm design. |
| 29 | Dd3Ec8AB2Pj / DdjjN2CzmPX | @atraintrades / @keonehub | **"IV walls"**: expected daily range from **implied volatility plus historical volatility** (options pricing). "90% chance price stays inside." Fade the walls with stops beyond them. "100% win rate, $30k on 3 accounts." "Prop firms will instantly send payouts." | Range-box charts. **The concept is real** (expected move = price × IV × √(t/365)), but "90%/100% win rate" ignores the tail losses that blow up prop accounts. |

### E. Data, forecasting and infrastructure tools

| # | Post | Creator | Tool |
|---|---|---|---|
| 30 | Dd-FFigDPFC (carousel) | @bestapps.ai | **Kronos.** "This Chinese guy just open-sourced a model that predicts the future." The first open-source foundation model for **financial candlesticks** (OHLCV → tokens → decoder-only Transformer). Feed it 400 candles and it predicts the next 120. Fine-tunable, MIT license, accepted at AAAI 2026. Even the repo says the signals are "**not a finished trading strategy**." |
| 31 | DeW3OJfgXP9 | @cracked.artificial | **Pythia** (live global intelligence that forecasts stocks, betting markets and world events with probabilities and reasoning), **Hummingbot** (open-source crypto market-making and arbitrage bots, over $14B in user volume; "Condor," an AI harness for Hummingbot), **OpenOutreach** (not trading). |
| 32 | DbW7Q45Mkpo | @keeran.ai | **World Monitor** (github koala73/worldmonitor, worldmonitor.app, about 76k stars): 500+ news feeds, flights, military conflict, shipping choke points, a layoffs tracker. "People use it for stock trades, **Polymarket, Kalshi**." |
| 33 | Deg346vDphY (carousel) | @sebastianhardy_ | "People are printing cash with 6 free GitHub repos." Only the cover slide is visible, so the repos are unknown. |
| 34 | DbEK3bustQ7 | @marc.kaz | **Microsoft SkillOpt** (self-evolving agent skills). Already covered in the JARVIS report. Relevant for making a trading skill improve itself, *with* the leakage caveat from #14. |
| 35 | DeR3K9LAq97 | @charliehills | 17 Hermes skills (Agent Reach and others). Already covered. Not trading-specific. |

---

## 2. Tool inventory (everything named across the 36 posts)

| Category | Tools |
|---|---|
| **AI builders and agents** | Claude Code, Claude.ai (Routines, Skills, custom MCP connectors), Grok (group chat with 6 bots), "JEV" (a fast, cheap decision model; Moon Dev's "typesafe/jev"), ChatGPT, DeepSeek, Astral (AI strategy builder), OpenClaw (execution in the Japan story), Microsoft SkillOpt |
| **Open-source trading platforms** | **OpenAlice** (TraderAlice), **Fincept Terminal**, **Vibe-Trading** (HKUDS), **Hummingbot** (+ Condor), Kalshi "Krypt Trader" agent council, Phantom Trader A.I. (paid) |
| **Forecasting and "predictive"** | **Kronos** (candlestick foundation model), **Pythia** (event and market forecaster), World Monitor (news/OSINT dashboard) |
| **Data** | **Quiver Quant** (Congress, insider, institutional trades), Binance API (aggregate trade streams), Polygon, Yahoo Finance, FRED, IMF, World Bank, DBnomics, SSRN, Quantpedia |
| **Brokers and venues** | **Robinhood** (agent "MCP account"), **Liquid** (multi-asset plus prediction markets), Alpaca, Interactive Brokers, CCXT exchanges, **Binance**, **Hyperliquid**, MT5 (Vantage), NinjaTrader-style futures |
| **Prediction markets** | **Polymarket** (BTC Up/Down 5- and 15-minute markets), **Kalshi** |
| **Prop firms** | **Propr** (crypto prop on Hyperliquid, Explorer 1-Step Turbo $50 for a 10k USDC account), futures prop evals (PROP_25K/50K accounts; specific firms not named) |
| **Validation methods** | Out-of-sample testing, walk-forward, Monte Carlo (on every parameter set), parameter-stability heatmaps, cluster analysis, **deflated Sharpe**, slippage and commission, scrambled-market null test, point-in-time news timestamps, the **Skeptic/Risk veto agent**, half-size on "cautious" news days |
| **Benchmarks and research** | Alpha Arena (Nof1) Season 1; "Why Better Models Can Create Riskier Systems" (Ross, So, De Simone, Pozniak & Lo); Bank of England speech "Agents of change" (Breeden, June 30, 2026) |

---

## 3. The "19-year-old" story, checked

**What the reel says (@msbintel, DerbR1flH4p):**
- A 19-year-old student in **Japan** built the bot with Claude Code in 2 days.
- $68 became about $7,000 in a day, then about $750k "after a couple of months."
- It compares 50+ markets against live Binance BTC prices every second and trades short-lived mispricings.

**What the original X posts add (quick search):**
- The markets are **Polymarket short-duration BTC "Up or Down" markets**, not Binance spot. Binance is only the price feed.
- The architecture is described as **"Claude → strategy and mispricing detection; OpenClaw → execution and Binance sync."**
- The edge is **latency arbitrage**. When BTC moves on Binance, the Polymarket 15-minute "BTC up?" odds lag for a few seconds, and the bot buys the stale side.
- One version claims a "reference wallet" with 54,356 trades and $1.72M profit, a worst drawdown of about 3%, and a $68 start.

**Red flags:**
- The most detailed post (@0x_Discover) is marked **"Paid partnership"** and pushes a **copy-trade link**.
- Another X user pointed out that the shown balance was **$1.19**, not $750k.
- There is no name, no verifiable primary source, and the numbers change between retellings ($750k vs $1.72M).
- Similar "student + Claude + Polymarket" stories ($1,400 → $238k) circulate with the same structure.

**What's real about it:**
- Latency arbitrage between a fast reference price (Binance) and slow prediction-market odds has been a known Polymarket strategy.
- It is a **speed and infrastructure game** that gets arbitraged away. Platforms respond with fees and rule changes; check whether Polymarket added taker fees on short crypto markets.
- A $100 account can't out-compete professional latency bots.
- Bottom line: **a real mechanism, an unverified story, and very likely promotional.**

**The "Chinese" one (Kronos, Dd-FFigDPFC):**
- A real model from Tsinghua (paper "Kronos: A Foundation Model for the Language of Financial Markets," AAAI 2026, github.com/shiyu-coder/Kronos).
- Pre-trained on more than 12 billion candlestick records from 45 exchanges.
- Claims better forecasting metrics than generic time-series models.
- It is a research tool, not a money printer, and the repo itself says so.

---

## 4. Plan

**Phase 0: Deep research (this prompt) → a go/no-go memo.** About 1 day.
- Run the prompt in section 5 in Claude (Research mode or Claude Code with web search).
- Output: a viability report plus a ranked shortlist of 1–2 strategy families and 1 prop firm.

**Phase 1: Learn and set up safely, with no real money.** 1–2 weeks.
- Paper accounts: Alpaca paper, Hyperliquid testnet, a prop firm's free trial or demo, Polymarket/Kalshi small-stake or "watch only."
- Install **OpenAlice** or **Fincept Terminal** locally, connected to Claude Code through MCP, in **approval-required mode**.
- Build the **4-question validation harness** (out-of-sample, neighbours, costs, scrambled market) plus Monte Carlo of **prop-firm rules** *before* any strategy work.

**Phase 2: Strategy research loop.** 2–4 weeks.
- Claude reads SSRN/Quantpedia papers, codes them in a backtester, and runs them through the harness.
- A Skeptic agent with veto power, plus a dated "lessons" file the agent must read first (@fidetolabs).
- Kill anything that fails any of the 4 questions.

**Phase 3: Prop-firm evaluation, first real money (about $50–100).**
- Choose a firm whose rules **explicitly allow bots/EAs/API** (to be researched; Propr says it does, and futures firms vary).
- Size the strategy so that a **Monte Carlo of the firm's exact drawdown and daily-loss rules** gives a high pass probability *and* survives the funded phase.
- Start with the cheapest evaluation and treat the fee as tuition.

**Phase 4: Only if the funded account pays out** for 2–3 months, consider scaling. Never chase screenshots.

**Guardrails throughout:**
- Hard daily-loss kill switch in code, below the firm's limit.
- Human approval for every live order at first.
- API keys with **trade-only, no-withdrawal** permissions.
- Never run strangers' "setup guides" or copy-trade links.
- Log every trade.
- No leverage beyond the firm's.
- Taxes and jurisdiction checked.

---

## 5. Deep-research prompt (copy-paste into Claude)

```
You are my research analyst. I want a rigorous, skeptical, well-sourced DEEP RESEARCH REPORT on whether I can realistically use Claude (Claude Code / Claude.ai with MCP connectors) to build and run an automated or semi-automated trading system, starting with prop-firm evaluations and a ~$100 budget. Use web search extensively, cite every factual claim with a link, show dates, and clearly label anything unverified. Prefer primary sources (official docs, rulebooks, GitHub repos, regulator sites, peer-reviewed or arXiv papers) over influencer content. Where sources conflict, say so.

## Context: what I've seen
I watched ~36 Instagram reels about "Claude trading bots." Claims and tools mentioned:
- A "19-year-old student in Japan" who supposedly built a Claude Code bot in 2 days that turned $68 into ~$750,000 by comparing 50+ markets to live Binance BTC prices and trading short-lived mispricings (reportedly Polymarket 15-minute "BTC Up or Down" markets; execution via "OpenClaw"; promoted with a paid-partnership copy-trade link).
- "6 Grok bots" / "JEV" multi-agent desks (Scout, News, Sentiment, Chart, Skeptic/Risk veto, Decision) claiming $89→$55k, $1k→$101k, $100→$52k, $63→$9k (self-reported, no wallets).
- "Claude turned $80 into $4,218" (rules: trade strongest time windows, size by confidence, fixed risk limits (~2%/trade), log every trade).
- Claude + Liquid (multi-asset + prediction-market broker) + Quiver Quant (Congress/insider/institutional trades) as an alert/recommendation agent with Routines and paper trading.
- Robinhood giving AI agents their own funded "MCP account."
- Alpha Arena Season 1 (Nof1, Oct–Nov 2025): 6 LLMs with $10k each; most lost heavily.
- Paper "Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets" (Ross, So, De Simone, Pozniak & Lo) on AI herding; Bank of England speech "Agents of change" (Sarah Breeden, 30 June 2026) on AI trading kill switches.
- Open-source tools: OpenAlice (TraderAlice), Fincept Terminal (free "Bloomberg-style" terminal, 37 agents, 100+ data connectors), Vibe-Trading (HKUDS), Hummingbot (+ Condor), Kronos (Tsinghua candlestick foundation model, AAAI 2026), Pythia (event/market forecaster), World Monitor (koala73), a Kalshi "Krypt Trader" agent council, Microsoft SkillOpt.
- Paper-to-bot workflows: SSRN or Quantpedia → Astral / DeepSeek / Claude → MQL5 in MT5 or Python backtests.
- Prop firms: Propr (crypto prop on Hyperliquid; "Explorer 1-Step Turbo" $50 for 10,000 USDC, 9% target, 3% static max drawdown, 3% daily loss, 80% split); futures prop accounts (25K/50K) run by bots ("Phantom Trader A.I."); a seller claiming "94.18% Monte Carlo chance of passing a $50k eval" on MNQ; "IV walls" (expected range from implied plus historical volatility, "90%/100% win rate").
- Validation advice: out-of-sample, walk-forward, Monte Carlo on every parameter set, parameter-stability heatmaps, cluster analysis, deflated Sharpe, slippage and commissions, scrambled-market null tests (8,500 tests → best Sharpe looks like luck), point-in-time news timestamps (37% of news after the close; Sharpe 3.18 → 0.98 when fixed), half position size on "cautious" news days, a dated lessons file for agent memory.

## Questions to answer

1. QUANT TRADING FUNDAMENTALS
   - What is quantitative trading? Main strategy families (trend/momentum, mean reversion, stat-arb/pairs, market making, carry, volatility/options, event/news-driven, arbitrage/latency, ML signals). Which are realistically accessible to a retail individual with small capital and consumer infrastructure, and which are dominated by firms with co-location and scale?
   - Realistic expectations: typical Sharpe ratios, capacity, alpha decay, transaction costs, slippage, and why most retail algos fail. The multiple-testing problem (deflated Sharpe, Bailey & López de Prado), look-ahead and survivorship bias.
   - A concrete validation protocol I should follow before risking money (combine the reel advice above with the academic literature).

2. CAN LLMs / CLAUDE ACTUALLY TRADE?
   - Evidence on LLM trading performance: Alpha Arena results (all seasons available), academic papers on LLM trading agents (e.g. TradingAgents, FinMem, FinAgent, StockAgent), the "better models → herding" paper, ChatGPT headline-sentiment studies and decay of returns.
   - Where an LLM plausibly adds value (research, coding, news and sentiment parsing, risk checks, journaling, a strategy-research loop) vs where it shouldn't be in the loop (latency-sensitive execution, sizing without hard rules).
   - Best architecture: Claude as researcher/coder/supervisor plus deterministic execution code plus hard risk rules. Evaluate multi-agent "desk" designs (Scout/News/Chart/Skeptic/Risk/Decision) vs a single agent with skills.
   - Costs: Claude API / subscription costs per decision, latency, and when a cheaper or faster model is needed.

3. TOOL-BY-TOOL EVALUATION
   For each, give: what it is (official link), license/cost, maturity (stars, last commit, issues), what it can and can't do, security risks, and whether it fits a $100 / prop-firm plan:
   OpenAlice, Fincept Terminal, Vibe-Trading (HKUDS), Hummingbot (+Condor), Kronos, Pythia, World Monitor, Kalshi Krypt Trader (find the repo), Quiver Quant (API/MCP), Liquid (what is it, regulated where?), Robinhood agent/MCP accounts (availability, rules), Alpaca (paper trading, MCP server), Interactive Brokers API, CCXT, Binance API, Hyperliquid API/testnet, Polymarket API (CLOB, fees especially on short crypto markets, geo-restrictions), Kalshi API (eligibility, fees), Astral, Quantpedia, SSRN, MT5/MQL5, NinjaTrader/Tradovate/Rithmic (for futures prop bots), QuantConnect/LEAN, Backtrader/vectorbt, Microsoft SkillOpt.
   Also compare the real Bloomberg Terminal (cost, what it provides) with these free alternatives, and say honestly what I lose by not having it.

4. PREDICTION MARKETS
   - How Polymarket and Kalshi work, fees, liquidity, who can legally use them (consider my jurisdiction: [FILL IN COUNTRY/STATE]).
   - The latency-arbitrage strategy behind the "19-year-old" story: is it real, how did it work, was it killed by fees or rule changes (check Polymarket's dynamic taker fees on short crypto markets), and what infrastructure does it need?
   - Forecasting-based strategies (LLM forecasters vs market prices; evidence from forecasting tournaments).

5. PROP FIRMS (most important for my start)
   - Compare current (2026) prop firms that ALLOW automated trading / bots / EAs / API, for futures (e.g. Topstep, Apex, Take Profit Trader, MyFundedFutures, Tradeify, Lucid, and others), crypto (Propr on Hyperliquid, HyroTrader, Breakout and others), and forex/CFD (FTMO, The5ers, FundingPips and others). For each: eval price (cheapest tier ≤ $100?), account size, profit target, daily loss, max drawdown type (static/trailing/EOD), consistency rules, minimum days, payout rules and split, activation fees, EXPLICIT bot/automation/copy-trading/HFT/latency-arb/news-trading policy (quote the rule and link), platform/API, reputation (Trustpilot, payout proof, history of rule changes or denied payouts), and regulatory status.
   - Which strategy types fit prop rules (drawdown limits punish high-variance and martingale; consistency rules punish one big day).
   - Design a method to Monte Carlo a strategy's trade distribution against a specific firm's rules to estimate (a) pass probability, (b) expected number of eval purchases before a pass, (c) probability of reaching a payout, (d) expected value per $ of eval fees. Give a Python outline Claude Code can implement.
   - Prop-firm business model reality: what share of traders pass and get paid; sim-funded vs live capital; known scams or rule-based payout denials.

6. THE $100 PLAN
   - Option A: one or two cheap prop evals (≤ $100) with a validated bot. Option B: a $100 personal account (crypto perps, micro futures need more margin, prediction markets, fractional stocks). Option C: paper only until validated. Compare expected outcomes honestly, including fees, minimums, leverage risk, and taxes.
   - A concrete step-by-step setup plan (accounts, tools, MCP connections, validation harness, risk kill switch, logging, approvals) with time estimates.

7. HYPE AUDIT
   - Investigate the specific viral claims (19-year-old Japan $68→$750k; 6 Grok bots/JEV; Claude $80→$4,218; "94.18% pass chance"; "IV walls 100% win rate"; Phantom Trader A.I.; "comment X for setup" funnels). Try to find primary sources (X accounts, wallets, repos). Classify each: verified / plausible but unverified / likely misleading / scam pattern. Explain survivorship bias, deposits mid-run, meme-coin luck, paid partnerships, and copy-trade/affiliate incentives.

8. RISKS, SECURITY & LEGAL
   - Security of giving an AI agent trading keys (prompt injection via news/web content, malicious repos/"setup guides," API key scopes, no-withdrawal keys, sandboxing).
   - Regulation: prediction-market legality, prop-firm regulatory gaps, offshore exchanges, taxes in [MY JURISDICTION], broker ToS on automation.
   - AI herding/flash-crash risk and why "the same Claude prompt as everyone else" has no edge.

## Output format
1. Executive summary (one page): is this viable, for whom, best path for me, expected outcome ranges, and what would change your mind.
2. Quant trading explainer (plain English, then technical).
3. Tool comparison table plus recommended stack.
4. Prop-firm comparison table (automation-friendly only, with linked rule quotes) plus top 3 picks for a ≤ $100 start.
5. Hype-audit table of the viral claims.
6. Step-by-step 30/60/90-day plan with gates (don't proceed unless X).
7. Validation-harness and prop-rule Monte Carlo spec (pseudocode/Python outline).
8. Risk register plus security checklist.
9. Sources list.
Be blunt. If the honest answer is "this mostly doesn't work for retail," say so, and then tell me the best version of it that could.
```

---

## 6. Sources checked for this brief
- The 19-year-old story on X: [Future Stacked](https://x.com/FutureStacked/status/2072340089829462203), [AdiiX](https://x.com/adiix_official/status/2049523561518313947), [0x_Discover (paid partnership)](https://x.com/0x_Discover/status/2049765508300353943)
- Blog retelling: [He Built a Trading Bot in 48 Hours](https://storiesoftheendlessarc.blogspot.com/2026/08/he-built-trading-bot-in-48-hoursthen.html)
- A similar story ($1,400 → $238k): [Threads post](https://www.threads.com/@businessbulls.in/post/DWN4Lc-kuin/a-student-reportedly-turned-into-in-days-using-a-trading-bot-built-with-claude)
- Kronos:
  - [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/39730)
  - [Hugging Face paper page](https://huggingface.co/papers/2508.02739)
  - [Pebblous summary](https://blog.pebblous.ai/report/kronos-financial-foundation-model/en/)
- Propr:
  - [fundedtrading.com review](https://fundedtrading.com/propfirm/propr/)
  - [Cointelegraph press release](https://regional-front.cointelegraph.com/press-releases/propr-launches-onchain-prop-trading-firm-hyperliquid)
- OpenAlice:
  - [gittrend listing](https://gittrend.io/repo/TraderAlice/OpenAlice)
  - [sourcepulse listing](https://www.sourcepulse.org/projects/24951030)
  - [awesome-trading-agents](https://github.com/LLMQuant/awesome-trading-agents)
- Repos named in captions:
  - [Fincept Terminal](https://github.com/Fincept-Corporation/FinceptTerminal)
  - [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)
  - [Microsoft SkillOpt](https://github.com/microsoft/SkillOpt)

---

## 7. Added Oct 23: "Free AI hedge fund, 11 agents" (@msbintel, DewXNu0jrzS)
**Claim:** a free GitHub project runs a crypto desk like a hedge fund, with 11 agents in 5 jobs. "11 AI agents. None can click BUY."

**The desk (on-screen diagram):**
1. **Screener** (×1) picks the coins worth a look from BTC, ETH, SOL, XRP, ADA, DOGE, AVAX, LINK, DOT, LTC, ATOM and NEAR. The example picks 3.
2. **Analysts** (×4) each build a case:
   - charts
   - the economy
   - on-chain/blockchain data
   - the mood online (the Crypto **Fear & Greed Index** from alternative.me is shown)
3. **Validators** (×3) poke holes in it: one argues for, one against, one stays neutral.
4. **Risk manager** (×1) **can veto any trade**.
5. **Auditors** (×2) review every trade afterward (a trade log with "reviewed" ticks).

**The smart part:** **the AI never places the order. It only pitches.** Plain code ("fixed rules") does the math, sets the size and caps risk per trade, so a bad AI answer like "go all in!" can't wreck the account. It starts on **paper trading** ("test with fake money → watch the results → then decide"). The caption hashtags mention **Bybit**.

**Repo:** not named in the reel. The link is gated behind commenting "FUND". Web searches found no exact match, but these are close relatives worth comparing:
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) and its crypto fork [TradingAgents-crypto](https://github.com/auronsun/TradingAgents-crypto): analysts, a bull/bear debate and risk debaters.
- [cubexch/ai-fund](https://github.com/cubexch/ai-fund): Claude Code, dozens of persona agents, paper trading by default.
- [MLgeek96/Multi-Agentic-AI-Quantitative-Trading](https://github.com/MLgeek96/Multi-Agentic-AI-Quantitative-Trading): independent risk veto plus audited agents.
- [Jev-Trades](https://github.com/zadescoxp/Jev-Trades): code handles sizing, take-profit and stop-loss; paper trading by default with optional Bybit testnet.

**Why it matters for our plan:** this is the right architecture. The LLM pitches and argues, deterministic code sizes and executes, a risk agent can veto, and auditors review afterward. It matches section 4's guardrails. Add "identify this repo and compare it with TradingAgents / ai-fund" to the research prompt's tool list (section 5.3).

---

## 8. Added Oct 23: four more reels

### 8.1 The prop-firm math paper (@davidtrades_model, DezXMPwoZL0)
**The paper:** [*Prop-Firm Challenges: A Barrier Model of Pass Rates and Expected Value*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7445798) by Rubén Villahermosa, on SSRN.

**What it shows:**
- A challenge is a race between two lines: the **profit target T** above and the **loss limit L** below.
- With **no edge**, your chance of passing is **L ÷ (T + L)**, *whatever the volatility*.
- On a standard challenge that's **44.4%**.
- Measured on real index-futures sessions (6 years of 1-minute data; the caption says 1,713 sessions), it falls to **40.4%** with the daily loss bracket and **34.7%** with a trailing drawdown.
- It then prices the whole life of a funded account. The paper's expected value per evaluation is about **+0.052 L at the fee actually paid and -0.018 L at list price**. In other words, without an edge the product only breaks even at discount prices.

**Why it matters:** this is the exact maths our Phase 3 needs.
- **Pick firms where L is large relative to T.**
- **Avoid trailing drawdowns** where possible.
- **Only buy evaluations at a discount.**
- **Size trades so that your edge, not luck, carries you.**

Add this paper to the deep-research prompt (section 5, question 5) and have Claude build the Monte Carlo on top of the formula. The creator's "comment PROFIT" prompts weren't accessed.

### 8.2 and 8.3 "3PO" AI quant, the same creator as #10 (@astongilltrading, DcYpBhBod3b + DcOV72Eo_NO)

**Claims:**
- A **25-day win streak** and **5 payouts**, "100% winning days in the last 5 weeks," fully automated.
- Shown on a **Lucid Trading "LucidFlex 50K"** futures prop account: balance about $52,574 against a $50,100 minimum, +$1,418 this payout period, 25 trading days.
- He requests a payout of about $1,300 live on camera, in crypto.

**How it works:**
1. 3PO scans the internet for quant papers and books (1,100+ research items).
2. It turns them into **about 72,000 strategies**.
3. Each strategy runs a gauntlet: in-sample screening → sweep neighbourhood → cost sensitivity → out-of-sample → walk-forward → Monte Carlo → deflated Sharpe → plateau → regime tests.
4. It picks the winners per **market regime**.
5. It executes through **NinjaTrader 8 (futures), MetaTrader 5/4 (forex), MultiCharts and Interactive Brokers (stocks), and CCXT (crypto)**.

**Stated results:**
- Combined: 57% win rate, +120R, profit factor 2.54, average win 1.37R vs average loss about 0.7R.
- Per market: futures +$6.5k with a $483 drawdown, forex +$3k, stocks +$5k, crypto +$3.5k.
- Phone alerts.

**Caveats:**
- It's a sales funnel ("comment ACCESS").
- One account's streak is a small sample, and these payouts are around $1.3k.
- The pipeline itself is textbook-correct and the closest public example of what our plan describes.
- Lucid Trading permitting this level of automation is worth adding to the prop-firm research list.

**Dashboard screenshots are saved in** [`trading-dashboard-inspo/`](trading-dashboard-inspo/), with design notes.

### 8.4 GPT-6 Astra trading NQ on a simulator (@faiz.smc, Dd9y_pys7WQ)
**What happens:** the creator lets **OpenAI's GPT-6 Astra** (released Sep 2026, strong at *computer use*) trade **1 NQ contract on SIM** by operating the chart software:
- **Deepcharts** footprint/order-flow charts, CVD, big-trades tools.
- **Gamma exposure (GEX)** levels; the transcript says "mentored cube," probably MenthorQ.

**On screen:** the chat log shows 11 trades (full target +$800, stop -$400, three +$600 wins, a breakeven stop and so on), totalling **+$1,935 on SIM**. It wrote: "I inspected the enlarged footprint before entry and exited early when selling stalled and CVD recovered." The creator says "don't try this at home." Next he'll try to pass an evaluation in one day.

**What it means for us:**
- This is the "AI looks at the screen and clicks" approach. It's slow and costly per decision, and only one SIM day is shown.
- It's interesting as a research or discretionary assistant, not a robust bot.
- Its opposite is the 11-agent reel (§7): code, not AI, places orders.
- It shows **GEX** and **footprint/CVD** as data sources worth evaluating.
