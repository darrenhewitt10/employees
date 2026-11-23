---
name: multi-expert-synthesis
description: "Run a multi-expert discussion and merge it into one answer: briefs, parallel analysis, cross-review of disagreements, veto handling and the final combined answer format. Use whenever several experts contribute to one question."
user-invocable: false
---
# Multi-expert synthesis

## Round 1 - independent analysis (parallel)
Send each chosen expert the same brief:
```
Question: <user question, verbatim>
Context: <relevant facts, files, prior decisions>
Your angle: <why you were chosen, what to focus on>
Answer in the project's standard answer format (Bottom line / Analysis / Risks / Next step / Confidence / Sources). Max ~300 words. Stay in your domain; flag anything outside it for another expert.
```
Launch independent experts in parallel.

## Round 2 - cross-review (only if needed)
If experts disagree on a material point, or a mandatory reviewer raises a concern, send the conflicting positions to the relevant experts (usually 1-2) and ask them to respond to the specific disagreement. Max one extra round.

## Resolution rules
1. **Vetoes win:** a risk-manager or validation-statistician objection blocks a recommendation until resolved; say so plainly.
2. **Evidence over opinion:** prefer the position with cited data from `docs/` or primary sources.
3. **Domain authority:** on legal, tax or security questions, defer to that expert.
4. If still unresolved, present both options and make it an **owner decision**.

## Final answer format
```markdown
## Answer
<2-4 sentence combined recommendation>

## Why
- Key points, each attributed with first name and agent: (Ruth, risk-manager), (Cora, tax-advisor)...

## Where the experts disagreed
- <point>: <position A (Name, agent)> vs <position B (Name, agent)> -> <resolution or owner decision>

## Vetoes and required approvals
- <none> | <who, what is blocked, what would clear it>

## Next steps
1. <action> - owner: <agent or owner>

## Experts consulted
<Name (agent), ...> · Confidence: high/medium/low
```
Keep it shorter than the sum of the inputs. Do not invent facts no expert provided.
