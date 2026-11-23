# 08 — System Architecture

> **Purpose for agents:** The reference architecture the team will build. It
> separates deterministic trading machinery from AI components so that no
> LLM can move money without passing hard-coded risk checks.

## Design principles

1. **Deterministic core, AI at the edges.** Data → signals → target portfolio
   → orders is reproducible code. LLMs generate *features* and *assist humans
   and agents*; they do not place orders directly.
2. **One code path** for backtest, paper, and live signal generation.
3. **Independent risk gateway** between any order source and the broker.
4. **Everything is logged and replayable** (event-sourced decisions).
5. **Fail safe:** on any doubt (bad data, errors, mismatch), do nothing and alert.
6. **Broker-agnostic adapters** so brokers can be swapped/added.

## Component diagram

```
                  ┌──────────────────────── Research plane ───────────────────────┐
                  │  Agent team (LLM)  ──►  Notebooks / experiments ──► Trial log │
                  │       │                      │                                 │
                  │       ▼                      ▼                                 │
                  │  Strategy code (git, PR-reviewed)   Validation reports (06)    │
                  └───────────────┬───────────────────────────────────────────────┘
                                  │ promoted via gates (human approval)
┌──────────── Data plane ─────────┼──────────────── Trading plane ──────────────────┐
│ Vendors/APIs ─► Ingest ─► Validate ─► Clean store (Parquet/DuckDB)                │
│ News/filings ─► LLM feature service (cached, schema-validated) ─┐                 │
│                                                                  ▼                │
│                     Signal engine ─► Portfolio constructor ─► Target weights       │
│                                                                  │                │
│                                         Order planner (diff vs. current positions)│
│                                                                  │                │
│                                   ┌──────── RISK GATEWAY ────────┴───────┐        │
│                                   │ limits, collars, kill switches, rate  │        │
│                                   └──────────────┬────────────────────────┘        │
│                                                  ▼                                 │
│                                       Broker adapter (Alpaca / IBKR)               │
│                                                  │                                 │
│                       Fills/positions ◄──────────┘ ─► Reconciler ─► Ledger (DB)    │
└────────────────────────────────────────────────────────────────────────────────────┘
          │                                                     │
          ▼                                                     ▼
   Monitoring & alerts (metrics, logs, pager)         Reporting (daily tear sheet,
                                                       LLM-written summary for owner)
```

## Components

| Component | Responsibility | Notes |
|---|---|---|
| **Ingest** | Pull bars, corporate actions, fundamentals, news, filings on schedule | Idempotent jobs; raw data immutable |
| **Validate** | Data-quality checks ([04](04-market-data.md#data-quality-rules-non-negotiable)) | Blocks downstream on failure |
| **LLM feature service** | Score text into bounded, typed features | Prompt versions in git; response cache; token budget; fallbacks |
| **Signal engine** | Compute signals from clean data + features | Pure functions, same code in backtest/live |
| **Portfolio constructor** | Signals → target weights with constraints | Vol targeting, caps, turnover penalty |
| **Order planner** | Target vs. current → orders | Minimum trade size threshold to avoid churn |
| **Risk gateway** | Pre-trade checks, kill switches | Separate process/service; own config; strategies can't import it to bypass |
| **Broker adapter** | Submit/cancel/replace; stream fills | Deterministic client order IDs; retries with backoff |
| **Reconciler / ledger** | Positions, cash, PnL, tax lots | Broker is source of truth; mismatch → freeze |
| **Scheduler** | Run daily/intraday cycles on the exchange calendar | e.g., cron/systemd timers, Prefect, or a simple APScheduler service |
| **Monitoring** | Metrics, logs, alerts, heartbeat | Dead-man's switch: alert if no heartbeat |
| **Reporting** | Daily/weekly reports | LLM-generated narrative *from* computed numbers, never inventing numbers |

## Suggested tech stack

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.12+ | Ecosystem; NautilusTrader/vectorbt/LightGBM |
| Dataframes | Polars (+ pandas where libraries require) | Speed, lazy queries |
| Storage | Parquet + DuckDB; Postgres for ledger/orders | Zero-ops analytics; ACID for money records |
| Backtest/live engine | Custom daily engine → NautilusTrader for live | See [06](06-backtesting-and-validation.md#frameworks) |
| ML | LightGBM, scikit-learn | Robust tabular baselines |
| LLM | Claude via Anthropic API / Claude Agent SDK; optional local model for cheap bulk scoring | Agent team + feature service |
| Agent tooling | MCP servers (Alpaca **paper**, internal read-only data/risk tools) | Gives agents controlled, auditable access |
| Config | Pydantic settings, YAML per environment (research/paper/live) | Validated config |
| Deployment | Docker on a small always-on VM; separate paper and live deployments | Reproducible |
| Observability | Structured logs, Prometheus/Grafana or a hosted equivalent; alerts to phone (Pushover/Telegram/email) | Know when it breaks |
| CI | Tests + backtest regression on every PR | Prevents silent changes in signals |

## Daily cycle (example for a daily-rebalance strategy)

1. **Pre-market (e.g., 08:00 ET):** ingest overnight data, filings and news;
   validate; reconcile positions with broker; check kill-switch state.
2. **Signal run:** compute features (LLM scores from cache or fresh), signals,
   target weights; persist the full decision record.
3. **Order planning:** diff vs. positions; apply minimum trade thresholds.
4. **Risk gateway:** pre-trade checks; reject/clip orders; log decisions.
5. **Execution window (e.g., 10:00–15:30 ET):** limit orders with collars,
   slicing if needed; cancel unfilled at window end.
6. **Post-close:** reconcile fills, update ledger and tax lots, compute PnL,
   slippage, risk metrics; generate the daily report; health checks.

## Where the agent team plugs in

| Agent activity | Allowed access |
|---|---|
| Research, coding, backtests | Read-only data, research compute, git branches |
| Proposing strategy changes | Pull requests only; merges require review + gates |
| Monitoring / incident triage | Read-only trading state, logs, metrics; can trigger *tightening* actions (pause, kill switch) |
| Paper trading | Paper broker keys via adapter/MCP |
| Live trading | **None directly.** Live orders come only from the deterministic pipeline through the risk gateway |

This mirrors the multi-agent "trading firm" pattern from TradingAgents (analyst
→ researcher → trader → risk) but places the LLM agents in the research and
oversight planes rather than in the live order path.
