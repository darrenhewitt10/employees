---
name: portfolio-construction
description: "Convert signals into constrained target weights: position and sector caps, volatility targeting, risk parity, turnover penalties and minimum trade thresholds. Use when designing how strategies become holdings."
user-invocable: false
---
# Portfolio construction

## Steps
1. **Normalize signals** to comparable scores (z-score or rank) per rebalance date.
2. **Map to raw weights** (e.g. rank-proportional, top-quantile equal weight, or inverse-vol weighted).
3. **Apply constraints:** single position <= 10% of strategy capital (broad-index ETFs up to 30%); sector/theme <= 30%; long-only and gross <= 1.0x by default; liquidity: order <= 1% of 20-day ADV.
4. **Volatility target** (e.g. 10-12% annualized): scale exposure by target/forecast vol, capped at 1.0x.
5. **Turnover control:** penalize changes or use a no-trade band; skip trades below a minimum notional/% threshold.
6. **Combine strategies** with fixed capital allocations or equal risk contribution; no strategy > 50% until proven.
7. **Output** target weights + the diff vs current holdings for the order planner.

## Rules
- Deterministic and shared by backtest and live.
- Log the full decision record (inputs, scores, constraints hit, final weights).
- Cash/T-bill ETF is the default holding when signals are weak or data is bad.
