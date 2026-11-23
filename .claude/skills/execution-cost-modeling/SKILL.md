---
name: execution-cost-modeling
description: "Design order execution and transaction-cost models: order types, collars, slicing, auctions, slippage measurement and feedback. Use for execution design or when live costs differ from backtests."
user-invocable: false
---
# Execution and transaction-cost modeling

## Execution principles (doc 05)
1. Marketable **limit** orders with a price collar; no market orders outside regular hours.
2. Deterministic `client_order_id` = hash(strategy, rebalance_id, symbol) for idempotent retries.
3. Slice orders above a small % of ADV over the execution window.
4. Avoid the first/last minutes unless deliberately using MOO/MOC auction orders.
5. Cancel unfilled orders at window end; log reasons.
6. 23x5 sessions (from Dec 2026) have thin overnight liquidity: regular session by default.

## Cost model
`cost = commission + reg fees (SEC Sec. 31, FINRA TAF on sells) + half-spread + k * sigma * sqrt(order_size / ADV)`
Half-spread defaults by liquidity bucket: 1-2 bps mega-cap ETFs; 5-20+ bps small caps. Crypto: actual taker fee tier (often 0.4%+ at low volume).

## Slippage measurement
Per fill: vs decision price and vs arrival price, in bps. Weekly: compare realized vs modeled; if realized > modeled, update the backtest cost model and re-validate affected strategies.
