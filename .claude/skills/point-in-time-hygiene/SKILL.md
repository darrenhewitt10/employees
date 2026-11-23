---
name: point-in-time-hygiene
description: "Prevent look-ahead and survivorship bias: point-in-time data, corporate actions, timestamps and exchange calendars. Use whenever data feeds a backtest, model or live signal."
user-invocable: false
---
# Point-in-time hygiene

## Rules
1. A feature at decision time *t* may use only data **published** before *t* (fundamentals by filing/release date, news by publication timestamp, restated data by its original vintage).
2. Decisions at bar *t* execute at *t+1* open or later, never at the same bar's close.
3. Universes include **delisted** securities (survivorship-free); index membership as of each date.
4. Store raw prices plus adjustment factors; derive adjusted series deterministically; cross-check splits/dividends with a second source.
5. Timestamps in UTC; sessions, holidays and half-days from an exchange calendar (update for 23x5 sessions from Dec 2026).
6. Labels (forward returns) must not overlap the training window without purging/embargo.
7. LLM-derived features: see `llm-lookahead-audit`.

## Review checklist
- [ ] Every join is an as-of join on availability time, not on period end.
- [ ] No `shift(-n)` or future window leaks into features.
- [ ] Universe file is dated and includes dead tickers.
- [ ] Corporate-action adjustments applied once, verified.
- [ ] One-bar execution delay in the simulator.
- [ ] Validation checks ran: missing bars, zero/negative prices, unexplained jumps, duplicates, stale quotes.
