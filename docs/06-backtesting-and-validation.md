# 06 — Backtesting and Validation

> **Purpose for agents:** How to test a strategy so results mean something.
> The Validation (red-team) agent owns this document and has veto power over
> promoting any strategy to paper or live trading.

## Why most backtests lie

| Bias | What happens | Defense |
|---|---|---|
| **Look-ahead** | Uses information not available at decision time (restated fundamentals, close price used for same-bar entry, LLM memorization) | Point-in-time data; decisions at bar *t* execute at *t+1* open or later; post-cutoff testing for LLMs |
| **Survivorship** | Universe excludes delisted/bankrupt firms | Survivorship-free datasets |
| **Overfitting / data snooping** | Many variants tried; best one reported | Pre-registration, trial logging, DSR, PBO, holdout |
| **Cost neglect** | Ignoring spread, slippage, fees, borrow, taxes | Explicit cost model calibrated to live fills |
| **Regime dependence** | Works only in one market regime | Test across 2000–02, 2008, 2015, 2018 Q4, 2020, 2022 sub-periods |
| **Implementation gap** | Backtest engine fills unrealistically (e.g., at the high/low) | Event-driven sim with realistic fills; paper trading |

## Validation protocol (required for every strategy)

1. **Pre-register** the hypothesis, economic rationale, universe, parameters
   to tune and their ranges, and the success metric — committed to git
   *before* running tests.
2. **Log every trial.** The number of configurations tried (*N*) is needed to
   deflate results. Untracked trials invalidate the study.
3. **Split data:** development period → walk-forward validation → final
   **untouched holdout** (most recent 1–2 years, used once).
4. **Walk-forward / purged CV:** for ML models, use purged K-fold with an
   embargo (López de Prado, *Advances in Financial Machine Learning*) or
   combinatorial purged CV so overlapping labels don't leak.
5. **Statistical bars:**
   - **Deflated Sharpe Ratio (DSR)** — corrects Sharpe for multiple testing
     and non-normal returns (Bailey & López de Prado, *J. Portfolio Mgmt*,
     2014; [SSRN](https://papers.ssrn.com/abstract=2460551)). Proposed gate:
     DSR ≥ 0.95.
   - **Probability of Backtest Overfitting (PBO)** via combinatorially
     symmetric cross-validation (Bailey, Borwein, López de Prado & Zhu,
     *J. Computational Finance*; [SSRN](https://papers.ssrn.com/abstract=2326253)).
     Proposed gate: PBO ≤ 0.2.
   - t-stat of mean excess return ≳ 3 (Harvey, Liu & Zhu 2016 haircut).
6. **Robustness:** parameter sensitivity (performance should be a plateau, not
   a spike), alternate universes, ±50% cost assumption, delayed execution by
   one bar, removal of best 5 trades/days.
7. **Benchmark comparison:** vs. buy-and-hold and vs. the simplest version of
   the idea (e.g., ML model vs. plain momentum rank).
8. **Paper trading:** minimum 3 months (or ≥ 50 rebalances for faster
   strategies), comparing live signals, fills and PnL against a backtest run
   over the same period.
9. **Holdout reveal** last, once; if it fails, the strategy is rejected, not
   re-tuned.

## Metrics to report (standard tear sheet)

CAGR, volatility, Sharpe, Sortino, max drawdown and duration, Calmar, hit
rate, average win/loss, turnover (annualized), average holding period,
exposure, beta to benchmark, alpha (with t-stat), costs as % of gross return,
tax-adjusted return estimate, DSR, PBO, number of trials *N*.

## Frameworks

| Framework | Style | Live trading | Notes |
|---|---|---|---|
| **vectorbt** (OSS) / vectorbt PRO | Vectorized (NumPy/Numba) | No native | Fastest for parameter sweeps and research; easy to overfit *because* it's fast — log trials |
| **NautilusTrader** | Event-driven, Rust core, Python API | Yes (multiple venues incl. IBKR, Databento data, crypto) | Same code for backtest and live; production-grade; steeper learning curve |
| **QuantConnect LEAN** | Event-driven (C#/Python) | Yes (cloud or self-hosted) | Large data library in cloud; open-source engine; cloud tiers ~$0–$400/mo |
| **backtrader** | Event-driven | Some brokers | Popular but largely unmaintained; avoid for new builds |
| **zipline-reloaded** | Event-driven, daily focus | No | Maintained fork of Quantopian's Zipline; good for daily equity research |
| **Freqtrade** | Crypto bot framework | Yes (crypto exchanges) | Batteries-included for crypto; hyperopt makes overfitting easy |
| **Custom (pandas/Polars)** | Simple vectorized rebalance sim | — | Fine for daily/weekly portfolio strategies; must share code with live signal generation |

Sources: third-party comparisons ([DEV, 2026](https://dev.to/pickuma/quantconnect-vs-backtrader-vs-vectorbt-which-to-start-with-in-2026-4954),
[NautilusTrader overview](https://groundy.com/articles/nautilustrader-building-production-ready-algorithmic/)) — opinions vary; benchmark claims are not comparable across sources.

### Recommendation

- **Research:** vectorbt or a small custom Polars engine for daily/weekly
  portfolio strategies.
- **Pre-live validation and live:** **NautilusTrader** (broker/infra-agnostic,
  same code path backtest→live) — or LEAN if we prefer a managed cloud.
- **Golden rule:** the function that turns data into target weights must be the
  *same code* in backtest, paper, and live. Divergent implementations are a
  leading cause of live underperformance.

## Promotion gates summary

| Stage | Gate to pass |
|---|---|
| Idea → Backtest | Pre-registration committed; rationale reviewed |
| Backtest → Paper | DSR ≥ 0.95, PBO ≤ 0.2, beats benchmark net of costs, robustness checks pass, Risk agent sign-off |
| Paper → Live (small) | ≥ 3 months paper; live-vs-backtest tracking within tolerance; zero operational incidents; human approval |
| Small live → Scaled | ≥ 6 months live within risk limits; realized slippage ≤ modeled; human approval |
