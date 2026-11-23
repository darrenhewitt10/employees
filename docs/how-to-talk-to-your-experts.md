# How to Talk to Your Experts

> **Purpose:** Copy-paste prompts for the 34-agent expert team built in
> `.claude/agents/`. Run them in Claude Code from this repo. See
> [expert-roster.md](expert-roster.md) for who's on the team and what each
> expert does.

There are three ways to ask:

| You want | Use | What happens |
|---|---|---|
| One expert's view | Name the agent | That expert answers alone, from its own domain |
| Several experts, one answer | `/ask-team` or "Use the orchestrator to…" | The orchestrator picks the right experts, runs them, resolves disagreements and returns one combined answer |
| Every question in the session routed through the team | `claude --agent orchestrator` | The whole session runs as the orchestrator |

## 1. Ask one specific expert

Name the expert in plain language:

```text
Ask the tax-advisor: if a momentum strategy rebalances monthly in a taxable account, roughly how much of a 10% gross return would short-term gains tax eat, and would running it in an IRA be better?
```

```text
Use the risk-manager subagent to review the default limits in docs/12-decisions-needed.md for a $10,000 paper account and tell me which ones you'd tighten.
```

Or @-mention it (type `@` and pick the agent, or type it out):

```text
@agent-validation-statistician What would you need to see before you'd believe a backtest with a Sharpe ratio of 2.5?
```

**Tips:**
- Use the exact agent name from the roster (`tax-advisor`, `risk-manager`, `quant-researcher`…).
- An expert stays in its lane. If part of your question belongs to someone else, it will say so and name them. When that happens, ask the team instead.

## 2. Ask the whole team (via the orchestrator)

Either type the slash command:

```text
/ask-team Are we ready to start phase 1, and what's the first week of work?
```

Or ask for the orchestrator in plain language:

```text
Use the orchestrator to tell me whether we're ready to start phase 1 and what the first week of work should be.
```

Or make the orchestrator the whole session, then just ask questions:

```bash
claude --agent orchestrator
```

**What "the whole team" means:** the orchestrator doesn't wake all 32 experts. It reads the question and picks 2–5 experts, plus any reviewers who must be included (risk, validation, legal, tax, security, AI governance). It never uses more than 7. That keeps answers focused and cheaper.

**What you get back:** one answer with these sections: **Answer**, **Why** (each point credited to an expert), **Where the experts disagreed**, **Vetoes and required approvals**, **Next steps** (each with an owner) and **Experts consulted**.

## 3. Example prompts that bring several experts together

Each one crosses several domains on purpose, so the orchestrator has to coordinate. The expert lists are what the routing table points to; the orchestrator makes the final call.

### Example A — How much money, where, and how much loss is OK

```text
/ask-team I have $25,000 I could put toward this project once we reach phase 6. How much of it should go into the automated strategy versus a plain index fund, should it be in my taxable account or my IRA, and what drawdown limit should trigger the kill switch? I tend to get nervous after losses.
```

Likely experts: `financial-planner`, `tax-advisor`, `risk-manager`, `behavioral-finance-coach`, `finance-controller`.
Why it's a good test: they pull in different directions. The planner limits capital at risk, tax favors the IRA for high turnover, risk sets the limits, the coach designs guardrails against panic overrides, and finance checks whether the costs are worth it at that size.

### Example B — Adding an AI news signal safely

```text
Use the orchestrator: we want to add an LLM news-sentiment tilt to the ETF momentum strategy. Design how it should work and list everything that has to be true before it can go to paper trading.
```

Likely experts: `llm-agent-architect`, `quant-researcher`, `validation-statistician`, `ai-governance-officer`, `risk-manager`, `security-engineer`.
Why it's a good test: it touches design, look-ahead bias in LLM backtests, model change control, prompt injection from news text, and the promotion gates. It's very likely to produce a veto condition from validation.

### Example C — Something went wrong in paper trading

```text
/ask-team We've been paper trading for four weeks. Fills are costing about 3x the slippage our backtest assumed, and on Tuesday our positions didn't match the broker's after the close. What should we do, in what order, and does this reset our paper track record?
```

Likely experts: `trading-operations-manager`, `execution-specialist`, `risk-manager`, `performance-analyst`, `validation-statistician`, `platform-sre-engineer`.
Why it's a good test: incident response (freeze, reconcile), recalibrating the cost model, and whether the paper-to-live gate clock restarts all have to be merged into one ordered plan.

### Example D — Sharing results publicly

```text
Use the orchestrator: I'd like to post our monthly paper-trading results on the Netlify docs site, and maybe one day sell the signals to friends. What am I allowed to do, what would the page need to say, and what should I avoid?
```

Likely experts: `securities-regulatory-counsel`, `marketing-communications-strategist`, `compliance-officer`, `performance-analyst`, `contracts-licensing-counsel`, `validation-statistician`.
Why it's a good test: adviser-registration triggers, honest performance presentation, data-license limits on publishing vendor data, and record-keeping all apply at once. Counsel review is mandatory for anything public, and validation review is mandatory for any performance claim.

## 4. Getting better answers

- **Give the facts that change the answer:** amounts, which phase you're in, account type, deadlines. Without them, the team falls back to the defaults in [12-decisions-needed.md](12-decisions-needed.md) and says so.
- **Ask for the format you want:** "as a decision memo", "as a checklist", "as requirements with acceptance criteria".
- **Save the result:** add "…and save the answer to `docs/decisions/<name>.md`". The orchestrator only reads files; your main Claude session writes the answer into the repo.
- **Follow up on one point:** after a team answer, ask the specific expert, e.g. "Ask the risk-manager to expand on its condition."
- **Expect a few minutes and more usage:** a team question runs several agents, often in parallel. A single expert is quicker and cheaper.
- **To change the team itself:** "Ask the meta-agent to add a … expert" or "…to improve how the orchestrator routes tax questions."

## Things the team will not do

- Place live trades or handle live broker keys. Live orders only come from the deterministic pipeline through the risk gateway.
- Loosen a risk limit, go live or add capital without your explicit approval.
- Give professional legal, tax or financial advice. These experts do research; confirm material decisions with a licensed professional.
