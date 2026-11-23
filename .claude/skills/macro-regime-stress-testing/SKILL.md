---
name: macro-regime-stress-testing
description: "Classify market regimes and stress-test strategies and portfolios against historical crises and hypothetical shocks. Use for scenario analysis, regime context or tail-risk questions."
user-invocable: false
---
# Macro regime analysis and stress testing

## Regime dimensions
- Growth/inflation quadrant; policy rate direction; yield-curve slope.
- Volatility regime (VIX level and trend; realized vs implied).
- Correlation regime (stock-bond correlation sign; average pairwise equity correlation).
- Liquidity/credit (credit spreads, funding stress).

## Historical stress set (minimum)
| Episode | Why |
|---|---|
| 2000-02 dot-com bust | Long equity bear, momentum reversal |
| 2008 GFC | Correlation spike, liquidity crisis |
| Aug 2015 / Feb 2018 | Flash/volatility shocks, ETF dislocations |
| Q4 2018 | Rate-driven drawdown |
| Mar 2020 | Fastest crash, gap risk |
| 2022 | Stocks and bonds fall together (inflation) |

## Hypothetical shocks
Equity -20% overnight gap; rates +200bp; stock-bond correlation +0.6; vol doubles; broker/data outage for 2 days.

## Output
For each scenario: P&L, max drawdown, limit breaches triggered, kill switches that would fire, liquidity to exit. Flag any scenario that breaches the owner's max drawdown (default -15%).
