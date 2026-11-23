---
name: agent-skill-authoring
description: "Create, edit and validate this project's Claude Code subagents (.claude/agents/) and skills (.claude/skills/), following the official format and keeping roster, routing and CLAUDE.md in sync. Use when adding or improving agents or skills."
user-invocable: false
---
# Agent and skill authoring (per code.claude.com/docs/en/sub-agents and /skills)

## Subagent files: `.claude/agents/<name>.md`
Frontmatter between `---` lines (first line of the file), then the system prompt in markdown.
- Required: `name` (lowercase-hyphen convention, unique, no `:`, max 256 chars) and `description` (when to delegate; one or two sentences that single this agent out; "use proactively" encourages auto-delegation).
- Optional: `tools` (comma string, allowlist; omit to inherit all), `disallowedTools`, `model` (`sonnet`, `opus`, `haiku`, `fable`, full ID, or `inherit`), `skills` (YAML list; **full content preloaded at startup**, max 32), `color` (red, blue, green, yellow, purple, orange, pink, cyan), `maxTurns`, `memory` (`user`/`project`/`local`), `permissionMode`, `effort`, `isolation: worktree`, `hooks`, `mcpServers`.
- Field names are exact camelCase; **unknown fields are ignored silently** - always run the validator.
- Spawning: tool name `Agent`. Subagents can nest up to three layers by default. `Agent(a, b)` allowlists only apply when the agent runs as the main session (`claude --agent <name>`).
- Keep descriptions short (all descriptions load every session); put detail in the body.

## Skill files: `.claude/skills/<name>/SKILL.md`
- Frontmatter: `name` (= directory name), `description` (key use case first; description + `when_to_use` truncated at 1,536 chars). Optional: `when_to_use`, `user-invocable`, `disable-model-invocation` (true **prevents preloading into subagents**), `allowed-tools`, `context: fork` + `agent: <type>`, `background`, `argument-hint`, `model`, `effort`, `paths`.
- Body under 500 lines; concise standing instructions; move detail to sibling files linked from SKILL.md.
- Substitutions: `$ARGUMENTS`, `$0`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`.
- This project hides knowledge skills from the `/` menu with `user-invocable: false`; `/ask-team` is the user entry point.

## Procedure for a new or changed expert
1. Check `docs/expert-roster.md` for overlap; prefer improving an existing agent or skill over adding one. Total agents must stay within 10-50.
2. Reuse existing skills; create a new skill only for knowledge used by 2+ agents or clearly reusable.
3. Write/update the agent file (mission, personality, knowledge-folder step, responsibilities, how you work, deliverables, works with, boundaries) and its `skills:` list (always include `project-context`). Every agent has:
   - **A model** from `docs/agent-brains.md`: `opus` for deep strategy, legal and finance judgment or veto holders; `sonnet` for most specialist work; `haiku` for fast lookups and upkeep (haiku agents escalate judgment calls).
   - **A persona:** a unique first name (prefixed in the description as `"Name - ..."`), a voice and a working style, in a `## Personality` section.
   - **A knowledge folder** `knowledge/<agent-name>/README.md` listing what belongs there, and a `## Before answering: read your knowledge folder` section (copy it from an existing agent, changing the name).
4. Update in the same change: `docs/expert-roster.md` (role and skill tables), `docs/agent-brains.md` (name, model, reason, voice, style), `.claude/skills/expert-routing/SKILL.md` (routing rows), the orchestrator's `Agent(...)` tool allowlist and expert list, and the team table in `CLAUDE.md`.
5. Run `python3 .claude/scripts/validate_team.py` and fix every error.
6. Summarize what changed and why.
