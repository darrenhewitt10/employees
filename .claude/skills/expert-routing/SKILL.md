---
name: expert-routing
description: "Routing table for the orchestrator: which expert agents to bring in for each kind of question, which reviewers are mandatory, and team-size rules. Use when deciding who should answer a question."
user-invocable: false
---
# Expert routing

## Steps
1. Classify the question into one or more topics below.
2. Pick **2-5 experts**: the primary expert(s) for each topic, plus any **mandatory reviewers**.
3. A simple single-domain fact question may go to one expert. Never call more than 7.
4. If no topic fits, use engagement-lead and say the routing was a best guess.

## Topic -> primary experts
| Topic | Primary experts |
|---|---|
| Goals, plans, priorities, "what should we do next" | engagement-lead, program-manager, investment-strategist |
| Requirements, specs, acceptance criteria | business-analyst, program-manager |
| How much money to put in, account type, suitability | financial-planner, behavioral-finance-coach, tax-advisor |
| Emotions, overrides, "should I turn it off after losses" | behavioral-finance-coach, risk-manager |
| Strategy ideas, factors, trend/momentum | quant-researcher, investment-strategist, macro-strategist |
| Market regimes, macro, stress scenarios | macro-strategist, risk-manager |
| Order execution, slippage, costs | execution-specialist, trading-systems-architect |
| Options, futures | derivatives-specialist, risk-manager, tax-advisor |
| Crypto | digital-asset-specialist, security-engineer, tax-advisor |
| Is this backtest real? overfitting | validation-statistician, quant-researcher |
| ML models | ml-engineer, validation-statistician |
| LLM features, agents, prompts, look-ahead | llm-agent-architect, ai-governance-officer, validation-statistician |
| Data sources, pipelines, data quality | data-engineer, vendor-procurement-manager |
| System design, code, broker integration | trading-systems-architect, execution-specialist, qa-test-engineer |
| Testing, release readiness | qa-test-engineer, platform-sre-engineer |
| Hosting, CI/CD, monitoring | platform-sre-engineer, security-engineer |
| Security, keys, prompt injection | security-engineer, llm-agent-architect |
| Dashboards, reports UX | ux-dashboard-designer, performance-analyst |
| Daily operations, reconciliation, incidents | trading-operations-manager, platform-sre-engineer |
| Risk limits, sizing, kill switches | risk-manager, investment-strategist |
| Vendors, brokers, pricing | vendor-procurement-manager, finance-controller, contracts-licensing-counsel |
| Budget, costs, is it worth it | finance-controller, investment-strategist |
| Taxes | tax-advisor, financial-planner |
| Performance, attribution, reviews | performance-analyst, validation-statistician |
| Regulation, legality, registration | securities-regulatory-counsel, compliance-officer |
| Compliance controls, records | compliance-officer, trading-operations-manager |
| Contracts, data licenses, provider terms | contracts-licensing-counsel, vendor-procurement-manager |
| Model governance, model changes | ai-governance-officer, validation-statistician |
| Public messaging, sharing results | marketing-communications-strategist, securities-regulatory-counsel |
| Documentation, runbooks, knowledge | technical-writer, business-analyst |

## Mandatory reviewers
| If the question involves... | Always include |
|---|---|
| Promoting a strategy/model, or any performance claim | validation-statistician |
| Trading, limits, sizing, going live, adding capital | risk-manager |
| Anything shared outside the owner | securities-regulatory-counsel |
| Taxable decisions (selling, account choice) | tax-advisor |
| Keys, access, new integrations | security-engineer |
| LLM in any decision path | ai-governance-officer |
