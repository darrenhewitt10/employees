---
name: infrastructure-ci-cd
description: "Run infrastructure: Docker, infrastructure as code, scheduling on the exchange calendar, CI/CD and research/paper/live environment separation. Use for deployment and platform work."
user-invocable: false
---
# Infrastructure and CI/CD

## Environments (doc 10)
| Env | Keys | Deploy |
|---|---|---|
| research | none | any agent via PR |
| paper | paper keys | merge to main after CI |
| live | live keys (execution service only) | tagged release + **human approval** |
Same container image for paper and live; differs only by injected config and secrets.

## Practices
- Infrastructure as code; one-command rebuild of the trading host (small always-on VM).
- Scheduler runs cycles on the exchange calendar (cron/systemd timers, APScheduler or Prefect).
- CI: lint, type-check, unit/integration tests, backtest regression snapshot.
- Deploy live only outside market hours with a rollback plan; NTP clock sync; UTC everywhere.
- Backups of ledger DB and decision logs daily, off-site; restore tested quarterly.
