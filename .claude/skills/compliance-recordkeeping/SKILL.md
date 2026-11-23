---
name: compliance-recordkeeping
description: "Operate compliance controls: pre-trade conduct checks, restricted lists, 7-year record retention, audit trails and annual rule reviews. Use when building or checking compliance controls."
user-invocable: false
---
# Compliance and recordkeeping (doc 09)

## Pre-trade checks (in the risk gateway)
- Block self-crossing orders (no wash trades with yourself, including across accounts).
- Order-to-fill ratio and cancel-rate limits (anti-spoofing hygiene).
- **Restricted list** (e.g. owner's employer, lock-up holdings) - must be confirmed before live.
- Symbol allowlist per enabled asset class.

## Records (>= 7 years)
Every order, fill, cancel, decision record, config/limit change, deploy, manual intervention, and LLM input/output (via cache keys). Immutable, backed up, retrievable by date and strategy.

## Annual review
Compliance officer summarizes changes in FINRA/SEC/CFTC/IRS/state rules and broker terms, and updates docs/09.

## Fraud hygiene
Never integrate third-party bots or signal sellers promising returns.
