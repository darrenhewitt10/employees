---
name: technical-writing
description: "Write and maintain clear project docs, runbooks, reports and agent instructions in markdown, following this repo's conventions. Use when creating or updating anything in docs/ or .claude/."
user-invocable: false
---
# Technical writing

## Repo conventions
- Topic docs live in `docs/NN-topic.md`; `docs/README.md` is the index - update it when adding a doc.
- Each doc starts with `# NN - Title` and a `> **Purpose for agents:**` block naming the owner agent.
- Time-sensitive facts carry dates and source links (see source-verification).
- Tables for comparisons; numbered steps for procedures; no walls of prose.
- Incidents go in `docs/incidents/YYYY-MM-DD-slug.md`; decisions in `docs/decisions/`.
- Changes go through pull requests; mention which docs/agents are affected.

## Style
- Lead with the answer. Short sentences. Plain words over jargon; define acronyms on first use.
- Write for an agent that has never seen the conversation: name files, owners, thresholds.
- Don't duplicate content across docs - link to the owning doc.

## When agents or skills change
Keep `docs/expert-roster.md`, `CLAUDE.md` and `.claude/skills/expert-routing/SKILL.md` consistent with `.claude/agents/` (meta-agent owns this; run `python3 .claude/scripts/validate_team.py`).
