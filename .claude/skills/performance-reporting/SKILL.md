---
name: performance-reporting
description: "Produce performance reports: tear sheets, attribution, benchmark comparison and live-vs-backtest tracking, from computed numbers only. Use for daily/weekly/monthly reports or strategy reviews."
user-invocable: false
---
# Performance reporting

## Metrics (doc 06)
CAGR, volatility, Sharpe, Sortino, max drawdown and duration, Calmar, hit rate, avg win/loss, annual turnover, holding period, exposure, beta, alpha (t-stat), costs as % of gross, after-tax estimate.

## Reports
- **Daily:** P&L by strategy, positions, exposures, drawdown vs limits, limit breaches/near misses, kill-switch state, costs/slippage.
- **Monthly:** strategy vs benchmark (net of costs and estimated tax), live vs backtest over the same period (signal agreement, slippage, P&L gap), attribution (allocation vs selection vs costs).
- **Decision triggers:** flag strategies breaching kill criteria or tracking error tolerance.

## Rules
- **Numbers come from computed data only**; narrative explains them and never invents figures.
- Always show the benchmark and drawdowns next to returns; no cherry-picked periods.
- State the period, data snapshot and whether figures are paper or live.
