# 05 — Brokers, APIs, and Execution

> **Purpose for agents:** Which brokers expose APIs suitable for an automated
> personal account, how they compare, and how orders should be executed.
> Execution Engineer agent owns this. Verify fees and terms on official sites.

## Broker comparison (US-focused)

| Broker | API | Assets | Paper trading | Strengths | Weaknesses |
|---|---|---|---|---|---|
| **Alpaca** | REST + WebSocket; official Python SDK (`alpaca-py`); official **MCP server** | US stocks/ETFs, options, crypto | Yes, free, defaults in MCP server | API-first, easiest to start, free paper account, good docs | Free data is IEX-only; fewer order types than IBKR |
| **Interactive Brokers (IBKR)** | Web API (REST/WebSocket), TWS API (socket via TWS/IB Gateway), FIX | Global stocks, options, futures, FX, bonds, crypto | Yes | Broadest markets and order types (incl. VWAP/TWAP algos via TWS API), low margin rates | Gateway process to babysit, steeper learning curve; Web API trading needs funded IBKR Pro account |
| **Charles Schwab Trader API** | OAuth2 REST (successor to TD Ameritrade API) | US stocks, ETFs, options | No native paper via API | Large established broker | Developer app requires approval; token refresh is frequent; fewer features than IBKR |
| **Tradier** | REST + streaming | US stocks, options | Sandbox | Options-friendly, simple API | Smaller ecosystem |
| **Coinbase Advanced** | REST + WebSocket | Crypto | Sandbox (limited) | US-regulated, reliable | Higher fees at low volume (entry tiers reported ~0.4–0.6% taker+) |
| **Kraken (Pro)** | REST, WebSocket v1/v2, FIX, futures API | Crypto | Limited | More order types, lower fees reported for US order-book traders | State availability varies |

Sources: [Alpaca MCP server](https://github.com/alpacahq/alpaca-mcp-server),
[Alpaca MCP docs](https://docs.alpaca.markets/docs/alpaca-mcp-server),
[IBKR API](https://www.interactivebrokers.com/en/trading/ib-api.php),
[IBKR Web API for individuals](https://www.interactivebrokers.com/docs/web-api/trading/getting-started/trading-access-for-individuals),
[Coinbase Advanced API](https://www.coinbase.com/developer-platform/products/advanced-trade-api),
[Coinbase vs Kraken fees (BrokerChooser)](https://brokerchooser.com/news/coinbase-vs-kraken-fee-structures-and-trading-features-compared--bbeea493).

### Recommendation

- **Phase 1–3 (build, backtest, paper):** **Alpaca** — free paper account,
  simplest API, official MCP server so agents can read positions/market data.
- **Later (if expanding to futures, international, or advanced orders):** add
  **IBKR** behind the same internal broker-adapter interface.
- Keep a **broker-agnostic adapter layer** so strategies never call a broker
  SDK directly.

## Important rule changes

- **Pattern Day Trader (PDT) rule replaced.** The SEC approved FINRA Rule 4210
  amendments on **April 15, 2026**, eliminating the PDT designation, the
  4‑trades‑in‑5‑days test, and the **$25,000 minimum equity**, replacing them
  with risk-based **intraday margin** requirements. Brokers may phase in
  implementation (reports cite an adoption window running to Oct 2027), so
  check each broker's current status.
  ([FINRA Regulatory Notice 26‑10](https://www.finra.org/rules-guidance/notices/26-10),
  [Schwab explainer](https://www.schwab.com/learn/story/sec-approves-scrapping-25000-day-trader-minimum))
  *Implication:* small accounts can day trade more freely — which also removes
  a guardrail. Our own turnover limits must replace it.
- **T+1 settlement** for US equities since May 2024: cash accounts must still
  avoid good-faith/free-riding violations when recycling unsettled proceeds.
- **23×5 trading** on Nasdaq/NYSE Arca targeted for Dec 6, 2026 (see
  [02-strategy-landscape.md](02-strategy-landscape.md#session-hours-note)).

## Execution principles

1. **Order types:** default to **limit** orders (marketable limits with a
   price collar) rather than raw market orders. Never send market orders in
   pre/post/overnight sessions.
2. **Idempotency:** every order carries a deterministic `client_order_id`
   derived from (strategy, rebalance id, symbol). Retries must not duplicate.
3. **Pre-trade checks** (in the risk gateway, independent of strategy code):
   max order notional, max position %, max daily turnover, price collar vs.
   last trade, symbol allowlist, buying power, market-hours check.
4. **Slicing:** orders > a small % of average daily volume are split over time.
5. **Timing:** avoid the first and last few minutes of the session unless the
   strategy specifically targets open/close auctions (use MOO/MOC orders then).
6. **Post-trade:** reconcile fills against intended orders; log slippage
   (fill vs. decision price and vs. arrival price) for every fill.
7. **Reconciliation:** at start and end of day, broker positions/cash are the
   source of truth; internal state is corrected (and alerts raised) on mismatch.
8. **Fractional shares** (Alpaca supports them) reduce rounding error for
   small accounts but check per-broker order-type limits on fractional orders.

## Transaction cost model (for backtests)

Per trade cost = commission + half-spread + market impact + fees.
- Commission: often $0 for US stocks/ETFs, but include regulatory fees (SEC
  Section 31, FINRA TAF) on sells and per-contract options fees.
- Half-spread: use historical quote data or a conservative bps assumption by
  liquidity bucket (e.g., 1–2 bps mega-cap ETFs, 5–20+ bps small caps).
- Impact: square-root model `k · σ · sqrt(order_size / ADV)`; negligible at
  very small size but must exist in the model.
- Crypto: taker fees at the actual account tier (often 0.4%+ at low volume).

Live slippage must be tracked and fed back into the backtest cost model.

## API keys and access control

- Separate **paper** and **live** keys; live keys are held only by the
  execution service, never given to research agents or LLM tool contexts.
- If an agent uses the Alpaca MCP server, configure it with **paper keys** and
  the narrowest toolset (`ALPACA_TOOLSETS`). Alpaca itself warns that
  unintended AI-generated orders can cause real losses.
- Store secrets in a secrets manager or environment injected at runtime —
  never in git.
- Enable broker-side protections where offered (IP allowlists, 2FA, trading
  permissions limited to needed asset classes, no withdrawals via API).
