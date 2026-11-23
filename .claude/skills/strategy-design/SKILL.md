---
name: strategy-design
description: "Design and pre-register trading strategies with an economic rationale: trend, momentum, volatility targeting, factor tilts, mean reversion, event and text signals. Use when proposing or changing a strategy."
user-invocable: false
---
# Strategy design

## Principles (doc 02)
- Economic rationale first (risk premium, behavioral bias, structural flow, limits to arbitrage).
- Low-to-moderate turnover; no speed-based edges at retail scale.
- Published anomalies decay (~58% lower post-publication, McLean & Pontiff 2016) - haircut expectations.
- Start simple: passive benchmark -> trend filter -> vol targeting -> multi-asset TS momentum -> LLM text tilt.

## Families
Passive + rebalance (benchmark) · time-series momentum/trend · cross-sectional momentum · volatility targeting/risk parity · factor tilts · short-term mean reversion · pairs/stat-arb · event-driven (PEAD) · text/NLP signals · options income · crypto trend/carry. Avoid HFT, market making, latency arbitrage.

## Pre-registration template (`research/<strategy>/PREREG.md`)
```markdown
# <Strategy> pre-registration (<date>, commit <hash>)
Hypothesis and economic rationale:
Universe and data (with survivorship handling):
Signal definition:
Portfolio construction and rebalance frequency:
Parameters to tune and ranges (max trials):
Cost assumptions:
Benchmark:
Success metrics and gates (DSR, PBO, net excess return):
Kill criteria (live drawdown that disables it):
```
Commit it **before** running any test.
