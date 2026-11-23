---
name: market-data-apis
description: "Use market and alternative data APIs correctly: Alpaca, Massive (Polygon), Databento, IBKR, SEC EDGAR, FRED, crypto exchanges; rate limits, feeds and licensing. Use when choosing or integrating data sources."
user-invocable: false
---
# Market data APIs (as of Nov 2026; re-verify prices)

| Source | Use | Notes |
|---|---|---|
| Alpaca Market Data | Prototype bars, live data | Free = IEX feed only (~2.5% of volume), no latest 15 min historical; Algo Trader Plus (~$99/mo) = full SIP |
| Massive (formerly Polygon.io) | Stocks/options/crypto bars, flat files | Renamed Oct 30 2025; `api.massive.com` live, `api.polygon.io` still supported; Starter reportedly ~$29/mo (verify) |
| Databento | Exchange-direct depth, futures | Usage-based historical; live equities need subscription; US equities from 2018 |
| Norgate / Sharadar / Tiingo | Survivorship-free EOD | Needed for stock-level research |
| SEC EDGAR | Filings, XBRL, Form 4, 13F | Free; declare a User-Agent; respect fair-access rate limits |
| FRED | Macro series | Free API key |
| Coinbase Advanced / Kraken | Crypto market data | Free REST/WebSocket |
| yfinance | Exploration only | Unofficial; never for validation or production |

## Integration rules
- Wrap each vendor in an adapter with retries, backoff and rate-limit handling; log request counts.
- Save raw responses immutably before transforming.
- Reconcile daily closes between broker feed and research vendor; alert on divergence.
- Respect licenses: no redistribution, no committing vendor data, check display vs non-display terms.
- Record vendor, dataset, and download date in every dataset's metadata.
