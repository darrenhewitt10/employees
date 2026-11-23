---
name: risk-limits-kill-switches
description: "Specify, enforce and test risk limits and kill switches at account, strategy, position and order level. Use for any limit design, breach, or kill-switch question."
user-invocable: false
---
# Risk limits and kill switches (doc 07 defaults; owner may tighten or loosen)

## Limits
| Level | Control | Default |
|---|---|---|
| Account | Gross leverage | <= 1.0x |
| Account | Max drawdown from high-water mark | -15% -> halt, flatten to cash/benchmark, human review |
| Account | Daily loss | -2% -> stop for the day |
| Strategy | Capital share | <= 50% until proven |
| Strategy | Drawdown | 1.5x worst backtest DD -> auto-disable |
| Strategy | Turnover | annual cap + max trades/day |
| Position | Single name | <= 10% (broad ETFs <= 30%) |
| Position | Sector | <= 30% |
| Order | Notional, price collar (+/-2%), allowlist, duplicate check, buying power, session hours, max orders/minute | enforced in gateway |

## Kill switches
Drawdown limit · daily loss · reconciliation mismatch (freeze) · stale/failed data (skip rebalance) · order-rate anomaly · broker error spike · LLM anomaly (fall back to non-LLM signal) · manual flatten-all.

## Rules
- Limits live in the **risk gateway**, outside strategy code; strategies and agents cannot bypass them.
- Agents may **tighten** limits autonomously; **loosening requires logged owner approval**.
- Every kill switch has a paper fire drill at least monthly; record results.
