# 01 — Reality Check: What an AI Trader Can and Cannot Do

> **Purpose for agents:** Read this first. It sets the expectations every other
> document assumes. Any agent proposing a strategy, a target return, or a
> timeline should be consistent with the evidence here.

## TL;DR

- Most active retail traders lose money, and "AI" does not change the math by
  itself. The edge has to come from a real, testable market inefficiency plus
  disciplined risk and cost control.
- Public tests of frontier LLMs trading on their own (2025–2026) mostly **lost
  money**, overtraded, and behaved inconsistently under identical prompts.
- Academic work shows LLMs *can* extract useful signal from text (e.g., news
  headlines), but that signal is strongest in small or illiquid stocks, decays
  as adoption grows, and is easy to overstate through look-ahead bias.
- The realistic goal for a personal AI trading system is: **a disciplined,
  automated, well-risk-managed portfolio that tracks or modestly beats a simple
  benchmark after costs and taxes, without blowing up.** Anything promising
  much more should be treated as a red flag.

## Evidence

### Retail active trading outcomes

- **"Day Trading for a Living?"** (Chague, De-Losso, Giovannetti; FGV/SSRN,
  2019, revised): of everyone who started day trading Brazilian equity index
  futures in 2013–2015 and persisted for 300+ days, **97% lost money**; only
  ~0.5% earned more than a bank teller's starting salary; no evidence traders
  improved with experience.
  ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101))
- A 2025 follow-up concludes that day trading systematically transfers wealth
  from individuals to financial institutions.
  ([Brazilian Review of Finance](https://periodicos.fgv.br/rbfin/article/view/94291))

### LLMs trading autonomously

- **Nof1 Alpha Arena, Season 1 (crypto, Oct–Nov 2025):** six frontier models
  each traded real money. Only two finished positive (Qwen3‑Max ≈ +22%,
  DeepSeek); GPT‑5 lost ~62–63%. Nof1 noted early-run PnL was **dominated by
  trading costs because agents overtraded.**
  ([Forklog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/),
  [Protos](https://protos.com/llm-crypto-trading-contest-finds-llms-cant-trade-crypto))
- **Later Alpha Arena seasons (US tech stocks, 2026):** eight systems
  (including Claude, Gemini, ChatGPT, Grok) ran $10k each across four
  competitions; only 6 of 32 results were positive and the aggregate fell
  ~33%. Under the *same prompt*, one model made 1,418 trades and another 158.
  ([ThinkAdvisor/Bloomberg, May 2026](https://www.thinkadvisor.com/2026/05/06/why-ai-bots-arent-ready-to-replace-your-fund-manager/),
  [Bloomberg Law](https://news.bloomberglaw.com/banking-law/ai-bots-auditioning-for-wall-street-trading-are-mostly-losing))
- A tracker of 11 public AI trading competitions found every event had at least
  one profitable model (survivorship!) but only two had a **profitable median**.
  (same Bloomberg coverage)
- **StockBench** (Tsinghua et al., arXiv 2510.02209): LLM agents trading DJIA
  stocks Mar–Jun 2025. Some beat buy-and-hold, **usually by slim margins**;
  performance fell as the tradable universe grew from 5 to 30 stocks; strong
  financial-QA scores did **not** translate into trading skill.
  ([arXiv](https://arxiv.org/abs/2510.02209))

### Where LLMs *do* show value

- **Lopez-Lira & Tang, "Can ChatGPT Forecast Stock Price Movements?"**
  (arXiv 2304.07619, v6 Oct 2025): LLM-scored headline sentiment predicts
  next-day returns and beats classic sentiment methods; smaller models
  (GPT‑1/2, BERT) can't. Predictability is concentrated in **small stocks and
  bad news**, and **strategy returns decline as LLM adoption rises.**
  ([arXiv](https://arxiv.org/abs/2304.07619))
- Caveat: see look-ahead bias in [03-ai-ml-approaches.md](03-ai-ml-approaches.md#look-ahead-bias-in-llms)
  — memorization can inflate backtested LLM predictive power substantially.

### Regulators' warnings

- **CFTC advisory "AI Won't Turn Trading Bots into Money Machines"** (Jan 2024)
  and the **SEC/NASAA/FINRA joint alert on AI investment fraud**: claims of
  high or guaranteed returns from AI bots are a classic fraud pattern; AI cannot
  predict sudden market shifts.
  ([CFTC](https://www.cftc.gov/LearnandProtect/AdvisoriesAndArticles/AITradingBots.html),
  [Investor.gov](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/artificial-intelligence-fraud))

## Implications for our design

1. **Benchmark everything.** Every strategy must be compared, after costs and
   taxes, to a passive alternative (e.g., a broad-market ETF buy-and-hold, or
   60/40). If it can't beat that with a statistically credible margin, we run
   the passive alternative.
2. **The LLM is not the trader.** Put LLMs where they have demonstrated value
   (reading text, research assistance, summarizing, anomaly explanation,
   code generation, oversight) and keep order generation deterministic,
   rule-bound, and risk-gated. See [08-system-architecture.md](08-system-architecture.md).
3. **Turnover is the enemy.** Overtrading was the most common failure mode in
   public LLM contests. Hard caps on trade frequency and turnover belong in the
   risk layer, not the prompt.
4. **Survive first.** Drawdown limits and kill switches matter more than
   expected return. See [07-risk-management.md](07-risk-management.md).
5. **Earn the right to scale.** Paper trade, then trade tiny, then scale only
   when live results match the backtest. See [11-agent-team-and-roadmap.md](11-agent-team-and-roadmap.md).

## Success criteria (proposed)

| Metric | Minimum bar to keep running live |
|---|---|
| Net return vs. benchmark (after fees, slippage, tax drag) | ≥ benchmark over rolling 12 months, or clear risk-reduction benefit |
| Max drawdown | Within the pre-agreed limit (e.g., ≤ 15–20% of strategy capital) |
| Live vs. backtest tracking | Slippage and signal hit rate within pre-registered tolerance |
| Operational incidents | Zero unreconciled positions; zero orders outside risk limits |
