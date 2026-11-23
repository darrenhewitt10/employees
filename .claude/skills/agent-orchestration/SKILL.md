---
name: agent-orchestration
description: "Design how AI agents divide work: roles, separation of duties, tool and MCP scoping, escalation rules, and keeping LLMs out of the live order path. Use when designing agent workflows or agent access."
user-invocable: false
---
# Agent orchestration design

## Principles (docs 08, 11)
- Agents work in the **research and oversight planes**; live orders only from the deterministic pipeline via the risk gateway.
- **Separation of duties:** the builder of a strategy cannot validate it or approve its limits.
- **Least privilege:** each agent gets only the tools it needs; research agents get no broker keys; MCP broker servers use **paper** keys and the narrowest toolset (e.g. `ALPACA_TOOLSETS`).
- **Work through git:** changes are PRs with tests; evidence links to commit + data snapshot + config.
- **Escalate to the owner** for going live, adding capital, loosening limits, new asset classes, broker changes, money-affecting incidents.

## Access matrix
| Activity | Access |
|---|---|
| Research, backtests | Read-only data, research compute, git branches |
| Strategy changes | Pull requests only |
| Monitoring/triage | Read-only state; may trigger tightening (pause, kill switch) |
| Paper trading | Paper keys via adapter/MCP |
| Live trading | None directly |

## Handoff artifacts
PREREG.md -> trials.parquet -> VALIDATION.md -> RISK.md -> config.yaml (see doc 11).
