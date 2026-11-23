---
name: crypto-exchange-ops
description: "Operate a crypto trading sleeve: exchange selection, trade-only keys, custody and counterparty risk, fees, 24/7 monitoring and crypto tax status. Use for any crypto question."
user-invocable: false
---
# Crypto exchange operations

## Rules
- Treat crypto as a **separate sleeve** with its own capital cap and limits (default: disabled until owner enables).
- Keep only trading capital on exchange; API keys **trade-only, withdrawal disabled, IP allowlisted**.
- Fees dominate at low volume (entry taker tiers often 0.4-0.9%): model the actual tier; favor low turnover.
- 24/7 markets: monitoring and kill switches must run continuously; weekend gaps and outages happen.
- Stablecoins carry issuer/depeg risk.

## Exchanges (US, verify)
Coinbase Advanced (REST/WebSocket, volume-tiered fees), Kraken Pro (REST, WebSocket v1/v2, FIX, futures; more order types). State availability varies.

## Tax (doc 09)
Each disposal is taxable. Wash-sale rule does **not** currently apply to crypto (bills proposed in 2026, not enacted - re-check). Brokers issue Form 1099-DA; track lots per exchange yourself.
