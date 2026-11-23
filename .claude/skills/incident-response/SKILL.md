---
name: incident-response
description: "Respond to incidents: contain, assess, reconcile, communicate, fix and write a blameless postmortem. Use when anything goes wrong in paper or live operation."
user-invocable: false
---
# Incident response (doc 10)

1. **Contain:** if money is at risk, trigger the kill switch (cancel orders, freeze strategy or flatten per policy).
2. **Assess:** what happened, affected positions/orders, exposure vs limits.
3. **Reconcile:** broker state is truth; correct the ledger.
4. **Communicate:** notify the owner with facts, not guesses: impact, current state, next update time.
5. **Fix:** root cause via PR with a regression test; re-run the relevant fire drill in paper.
6. **Postmortem:** blameless, in `docs/incidents/YYYY-MM-DD-slug.md`.

## Postmortem template
Summary · timeline (UTC) · impact ($, positions) · root cause · what went well · what went wrong · action items (owner agent, due date) · detection gap (why alerts did or didn't fire).

## Severity
SEV1 money at risk or unreconciled live positions · SEV2 trading halted/degraded · SEV3 paper-only or non-trading issue.
