---
name: observability-alerting
description: "Monitor the system with metrics, logs, heartbeats and alert routing so failures are noticed fast. Use when adding monitoring or deciding what should alert."
user-invocable: false
---
# Observability and alerting

## Alert on (doc 10)
| Signal | When |
|---|---|
| Heartbeat (dead-man's switch) | No completed cycle on a trading day |
| Data | Stale or failed validation |
| Reconciliation | Any position/cash mismatch |
| Risk | Breach, or within 80% of a limit |
| Orders | Rejections, unusual rate, unfilled at window end |
| P&L | Daily loss beyond 2 sigma; drawdown thresholds |
| Slippage | Rolling realized > modeled by margin |
| LLM | Schema failure rate, latency, cost over budget, output drift |
| Infra | CPU/mem/disk, API errors, token/cert expiry (Schwab OAuth) |

## Routing
Critical (money at risk, kill switch fired, reconciliation mismatch) -> owner's phone immediately. Everything else -> daily digest.

## Practice
Structured logs with run/rebalance IDs; metrics with Prometheus/Grafana or hosted equivalent; every alert links to a runbook step.
