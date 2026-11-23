---
name: testing-and-fire-drills
description: "Test the system: unit and integration tests, backtest regression snapshots, broker sandbox tests and kill-switch fire drills. Use when adding tests or verifying a release."
user-invocable: false
---
# Testing and fire drills

## Test layers
| Layer | What |
|---|---|
| Unit | Signal math, sizing, limits, cost model, calendar logic |
| Data | Schema, validation rules, corporate-action adjustments on fixtures |
| Integration | Adapter against broker **paper/sandbox**; end-to-end daily cycle in paper |
| Regression | Signal outputs for a fixed historical window must match a stored snapshot unless the PR intends a change |
| Property | Risk gateway never emits an order breaching a limit, for random inputs |

## Fire drills (monthly, in paper)
Trigger each kill switch: drawdown, daily loss, reconciliation mismatch, stale data, order-rate runaway, broker outage, manual flatten. Pass = correct action within the expected time, alert received, state recoverable. Record results in `docs/incidents/drills/`.

## Release checklist
CI green · regression snapshot reviewed · paper run clean for N days · rollback plan · deploy outside market hours.
