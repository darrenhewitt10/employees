---
name: reconciliation-ledger
description: "Reconcile positions and cash with the broker and maintain the order/fill ledger and tax lots. Use for daily reconciliation, ledger design or any mismatch."
user-invocable: false
---
# Reconciliation and ledger

## Daily procedure
1. **Pre-market:** pull broker positions, cash, open orders; compare to internal ledger.
2. **Post-close:** ingest fills; update positions, cash, fees; compare again.
3. Any mismatch -> **freeze trading**, alert, correct internal state to broker truth, record cause.

## Ledger (Postgres)
Tables: `orders` (client_order_id, strategy, rebalance_id, symbol, side, qty, limit, status, timestamps), `fills` (fill_id, order_id, qty, price, fees, venue, ts), `positions_snapshot`, `cash_ledger`, `tax_lots` (lot_id, symbol, acquired, qty, cost basis, wash-sale adjustments), `decision_records` (inputs, signals, weights, LLM cache keys).

## Rules
- The broker is the source of truth; internal state is corrected, never the reverse.
- Records kept >= 7 years (audit, tax).
- Year-end realized gains reconcile to broker 1099-B / 1099-DA.
