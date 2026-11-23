# 12 — Decisions Needed from the Owner

> **Purpose for agents:** Open questions only the owner can answer. Until they
> are answered, agents use the **default** shown and must not exceed it.

| # | Question | Why it matters | Default until answered |
|---|---|---|---|
| 1 | **Jurisdiction / tax residence?** | Regulation, tax rules, broker availability | US resident individual |
| 2 | **How much capital for automated trading, and how much can you afford to lose entirely?** | Position sizing, broker/account type, whether costs dominate | Paper trading only |
| 3 | **Account type:** taxable, IRA, or both? Cash or margin? | Tax drag, wash sales, shorting/leverage availability | Taxable cash account, no margin |
| 4 | **Objective:** beat the market, reduce drawdowns, generate income, or learn? | Strategy selection and benchmark | Risk-adjusted outperformance vs. a passive ETF benchmark |
| 5 | **Maximum acceptable drawdown?** | Kill-switch thresholds | −15% account, −2% daily |
| 6 | **Asset classes allowed?** (ETFs, stocks, options, futures, crypto) | Data, broker, and risk scope | US ETFs and stocks, long-only |
| 7 | **Holding period preference / time you'll spend monitoring?** | Intraday vs. daily vs. weekly design; ops burden | Daily-to-weekly rebalancing |
| 8 | **Broker preference or existing accounts?** | Adapter priority | Alpaca (paper first) |
| 9 | **Budget for data, LLM API, and hosting per month?** | Vendor choices, LLM usage limits | ≤ $150/month total |
| 10 | **Approval mode for live trades:** fully automatic within limits, or human confirms each rebalance? | Execution workflow | Human confirms each live rebalance |
| 11 | **Restricted symbols** (e.g., your employer, holdings with lockups)? | Compliance | Empty list — must be confirmed before live |
| 12 | **Will you ever trade for others or share signals?** | Registration obligations | No (personal account only) |
| 13 | **Tax professional involvement?** (trader tax status, §475 election) | Lot accounting design | No election assumed |
