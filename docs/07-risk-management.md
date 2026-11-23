# 07 — Risk Management

> **Purpose for agents:** The rules that keep the account alive. The Risk
> Manager agent owns this document and holds **veto power** over every trade,
> strategy promotion, and limit change. Limits here are *proposed defaults*
> pending the owner's decisions in [12-decisions-needed.md](12-decisions-needed.md).

## Principles

1. **Survival over return.** A 50% loss needs a 100% gain to recover.
2. **Limits live in code outside the strategy.** A separate risk gateway
   enforces them; strategies and LLM agents cannot override them.
3. **Limits only loosen with human approval.** Agents may tighten limits
   automatically; loosening requires an explicit, logged owner approval.
4. **Assume the model is wrong.** Size for the case where the signal has zero
   edge.

## Layers of control

### 1. Account level
| Control | Proposed default |
|---|---|
| Capital allocated to automated trading | Only money the owner can afford to lose; start with a small fraction of planned capital |
| Gross leverage | ≤ 1.0× (no margin) in early phases |
| Max account drawdown from high-water mark | −15% → halt all new risk, flatten to cash/benchmark, require human review |
| Daily loss limit | −2% of account → stop trading for the day |
| Asset class permissions | Only those explicitly enabled (start: US ETFs/stocks, long-only) |

### 2. Strategy level
| Control | Proposed default |
|---|---|
| Capital per strategy | Fixed allocation; no strategy > 50% of automated capital until proven |
| Strategy drawdown limit | Pre-registered, e.g., 1.5× worst backtest drawdown → auto-disable |
| Volatility target | e.g., 10–12% annualized; scale exposure by forecast vol |
| Turnover cap | Annual turnover ceiling and max trades/day per strategy |

### 3. Position level
| Control | Proposed default |
|---|---|
| Max single position | ≤ 10% of strategy capital (ETFs up to 30% for broad-index funds) |
| Max sector/theme concentration | ≤ 30% |
| Liquidity | Order ≤ 1% of 20-day ADV; min price and min ADV filters |
| Stops | Strategy-defined; gap risk acknowledged (stops are not guarantees) |

### 4. Order level (pre-trade checks)
Max notional per order, price collar (e.g., ±2% from last), symbol allowlist,
duplicate-order detection, buying-power check, session-hours check,
max orders per minute (rate limit / runaway-loop protection).

## Position sizing

- **Volatility scaling:** weight ∝ target_vol / forecast_vol, capped.
- **Kelly criterion:** optimal growth fraction f* = edge/odds (or μ/σ² for
  continuous returns). Estimation error makes full Kelly dangerous; use
  **≤ ½ Kelly, typically ¼**, and only once edge is estimated from live data.
- **Equal risk contribution** across strategies/assets for the portfolio
  layer.
- Never size from backtest Sharpe alone; haircut expected returns by ≥ 50%.

## Kill switches

| Trigger | Action |
|---|---|
| Account drawdown limit hit | Cancel open orders, flatten or move to benchmark, disable strategies, page owner |
| Daily loss limit hit | Cancel orders, no new orders until next session |
| Reconciliation mismatch | Freeze trading until resolved |
| Data feed stale / validation failure | Skip rebalance; no orders on bad data |
| Order rate anomaly (runaway loop) | Hard stop at gateway, page owner |
| Broker/API error rate spike | Pause and retry with backoff; escalate |
| LLM component anomaly (schema failures, cost spike, output distribution shift) | Fall back to non-LLM signal or hold positions |
| Manual | One command / button to flatten and disable everything |

Kill switches must be **tested regularly in paper** (fire drills).

## Tail and operational risks

- **Gap risk:** overnight/weekend gaps blow through stops; size accordingly.
  23×5 sessions change but do not remove this.
- **Correlation spikes:** diversification fails in crises; stress test with
  2008, March 2020, and 2022 correlation regimes.
- **Leverage and shorting:** unlimited-loss profiles; disabled in early phases.
- **Options:** negatively skewed strategies (short puts) need explicit tail
  limits and assignment handling.
- **Crypto:** exchange insolvency/hack risk — keep only trading capital on
  exchange; withdraw-disabled API keys.
- **Model risk:** LLM provider changes model behavior or deprecates a model;
  pin versions and re-validate on change.
- **Key compromise:** see secrets handling in [05](05-brokers-and-execution.md#api-keys-and-access-control)
  and [10](10-operations-and-security.md).

## Risk reporting (daily)

Positions, exposures (gross/net/sector/beta), PnL by strategy, drawdown vs.
limits, realized vs. forecast volatility, turnover, costs and slippage, limit
breaches and near-misses, kill-switch state.
