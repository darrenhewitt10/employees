# AI Trading System — Research Docs

Research compiled **November 2026** as context for the expert agent team that
will design, build, and operate a personal AI-assisted trading system.

> **Not financial, legal, or tax advice.** Facts about vendors, prices, and
> regulations change; each doc links sources — re-verify before acting.

## Executive summary

1. **Expectations:** Most active retail traders lose money, and public tests of
   frontier LLMs trading autonomously (Alpha Arena 2025–26, StockBench) were
   mostly unprofitable or only marginally better than buy-and-hold, with
   overtrading as the main failure. The realistic target is a disciplined,
   low-turnover, well-risk-managed system that beats or matches a passive
   benchmark after costs and taxes.
2. **Where AI helps:** LLMs add value reading text (news, filings) as *features*,
   and as an agent team doing research, coding, validation, monitoring and
   reporting. Gradient-boosted trees remain the workhorse for tabular signals.
   LLM backtests are vulnerable to look-ahead bias from memorization: only
   post-training-cutoff results count.
3. **Architecture:** deterministic data → signal → portfolio → order pipeline;
   an **independent risk gateway** in front of the broker; **no LLM has live
   order authority**; same code path for backtest, paper, and live.
4. **Stack:** Python, Polars, Parquet/DuckDB, Postgres ledger, LightGBM,
   vectorbt/custom engine for research, NautilusTrader (or LEAN) for live;
   **Alpaca** to start (free paper trading, official MCP server), IBKR later.
5. **Validation:** pre-registration, trial logging, purged walk-forward CV,
   Deflated Sharpe Ratio, Probability of Backtest Overfitting, untouched
   holdout, then ≥ 3 months paper before small live capital.
6. **Recent rule changes:** the $25k pattern-day-trader rule was replaced by
   intraday margin (SEC approval April 15, 2026; broker phase-in varies);
   Nasdaq/NYSE Arca target 23×5 trading from Dec 6, 2026; crypto wash-sale
   rule proposed but not enacted.

## Index

| # | Document | Topic | Owner agent |
|---|---|---|---|
| 01 | [Reality Check](01-reality-check.md) | Evidence on retail and AI trading outcomes; success criteria | Orchestrator |
| 02 | [Strategy Landscape](02-strategy-landscape.md) | Strategy families feasible at retail scale; recommended starting ideas | Quant Researcher |
| 03 | [AI / ML Approaches](03-ai-ml-approaches.md) | ML, RL, LLM techniques; look-ahead bias; open-source projects | ML / LLM Researcher |
| 04 | [Market Data](04-market-data.md) | Vendors, costs, data-quality rules, storage | Data Engineer |
| 05 | [Brokers & Execution](05-brokers-and-execution.md) | Broker API comparison, PDT change, execution and cost model, key handling | Execution Engineer |
| 06 | [Backtesting & Validation](06-backtesting-and-validation.md) | Biases, validation protocol, DSR/PBO, frameworks, promotion gates | Validation (Red Team) |
| 07 | [Risk Management](07-risk-management.md) | Limits, sizing, kill switches, risk reporting | Risk Manager |
| 08 | [System Architecture](08-system-architecture.md) | Components, diagram, tech stack, daily cycle, agent access | Orchestrator / Execution / SRE |
| 09 | [Regulation & Tax](09-regulation-and-tax.md) | US rules for personal algo trading; tax effects on design | Compliance & Tax |
| 10 | [Operations & Security](10-operations-and-security.md) | Environments, security checklist, monitoring, incident runbook | Platform / SRE |
| 11 | [Agent Team & Roadmap](11-agent-team-and-roadmap.md) | Agent roster, interaction rules, phased roadmap, first sprint | Orchestrator |
| 12 | [Decisions Needed](12-decisions-needed.md) | Open questions for the owner, with safe defaults | Orchestrator |
| — | [Expert Roster](expert-roster.md) | 32 advisory experts (one-line job descriptions) and 43 shared skills, with which agents use each | Engagement Lead |
| — | [How to Talk to Your Experts](how-to-talk-to-your-experts.md) | Example prompts: ask one expert, ask the whole team, and multi-expert questions for the orchestrator | Technical Writer |

## The expert team

The roster is built as 34 Claude Code subagents (`.claude/agents/`) with 47 shared skills (`.claude/skills/`). `CLAUDE.md` at the repo root explains how to use them: `/ask-team <question>` for a combined answer from the right experts, or name an individual expert.

## How agents should use these docs

- **Every agent** reads 01, 08, 11, and 12 first, then its owned docs.
- Treat the defaults in 12 as hard limits until the owner changes them.
- When a doc is wrong or stale, fix it via pull request and cite the source.
- Prices, fees, and regulatory dates are point-in-time (Nov 2026); re-verify
  against official pages before relying on them.
