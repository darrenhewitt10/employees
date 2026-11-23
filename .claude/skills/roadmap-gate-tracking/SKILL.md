---
name: roadmap-gate-tracking
description: "Track work against the phased roadmap and promotion gates (docs 06 and 11): phase status, gate evidence, blockers. Use for status reports and go/no-go checks."
user-invocable: false
---
# Roadmap and gate tracking

## Phases (doc 11)
| Phase | Exit criteria |
|---|---|
| 0 Decisions | Doc 12 answered: capital, assets, limits, broker, account type |
| 1 Foundations | Reproducible backtest of buy-and-hold benchmark matches reference |
| 2 Baseline strategies | >=1 strategy passes Backtest->Paper gate, or documented that none beats benchmark |
| 3 Trading plane (paper) | 20 consecutive clean paper days; kill-switch fire drill passes |
| 4 AI signals | LLM/ML feature adds credible value in walk-forward + paper |
| 5 Paper track record | >=3 months; Paper->Live gate |
| 6 Small live | >=6 months live within limits; owner approval to scale |
| 7 Scale & extend | Each new sleeve repeats phases 2-6 |

## Promotion gates (doc 06)
| Stage | Gate |
|---|---|
| Idea -> Backtest | Pre-registration committed; rationale reviewed |
| Backtest -> Paper | DSR >= 0.95, PBO <= 0.2, beats benchmark net of costs, robustness passes, risk sign-off |
| Paper -> Live | >=3 months paper; live-vs-backtest within tolerance; zero incidents; owner approval |
| Small -> Scaled | >=6 months live within limits; realized slippage <= modeled; owner approval |

## Status report format
- **Phase:** current phase and % of exit criteria met
- **Gate evidence:** each criterion -> met / not met / unknown, with link to artifact
- **Blockers:** item, owner agent, needed decision
- **Next 2 weeks:** top 3 tasks with owners

A gate is **met only with evidence** (commit hash, report path, metric). Opinion is not evidence.
