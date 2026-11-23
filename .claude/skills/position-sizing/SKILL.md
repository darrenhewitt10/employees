---
name: position-sizing
description: "Size positions with volatility scaling and fractional Kelly using haircut expected returns. Use when deciding how much capital a position or strategy gets."
user-invocable: false
---
# Position sizing

## Methods
- **Volatility scaling:** `w_i = (target_vol / sigma_i) * base_weight_i`, capped by position limits. Use EWMA or 20-60 day realized vol; floor sigma to avoid huge weights.
- **Kelly:** continuous approximation `f* = mu / sigma^2`. Estimation error makes full Kelly dangerous - use **1/4 to 1/2 Kelly**, and only with edge estimated from **live/paper** data.
- **Equal risk contribution** across strategies and asset classes at the portfolio layer.

## Rules
- Haircut backtest expected returns by >= 50% before sizing.
- Size for the case where the signal has **zero edge**: the loss must be survivable.
- Never exceed the risk gateway limits; sizing proposes, the gateway disposes.
- Re-size on schedule (rebalance), not intraday in reaction to P&L.

## Output
Per position: target weight, vol estimate, risk contribution, which cap bound it.
