# 10 — Operations and Security

> **Purpose for agents:** How the system is run day to day, how it's secured,
> and what to do when something breaks. Platform/SRE agent owns this.

## Environments

| Environment | Broker keys | Who can deploy | Purpose |
|---|---|---|---|
| `research` | None (historical data only) | Any agent via PR | Backtests, experiments |
| `paper` | Paper keys | Merge to `main` after CI | Forward testing, fire drills |
| `live` | Live keys (execution service only) | Tagged release + human approval | Real money |

Configuration is per environment; the same container image runs in paper and
live, differing only by injected config and secrets.

## Security checklist

- [ ] Live API keys stored in a secrets manager / encrypted env, injected at
      runtime; never in git, logs, prompts, or LLM context.
- [ ] Broker account: 2FA, IP allowlisting where supported, API key scoped to
      trading only (no withdrawals/transfers), separate keys per service.
- [ ] Crypto exchange keys: trade-only, withdrawal disabled, IP allowlisted.
- [ ] LLM agents never receive live keys; MCP servers exposed to agents use
      paper keys or read-only internal APIs.
- [ ] Prompt-injection awareness: news, filings, and web content fed to LLMs
      are untrusted. LLM outputs pass through schema validation and cannot
      trigger actions beyond producing bounded features.
- [ ] Dependency pinning and vulnerability scanning in CI.
- [ ] Least-privilege VM/cloud IAM; SSH keys only; automatic security updates.
- [ ] Backups of ledger DB and decision logs (daily, off-site, restore tested).
- [ ] Audit log of every config change, limit change, deploy, and manual
      intervention.

## Monitoring and alerting

| Signal | Alert when |
|---|---|
| Heartbeat (dead-man's switch) | Scheduler hasn't completed a cycle on a trading day |
| Data freshness / validation | Stale or failed data |
| Reconciliation | Any position/cash mismatch |
| Risk limits | Breach or within 80% of a limit |
| Orders | Rejections, unusual order rate, unfilled at window end |
| PnL | Daily loss beyond 2σ of expected; drawdown thresholds |
| Slippage | Rolling slippage > modeled cost by a set margin |
| LLM service | Schema failure rate, latency, cost/day over budget, output distribution drift |
| Infra | CPU/memory/disk, API error rates, certificate/token expiry (e.g., Schwab OAuth refresh) |

Alerts go to the owner's phone for critical items; everything else to a daily
digest.

## Incident runbook (template)

1. **Contain:** trigger kill switch if money is at risk (cancel orders, freeze
   strategy or flatten per policy).
2. **Assess:** what happened, which positions/orders are affected, current
   exposure vs. limits.
3. **Reconcile:** broker state is truth; correct internal ledger.
4. **Communicate:** notify owner with facts (not guesses).
5. **Fix:** root cause via PR with regression test; re-run fire drill in paper.
6. **Postmortem:** written, blameless, stored in `docs/incidents/`, with
   action items tracked.

## Routine operations

| Cadence | Task |
|---|---|
| Daily | Pre-market checks, post-close reconciliation, daily report |
| Weekly | Review slippage, limit near-misses, LLM cost, data-quality incidents |
| Monthly | Strategy performance review vs. backtest and benchmark; kill-switch fire drill in paper |
| Quarterly | Re-validate models on new data; review LLM model versions; dependency upgrades |
| Annually | Tax lot reconciliation to 1099s; regulation review; full disaster-recovery test |

## Deployment practices

- Infrastructure as code; one-command rebuild of the trading host.
- CI runs unit tests, data-pipeline tests, and a **backtest regression test**
  (signal outputs for a fixed historical window must match a stored snapshot
  unless the change intends to alter them).
- Deploys to live only outside market hours, with a rollback plan.
- Clock sync (NTP) on all hosts; all timestamps UTC.
