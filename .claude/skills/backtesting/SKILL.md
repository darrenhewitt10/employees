---
name: backtesting
description: "Build and run realistic backtests: one-bar delay, cost model, same signal code as live, tear sheet output; framework choice (custom, vectorbt, NautilusTrader, LEAN). Use for any strategy simulation."
user-invocable: false
---
# Backtesting

## Engine requirements
- **Same code path:** the function mapping data -> target weights is shared by backtest, paper and live.
- Decisions on bar *t* fill at *t+1* (open or VWAP proxy); no fills at bar high/low.
- Cost model on every trade: commission + regulatory fees + half-spread + impact `k*sigma*sqrt(size/ADV)`; crypto uses actual taker fee tier.
- Cash, fractional shares, lot sizes, borrow (if shorting), dividends and corporate actions handled.
- Deterministic and seeded; results keyed by commit hash + data snapshot + config.

## Framework choice
- Research sweeps: vectorbt or a small custom Polars engine (log every trial - speed makes overfitting easy).
- Pre-live and live: NautilusTrader (same code backtest->live) or QuantConnect LEAN.
- Avoid backtrader for new work (largely unmaintained).

## Every run produces
1. Config + trial ID appended to the trial log.
2. Tear sheet: CAGR, vol, Sharpe, Sortino, max DD and duration, Calmar, hit rate, turnover, holding period, exposure, beta, alpha t-stat, costs % of gross, after-tax estimate.
3. Benchmark comparison (buy-and-hold and the simplest version of the idea).
4. Sensitivity: costs x1.5, one extra bar delay.

Hand results to **validation-statistician**; never self-certify.
