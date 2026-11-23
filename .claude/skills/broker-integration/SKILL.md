---
name: broker-integration
description: "Integrate broker and exchange APIs safely: Alpaca, IBKR, Schwab, Coinbase/Kraken; adapter pattern, idempotent orders, paper/live separation, reconciliation. Use when writing or reviewing broker code."
user-invocable: false
---
# Broker integration

## Adapter interface (strategies never call SDKs directly)
`get_account()`, `get_positions()`, `get_open_orders()`, `submit(order)`, `cancel(id)`, `stream_fills()`, `get_bars()`; all return internal types.

## Broker notes (verify current terms)
- **Alpaca:** start here. Free paper account; `alpaca-py` SDK; official MCP server (defaults to paper; restrict with `ALPACA_TOOLSETS`). Fractional shares.
- **IBKR:** broadest markets/order types; TWS API needs TWS/IB Gateway running; Web API trading needs a funded IBKR Pro account.
- **Schwab Trader API:** OAuth2, app approval required, frequent token refresh - monitor expiry.
- **Coinbase Advanced / Kraken:** trade-only keys, withdrawals disabled, IP allowlist.

## Rules
- Separate **paper** and **live** keys and deployments; live keys exist only in the execution service, never in prompts, logs, git or agent tools.
- Idempotent `client_order_id`; retries with exponential backoff; handle partial fills and rejects.
- Broker is the source of truth: reconcile positions and cash at start and end of day.
- PDT rule replaced by intraday margin (SEC approved Apr 15 2026; broker phase-in varies) - our own turnover limits replace that guardrail.
