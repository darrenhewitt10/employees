# 04 — Market Data

> **Purpose for agents:** Where to get data, what it costs, and the data-quality
> rules that keep backtests honest. Data Engineer agent owns this.
> Prices quoted are from public sources as of late 2026 and must be
> re-verified on the vendor's pricing page before purchase.

## Data needs by phase

| Phase | Needed | Good-enough source |
|---|---|---|
| Prototype (ETF trend/vol strategies) | Daily OHLCV, adjusted for splits/dividends | Broker API (Alpaca free tier), Tiingo, or Massive (Polygon) Starter |
| Stock-level research | Survivorship-bias-free daily bars incl. delisted names, corporate actions, point-in-time fundamentals | Paid vendor (Massive/Polygon, Databento, Norgate, Sharadar via Nasdaq Data Link) |
| Intraday strategies | Minute bars or trades/quotes; consolidated (SIP) feed | Massive, Databento, Alpaca Algo Trader Plus |
| Text/NLP signals | Timestamped news headlines, SEC filings, transcripts | Broker news APIs (Alpaca/Benzinga), SEC EDGAR (free), vendor news feeds |
| Macro | Rates, inflation, spreads | FRED (free) |

## Vendors

| Vendor | Notes |
|---|---|
| **Alpaca Market Data** | Free plan: IEX exchange feed only (~2.5% of US volume) for real-time; historical available but not the most recent 15 minutes. **Algo Trader Plus** (~$99/mo) adds full SIP (100% of volume). ([Alpaca docs](https://docs.alpaca.markets/docs/about-market-data-api)) |
| **Massive (formerly Polygon.io)** | Rebranded Oct 30, 2025; `api.massive.com` live, `api.polygon.io` still supported. Stocks Starter reportedly ~$29/mo (third-party figure, verify). Stocks, options, indices, FX, crypto; flat-file bulk downloads. ([announcement](https://www.einpresswire.com/article/863823068/polygon-io-is-now-massive), [pricing](https://massive.com/pricing)) |
| **Databento** | Exchange-direct feeds (full depth, not just SIP top of book); usage-based historical pricing, subscription required for live equities since Jan 2025; US equities history from 2018. Strong for futures. ([equities](https://databento.com/equities), [pricing change](https://databento.com/blog/upcoming-changes-to-pricing-plans-in-january-2025)) |
| **Interactive Brokers** | Market data subscriptions via brokerage account; good for live data if IBKR is the broker. |
| **Tiingo / Norgate / Sharadar** | Affordable end-of-day data; Norgate and Sharadar include delisted securities (survivorship-free). |
| **SEC EDGAR** | Free filings (10‑K, 10‑Q, 8‑K, Form 4 insider trades, 13F) with full-text search and XBRL financial data APIs. Respect SEC fair-access rate limits and declare a User-Agent. |
| **FRED** | Free macroeconomic time series via API. |
| **yfinance / scraped sources** | Fine for quick exploration; **not** for production or final validation (unofficial, unstable, no delisted data, ToS risk). |
| **Crypto exchanges** | Coinbase Advanced and Kraken provide free REST/WebSocket market data. |

## Data-quality rules (non-negotiable)

1. **Point-in-time correctness.** Every feature must use only data that was
   available at the decision timestamp. Fundamentals use the *filing/release*
   date, not the fiscal period end. News uses the *publication* timestamp.
2. **Survivorship bias.** Stock universes must include delisted securities.
   Backtesting today's S&P 500 constituents over 20 years inflates returns.
3. **Corporate actions.** Store raw prices and adjustment factors separately;
   compute adjusted series deterministically. Verify splits/dividends against
   a second source.
4. **Timezones and calendars.** Store timestamps in UTC; use an exchange
   calendar library (e.g., `exchange_calendars` / `pandas_market_calendars`)
   for sessions, holidays, half-days — and update for the new 23×5 sessions.
5. **Reproducibility.** Raw downloads are immutable and versioned (date-stamped
   Parquet snapshots); derived datasets are rebuilt by code.
6. **Validation checks** on every ingest: missing bars, zero/negative prices,
   >X% single-bar jumps without a corporate action, duplicate timestamps,
   stale quotes. Failures block downstream jobs and alert.
7. **Cross-vendor reconciliation** for anything feeding live trading: compare
   daily closes between broker feed and research vendor; alert on divergence.

## Storage recommendation

- **Format:** Parquet, partitioned by dataset/symbol/date.
- **Query engine:** DuckDB (local, zero-ops) or Polars for research;
  Postgres/TimescaleDB only if multi-process concurrent writes are needed.
- **Layout:**
  ```
  data/
    raw/<vendor>/<dataset>/<yyyy-mm-dd>/...   # immutable
    clean/<dataset>/...                        # validated, adjusted
    features/<feature_set_version>/...         # model inputs
    llm_cache/<model>/<prompt_version>/...     # cached LLM outputs
  ```
- Data should live outside the git repo (object storage or local disk) with
  only schemas and pipeline code committed.

## Licensing

Most vendor data licenses prohibit redistribution. Agents must not commit raw
vendor data to public repos or share it outside the system.
