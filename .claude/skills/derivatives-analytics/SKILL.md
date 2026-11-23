---
name: derivatives-analytics
description: "Analyze options and futures: Greeks, margin, assignment and early exercise, futures rolls, skew/tail risk and Section 1256 treatment. Use for any options or futures sleeve question."
user-invocable: false
---
# Derivatives analytics

## Options
- Greeks per position and aggregate: delta, gamma, vega, theta; stress P&L for spot +/-10-20% and vol +/-50%.
- Short options are **negatively skewed**: cap notional, define max loss, prefer defined-risk spreads.
- Assignment/early exercise: American-style equity options can be assigned early (esp. before ex-dividend); system must handle resulting stock positions.
- Liquidity: open interest, bid-ask width; per-contract fees in the cost model.
- Broker options approval level gates what is possible.

## Futures
- Roll schedule (by volume/open-interest crossover), roll cost tracking, continuous-contract construction for backtests (back-adjusted vs ratio-adjusted; never trade on the stitched series).
- Margin: initial vs maintenance; keep margin usage well below limits; leverage counts in gross exposure.

## Tax (doc 09)
Regulated futures and broad-based index options are **Section 1256**: 60% long-term / 40% short-term, marked to market at year end.

## Gate
No derivatives until the equity pipeline is stable and the owner enables the asset class (default: disabled).
