---
name: vendor-management
description: "Evaluate and manage vendors (brokers, data, LLM providers, hosting): scorecards, SLAs, rate limits, costs and exit plans. Use when selecting, comparing or reviewing vendors."
user-invocable: false
---
# Vendor management

## Scorecard (1-5 each, weighted)
Fit for need · data/service quality · reliability/SLA · API quality and limits · cost (monthly + overages) · license terms · security posture · support · lock-in/exit ease · longevity.

## Current shortlist (verify pricing)
- Broker: Alpaca (start), IBKR (later), Schwab, Tradier; crypto: Coinbase Advanced, Kraken.
- Data: Alpaca (free IEX / ~$99 SIP), Massive (ex-Polygon), Databento, Norgate/Sharadar/Tiingo, EDGAR, FRED.
- LLM: Anthropic Claude (agents/features); optional local model for bulk scoring.
- Hosting: small VM; Netlify for the docs site only.

## Rules
- Every vendor has an **exit plan** (alternative + migration effort).
- Track rate limits and usage; alert before overages.
- Re-verify pricing quarterly; record date and source.
- Route license questions to contracts-licensing-counsel.
