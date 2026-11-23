# Expert Roster — Advisory Bench for the AI Trading Project

> **Purpose:** The full set of experts a consultant on this project should
> have advising them, ready to turn into agents. Each role has a one-line job
> description; the skills section defines reusable skills and shows which
> agents share each one. Built from the research in this folder (docs 01–12).

**32 expert agents · 43 skills · 7 domains**

## How this relates to the core build team

[Doc 11](11-agent-team-and-roadmap.md) defines a 10-agent **core build team**.
This roster is the wider **advisory bench** around that team. Every core role
appears here (mapping below), plus experts the build team will consult as
needed: finance, legal, governance, communications and owner-facing roles.

| Doc 11 core role | Roster ID |
|---|---|
| Orchestrator / Portfolio Manager | E01 + E04 |
| Data Engineer | E15 |
| Quant Researcher | E07 |
| ML / LLM Researcher | E13 + E14 |
| Validation (Red Team) | E12 |
| Risk Manager | E22 |
| Execution Engineer | E09 + E16 |
| Platform / SRE | E18 |
| Compliance & Tax | E28 + E25 |
| Performance Analyst / Reporter | E26 |

**Ground rules that apply to every agent** (from docs 07, 08 and 11):
- No agent has live order authority. Live orders come only from the
  deterministic pipeline through the risk gateway.
- **E12 Validation** and **E22 Risk** hold vetoes and stay independent of
  the agents that build strategies.
- Going live, adding capital, loosening limits or adding asset classes needs
  the human owner's approval.
- Legal and tax agents give research, not professional advice. Material
  decisions go to a licensed professional.

## Part 1 — Expert roster


### Leadership & Business

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E01 | **Engagement Lead (Orchestrator)** | Coordinates every expert, resolves conflicting advice, and turns it into clear recommendations and decisions for the consultant and the account owner. | 01, 11, 12 | `project-context`, `source-verification`, `decision-memo`, `roadmap-gate-tracking`, `agent-orchestration`, `technical-writing` |
| E02 | **Program Manager** | Owns the roadmap, backlog, sprint plans, dependencies and phase-gate status so the build moves forward on schedule. | 11 | `project-context`, `decision-memo`, `roadmap-gate-tracking`, `requirements-spec`, `technical-writing` |
| E03 | **Business Analyst** | Turns the owner's answers in doc 12 into written, testable requirements and acceptance criteria for every build team. | 12 | `project-context`, `source-verification`, `roadmap-gate-tracking`, `requirements-spec`, `technical-writing` |
| E04 | **Investment Strategist / Portfolio Manager** | Sets the investment objective, benchmark and asset allocation, and decides how individual strategies combine into one portfolio. | 01, 02 | `project-context`, `source-verification`, `decision-memo`, `strategy-design`, `portfolio-construction`, `macro-regime-stress-testing` |
| E05 | **Personal Financial Planner** | Decides how much capital the owner can safely put at risk, which account types to use, and how the system fits their wider finances. | 07, 09, 12 | `project-context`, `source-verification`, `decision-memo`, `tax-analysis`, `behavioral-finance`, `personal-financial-planning` |
| E06 | **Behavioral Finance Coach** | Protects the owner from emotional overrides (panic-selling, chasing losses, loosening limits) and designs approval steps that resist bias. | 01, 07 | `project-context`, `decision-memo`, `behavioral-finance`, `compliant-communications` |

### Trading & Quantitative Domain

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E07 | **Quantitative Researcher** | Designs, pre-registers and backtests rules-based and factor strategies (trend, momentum, volatility targeting) against the benchmark. | 02, 06 | `project-context`, `source-verification`, `python-data-stack`, `point-in-time-hygiene`, `backtesting`, `statistical-validation`, `strategy-design`, `portfolio-construction` |
| E08 | **Macro & Market Strategist** | Supplies market-regime context (rates, inflation, volatility, correlations) and designs the historical stress scenarios every strategy must survive. | 02, 07 | `project-context`, `source-verification`, `decision-memo`, `macro-regime-stress-testing` |
| E09 | **Execution & Market Microstructure Specialist** | Designs order types, timing, slicing and the transaction-cost model, and analyzes live slippage against the model. | 05 | `project-context`, `source-verification`, `backtesting`, `execution-cost-modeling`, `broker-integration` |
| E10 | **Derivatives Specialist (Options & Futures)** | Advises on any options or futures sleeve: Greeks, margin, assignment, contract rolls and Section 1256 treatment. | 02, 07, 09 | `project-context`, `source-verification`, `strategy-design`, `risk-limits-kill-switches`, `derivatives-analytics`, `tax-analysis` |
| E11 | **Digital Asset Specialist** | Advises on any crypto sleeve: exchange selection, counterparty and custody risk, fees, 24/7 operations and crypto tax rules. | 02, 05, 09 | `project-context`, `source-verification`, `broker-integration`, `crypto-exchange-ops`, `tax-analysis` |
| E12 | **Validation Statistician (Red Team)** | Independently attacks every backtest for bias and overfitting and enforces the DSR/PBO promotion gates; holds a veto. | 06 | `project-context`, `point-in-time-hygiene`, `backtesting`, `statistical-validation`, `llm-lookahead-audit`, `testing-and-fire-drills` |

### AI & Technology

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E13 | **ML Engineer / Data Scientist** | Builds features, labels and gradient-boosted models with purged walk-forward validation, and monitors model drift. | 03, 06 | `project-context`, `python-data-stack`, `point-in-time-hygiene`, `statistical-validation`, `ml-modeling`, `software-engineering` |
| E14 | **LLM & AI Agent Architect** | Designs the LLM text-feature service, prompts, caching, guardrails and the agent team's tool access, so no LLM can place live orders. | 03, 08, 11 | `project-context`, `source-verification`, `llm-feature-engineering`, `llm-lookahead-audit`, `agent-orchestration`, `software-engineering`, `security-and-secrets` |
| E15 | **Data Engineer** | Builds the ingest, validation and point-in-time storage pipelines for prices, corporate actions, fundamentals, news and filings. | 04 | `project-context`, `python-data-stack`, `point-in-time-hygiene`, `market-data-apis`, `software-engineering`, `observability-alerting` |
| E16 | **Trading Systems Architect / Backend Engineer** | Builds the signal engine, portfolio constructor, order planner, independent risk gateway and broker adapters, with one code path for backtest and live. | 05, 08 | `project-context`, `portfolio-construction`, `risk-limits-kill-switches`, `execution-cost-modeling`, `broker-integration`, `software-engineering`, `reconciliation-ledger` |
| E17 | **QA & Test Engineer** | Owns unit, integration and backtest-regression tests and the kill-switch fire drills that run before any release. | 06, 10 | `project-context`, `risk-limits-kill-switches`, `software-engineering`, `testing-and-fire-drills` |
| E18 | **Platform / DevOps / SRE Engineer** | Runs hosting, containers, CI/CD, scheduling, monitoring and alerting for the research, paper and live environments. | 08, 10 | `project-context`, `software-engineering`, `infrastructure-ci-cd`, `observability-alerting`, `incident-response` |
| E19 | **Security Engineer** | Threat-models the system, scopes and protects broker and exchange keys, and defends LLM components against prompt injection. | 05, 10 | `project-context`, `source-verification`, `infrastructure-ci-cd`, `security-and-secrets`, `incident-response` |
| E20 | **UX & Dashboard Designer** | Designs the owner-facing dashboards, daily reports and approval screens so risk and performance are understood at a glance. | 07, 08 | `project-context`, `performance-reporting`, `data-visualization`, `technical-writing` |

### Operations

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E21 | **Trading Operations Manager** | Runs the daily trading cycle, broker reconciliation and incident runbooks, and makes sure nothing trades on bad data. | 08, 10 | `project-context`, `broker-integration`, `observability-alerting`, `reconciliation-ledger`, `incident-response`, `compliance-recordkeeping` |
| E22 | **Risk Manager** | Owns limits, position sizing, kill switches and the daily risk report; holds a veto on trades, promotions and any loosening of limits. | 07 | `project-context`, `decision-memo`, `portfolio-construction`, `risk-limits-kill-switches`, `position-sizing`, `performance-reporting`, `macro-regime-stress-testing` |
| E23 | **Vendor & Procurement Manager** | Selects and manages brokers, data vendors, LLM providers and hosting: pricing, SLAs, rate limits and exit plans. | 04, 05 | `project-context`, `source-verification`, `decision-memo`, `market-data-apis`, `contract-license-review`, `vendor-management`, `budgeting-tco` |

### Finance

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E24 | **Finance Controller / Budget Owner** | Tracks spend on data, LLM tokens and hosting against budget and against net trading value, and owns total cost of ownership. | 04, 12 | `project-context`, `decision-memo`, `performance-reporting`, `vendor-management`, `budgeting-tco` |
| E25 | **Tax Advisor** | Models after-tax returns, wash sales, holding periods, Section 1256, §475(f) and crypto rules, and specifies the tax-lot ledger. | 09 | `project-context`, `source-verification`, `decision-memo`, `reconciliation-ledger`, `tax-analysis`, `us-securities-regulation` |
| E26 | **Performance Analyst** | Produces attribution, benchmark comparisons and live-vs-backtest tracking that decide whether strategies stay, scale or stop. | 01, 06 | `project-context`, `statistical-validation`, `performance-reporting`, `tax-analysis`, `data-visualization` |

### Legal, Compliance & Governance

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E27 | **Securities Regulatory Counsel** | Interprets SEC, FINRA, CFTC and state rules (PDT replacement, manipulation, adviser/CTA registration triggers) for the project. | 09 | `project-context`, `source-verification`, `decision-memo`, `us-securities-regulation` |
| E28 | **Compliance Officer** | Puts pre-trade conduct checks, restricted lists, record retention and the annual rule review into day-to-day operation. | 09, 10 | `project-context`, `reconciliation-ledger`, `incident-response`, `us-securities-regulation`, `compliance-recordkeeping` |
| E29 | **Contracts & Data Licensing Counsel** | Reviews broker agreements, market-data licenses, LLM provider terms and privacy obligations, and catches redistribution or usage breaches. | 04, 05, 09 | `project-context`, `source-verification`, `us-securities-regulation`, `contract-license-review` |
| E30 | **AI Governance & Model Risk Officer** | Keeps the model inventory, controls model and prompt changes, enforces validation independence and LLM version pinning. | 03, 06, 08 | `project-context`, `decision-memo`, `statistical-validation`, `llm-lookahead-audit`, `compliance-recordkeeping`, `model-risk-governance` |

### Marketing & Communications

| ID | Expert | One-line job description | Key docs | Skills |
|---|---|---|---|---|
| E31 | **Marketing & Communications Strategist** | Shapes how the project is described to stakeholders and any future audience, keeping every claim compliant (no guaranteed or cherry-picked returns). | 01, 09 | `project-context`, `source-verification`, `compliant-communications`, `data-visualization`, `technical-writing` |
| E32 | **Technical Writer / Knowledge Manager** | Maintains the docs folder, runbooks, decision log and agent instructions so every expert works from current, cited information. | All | `project-context`, `source-verification`, `requirements-spec`, `technical-writing` |

> **Marketing note:** This is a personal trading system. E31's job is
> stakeholder communication and keeping any future public messaging
> compliant. Offering signals, performance or the system to other people
> can trigger investment-adviser or CTA registration (doc 09), so E31 must
> check with E27 before anything is published externally.

## Part 2 — Skill library

Each skill is defined once and shared. "Used by" lists every agent that loads it.


### Cross-cutting

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S01 | `project-context` | Read and cite the `docs/` research; apply the owner defaults in doc 12 as hard limits until changed. | E01, E02, E03, E04, E05, E06, E07, E08, E09, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31, E32 | 32 |
| S02 | `source-verification` | Web research with dated citations; re-verify vendor prices, fees and regulatory dates against official sources. | E01, E03, E04, E05, E07, E08, E09, E10, E11, E14, E19, E23, E25, E27, E29, E31, E32 | 17 |
| S03 | `decision-memo` | Write a recommendation memo: options, trade-offs, risks, recommendation, and what would change the call. | E01, E02, E04, E05, E06, E08, E22, E23, E24, E25, E27, E30 | 12 |
| S04 | `roadmap-gate-tracking` | Track work against the phased roadmap and promotion gates (docs 06 and 11); report blockers. | E01, E02, E03 | 3 |
| S05 | `requirements-spec` | Turn decisions into testable requirements and acceptance criteria. | E02, E03, E32 | 3 |
| S42 | `technical-writing` | Clear docs, runbooks and reports in markdown, kept current via pull requests. | E01, E02, E03, E20, E31, E32 | 6 |

### Data & Research

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S06 | `python-data-stack` | Python, Polars/pandas, Parquet and DuckDB for research and pipelines. | E07, E13, E15 | 3 |
| S07 | `point-in-time-hygiene` | Prevent look-ahead and survivorship bias; handle corporate actions, timestamps and exchange calendars. | E07, E12, E13, E15 | 4 |
| S08 | `market-data-apis` | Use Alpaca, Massive (Polygon), Databento, SEC EDGAR and FRED APIs within their rate limits and licenses. | E15, E23 | 2 |
| S09 | `backtesting` | Build and run backtests (vectorbt, custom engine, NautilusTrader) with realistic fills and costs. | E07, E09, E12 | 3 |
| S10 | `statistical-validation` | Purged walk-forward CV, Deflated Sharpe Ratio, PBO, multiple-testing haircuts, robustness checks. | E07, E12, E13, E26, E30 | 5 |
| S11 | `strategy-design` | Design and pre-register strategies (trend, momentum, vol targeting, factors) with an economic rationale. | E04, E07, E10 | 3 |
| S38 | `macro-regime-stress-testing` | Classify market regimes and stress-test against 2008, 2020, 2022 and similar episodes. | E04, E08, E22 | 3 |

### AI / ML

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S19 | `ml-modeling` | Feature engineering, labeling, gradient-boosted models, drift monitoring. | E13 | 1 |
| S20 | `llm-feature-engineering` | Versioned prompts, schema-validated outputs, response caching, ensembling and token budgets. | E14 | 1 |
| S21 | `llm-lookahead-audit` | Check model training cutoffs, anonymize entities, and accept only post-cutoff evidence. | E12, E14, E30 | 3 |
| S22 | `agent-orchestration` | Define agent roles, separation of duties, MCP tool scoping and escalation rules. | E01, E14 | 2 |

### Trading & Risk

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S12 | `portfolio-construction` | Turn signals into constrained target weights (caps, vol targeting, risk parity, turnover penalty). | E04, E07, E16, E22 | 4 |
| S13 | `risk-limits-kill-switches` | Specify and test account, strategy, position and order limits and kill switches. | E10, E16, E17, E22 | 4 |
| S14 | `position-sizing` | Volatility scaling and fractional Kelly sizing with haircut expected returns. | E22 | 1 |
| S15 | `execution-cost-modeling` | Order types, collars, slicing, auction orders; transaction-cost and slippage analysis. | E09, E16 | 2 |
| S16 | `broker-integration` | Alpaca, IBKR, Schwab and crypto exchange APIs; idempotent orders; paper vs. live separation. | E09, E11, E16, E21 | 4 |
| S17 | `derivatives-analytics` | Options Greeks, assignment, futures margin and rolls. | E10 | 1 |
| S18 | `crypto-exchange-ops` | Exchange selection, trade-only keys, custody and 24/7 operating risk. | E11 | 1 |

### Engineering & Operations

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S23 | `software-engineering` | Production Python, code review, PR workflow, clean interfaces. | E13, E14, E15, E16, E17, E18 | 6 |
| S24 | `testing-and-fire-drills` | Unit and integration tests, backtest regression snapshots, kill-switch fire drills. | E12, E17 | 2 |
| S25 | `infrastructure-ci-cd` | Docker, infrastructure as code, scheduling, CI/CD, environment separation. | E18, E19 | 2 |
| S26 | `observability-alerting` | Metrics, structured logs, heartbeats, alert routing. | E15, E18, E21 | 3 |
| S27 | `security-and-secrets` | Secrets management, key scoping, threat modeling, prompt-injection defense. | E14, E19 | 2 |
| S28 | `reconciliation-ledger` | Position and cash reconciliation; order/fill ledger; tax lots. | E16, E21, E25, E28 | 4 |
| S29 | `incident-response` | Contain, assess, reconcile, communicate, fix, and write the postmortem. | E18, E19, E21, E28 | 4 |

### Finance, Legal & Governance

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S30 | `performance-reporting` | Tear sheets, attribution, benchmark comparison, live-vs-backtest tracking. | E20, E22, E24, E26 | 4 |
| S31 | `tax-analysis` | After-tax returns, wash sales, holding periods, Section 1256, §475(f), crypto, IRAs. | E05, E10, E11, E25, E26 | 5 |
| S32 | `us-securities-regulation` | FINRA Rule 4210 intraday margin, market-manipulation rules, adviser/CTA registration triggers. | E25, E27, E28, E29 | 4 |
| S33 | `compliance-recordkeeping` | Pre-trade conduct checks, restricted lists, 7-year record retention, audit trails. | E21, E28, E30 | 3 |
| S34 | `contract-license-review` | Broker agreements, data licenses, LLM provider terms, privacy. | E23, E29 | 2 |
| S35 | `model-risk-governance` | Model inventory, change control, independent validation, version pinning. | E30 | 1 |
| S36 | `vendor-management` | Vendor evaluation, SLAs, rate limits, cost tracking, exit plans. | E23, E24 | 2 |
| S37 | `budgeting-tco` | Budgets, total cost of ownership, cost vs. net trading value. | E23, E24 | 2 |
| S43 | `personal-financial-planning` | Risk capacity, capital at risk, account-type selection, fit with overall finances. | E05 | 1 |

### People & Communication

| ID | Skill | What it covers | Used by | # |
|---|---|---|---|---|
| S39 | `behavioral-finance` | Recognize and counter investor biases; design bias-resistant approval steps. | E05, E06 | 2 |
| S40 | `compliant-communications` | Messaging with no guaranteed or cherry-picked performance claims; follows regulators' AI-fraud guidance. | E06, E31 | 2 |
| S41 | `data-visualization` | Dashboards and charts that make risk and performance clear. | E20, E26, E31 | 3 |

## Part 3 — Most-shared skills

The skills worth building first, because the most agents depend on them:

| Skill | Agents using it |
|---|---|
| `project-context` | 32 |
| `source-verification` | 17 |
| `decision-memo` | 12 |
| `software-engineering` | 6 |
| `technical-writing` | 6 |
| `statistical-validation` | 5 |
| `tax-analysis` | 5 |
| `point-in-time-hygiene` | 4 |
| `portfolio-construction` | 4 |
| `risk-limits-kill-switches` | 4 |
| `broker-integration` | 4 |
| `reconciliation-ledger` | 4 |

## Part 4 — Turning these into agents

Suggested layout once agents are built:

```
agents/
  E01-engagement-lead.md        # role prompt: mission, docs to read, skills, restrictions
  ...
skills/
  project-context/SKILL.md      # one folder per skill, shared by reference
  ...
```

For each agent definition, include:
1. **Mission:** the one-line job description above.
2. **Read first:** docs 01, 08, 11 and 12, plus its key docs.
3. **Skills:** load the listed skills by name.
4. **Restrictions:** the ground rules above, plus any veto or approval duty.
5. **Outputs:** the artifacts it hands off (see doc 11's handoff table).

