#!/usr/bin/env python3
"""Validate the expert team: .claude/agents/*.md and .claude/skills/*/SKILL.md.

Claude Code ignores unknown frontmatter fields silently and skips malformed
files, so this script catches mistakes the app won't report. Run from the
repo root:  python3 .claude/scripts/validate_team.py
Exit code 0 = OK, 1 = errors found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / ".claude" / "agents"
SKILLS = ROOT / ".claude" / "skills"
ROUTING = SKILLS / "expert-routing" / "SKILL.md"
ROSTER = ROOT / "docs" / "expert-roster.md"
CLAUDE_MD = ROOT / "CLAUDE.md"
COORDINATORS = {"orchestrator", "meta-agent"}

AGENT_FIELDS = {
    "name", "description", "tools", "disallowedTools", "model", "permissionMode",
    "maxTurns", "autoCompactWindow", "skills", "mcpServers", "hooks", "memory",
    "background", "omitClaudeMd", "effort", "isolation", "color", "initialPrompt",
    "experimental",
}
SKILL_FIELDS = {
    "name", "description", "when_to_use", "argument-hint", "arguments",
    "disable-model-invocation", "user-invocable", "allowed-tools", "disallowed-tools",
    "model", "effort", "context", "agent", "background", "hooks", "paths", "shell",
    "metadata", "license", "compatibility",
}
COLORS = {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"}
MODELS = {"sonnet", "opus", "haiku", "fable", "inherit"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

errors, warnings = [], []


def parse_frontmatter(path):
    """Minimal parser for the flat frontmatter used in this project."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: opening '---' must be the first line")
        return {}, ""
    try:
        end = text.index("\n---\n", 4)
    except ValueError:
        errors.append(f"{path}: no closing '---'")
        return {}, ""
    fm, body, key = {}, text[end + 5:], None
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(line[4:].strip())
            continue
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if not m:
            errors.append(f"{path}: cannot parse frontmatter line: {line!r}")
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        fm[key] = val if val else []
    return fm, body


# ---- skills ----
skills = {}
for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d}: missing SKILL.md")
        continue
    fm, body = parse_frontmatter(f)
    for k in fm:
        if k not in SKILL_FIELDS:
            errors.append(f"{f}: unknown skill field '{k}' (would be ignored)")
    if fm.get("name") != d.name:
        errors.append(f"{f}: name '{fm.get('name')}' must equal directory '{d.name}'")
    desc = fm.get("description") or ""
    if not desc:
        errors.append(f"{f}: missing description")
    if len(desc) + len(fm.get("when_to_use") or "") > 1536:
        errors.append(f"{f}: description + when_to_use over 1,536 chars")
    if len(body.splitlines()) > 500:
        warnings.append(f"{f}: body over 500 lines; move detail to supporting files")
    if fm.get("context") == "fork" and fm.get("agent") and not (AGENTS / f"{fm['agent']}.md").exists() \
            and fm["agent"] not in {"Explore", "Plan", "general-purpose"}:
        errors.append(f"{f}: agent '{fm['agent']}' does not exist")
    skills[d.name] = fm

# ---- agents ----
agents, used_skills = {}, set()
for f in sorted(AGENTS.glob("*.md")):
    fm, body = parse_frontmatter(f)
    name = fm.get("name")
    for k in fm:
        if k not in AGENT_FIELDS:
            errors.append(f"{f}: unknown agent field '{k}' (would be ignored)")
    if not name:
        errors.append(f"{f}: missing name")
        continue
    if not NAME_RE.match(name):
        errors.append(f"{f}: name '{name}' should be lowercase words joined by hyphens")
    if f.stem != name:
        errors.append(f"{f}: file name should match name '{name}'")
    if name in agents:
        errors.append(f"{f}: duplicate agent name '{name}'")
    if not fm.get("description"):
        errors.append(f"{f}: missing description (file would be skipped)")
    if fm.get("color") and fm["color"] not in COLORS:
        errors.append(f"{f}: invalid color '{fm['color']}'")
    model = fm.get("model")
    if model and model not in MODELS and not str(model).startswith("claude-"):
        errors.append(f"{f}: invalid model '{model}'")
    sk = fm.get("skills") or []
    if not isinstance(sk, list):
        errors.append(f"{f}: skills must be a YAML list")
        sk = []
    if len(set(sk)) > 32:
        errors.append(f"{f}: more than 32 skills (extra ones are not preloaded)")
    if "project-context" not in sk:
        errors.append(f"{f}: must preload project-context")
    for s in sk:
        if s not in skills:
            errors.append(f"{f}: skill '{s}' does not exist in .claude/skills/")
        elif str(skills[s].get("disable-model-invocation", "")).lower() in {"true", "yes", "on", "1"}:
            errors.append(f"{f}: skill '{s}' has disable-model-invocation and cannot be preloaded")
        used_skills.add(s)
    if not body.strip():
        errors.append(f"{f}: empty system prompt")
    agents[name] = fm

# ---- team-level checks ----
n = len(agents)
if not 10 <= n <= 50:
    errors.append(f"team has {n} agents; keep between 10 and 50")
for s, fm in skills.items():
    entrypoint = fm.get("context") == "fork"
    if s not in used_skills and not entrypoint:
        warnings.append(f"skill '{s}' is not preloaded by any agent")

experts = set(agents) - COORDINATORS
for missing in COORDINATORS - set(agents):
    errors.append(f"missing coordinator agent '{missing}'")

orch = agents.get("orchestrator", {})
m = re.search(r"Agent\(([^)]*)\)", orch.get("tools", "") or "")
allow = {x.strip() for x in m.group(1).split(",")} if m else set()
if orch and not m:
    errors.append("orchestrator tools must include Agent(...) allowlist")
for x in sorted(experts - allow):
    errors.append(f"orchestrator Agent(...) allowlist is missing '{x}'")
for x in sorted(allow - experts):
    errors.append(f"orchestrator Agent(...) allowlist names unknown or non-expert agent '{x}'")

routing = ROUTING.read_text(encoding="utf-8") if ROUTING.exists() else ""
for x in sorted(experts):
    if not re.search(rf"\b{re.escape(x)}\b", routing):
        errors.append(f"expert-routing table never mentions '{x}'")
for x in sorted(set(re.findall(r"\b[a-z]+(?:-[a-z]+)+\b", routing))):
    if x.endswith(("-specialist", "-manager", "-engineer", "-counsel", "-officer", "-analyst",
                   "-strategist", "-coach", "-lead", "-architect", "-planner", "-writer",
                   "-statistician", "-controller", "-advisor", "-designer")) and x not in agents:
        errors.append(f"expert-routing mentions unknown agent '{x}'")

# ---- brains, personas and knowledge folders ----
BRAINS = ROOT / "docs" / "agent-brains.md"
KNOWLEDGE = ROOT / "knowledge"
brains = {}
if BRAINS.exists():
    for m in re.finditer(r"^\| `([a-z0-9-]+)` \| ([^|]+?) \| \*\*([a-z]+)\*\* \|", BRAINS.read_text(encoding="utf-8"), re.M):
        brains[m.group(1)] = (m.group(2).strip(), m.group(3))
else:
    errors.append("docs/agent-brains.md is missing")
first_names = {}
for name, fm in agents.items():
    path = AGENTS / f"{name}.md"
    body = path.read_text(encoding="utf-8")
    if fm.get("model") not in {"opus", "sonnet", "haiku"}:
        errors.append(f"{path}: model must be opus, sonnet or haiku (see docs/agent-brains.md)")
    if name not in brains:
        errors.append(f"docs/agent-brains.md has no row for `{name}`")
    else:
        first, model = brains[name]
        if model != fm.get("model"):
            errors.append(f"{path}: model '{fm.get('model')}' but docs/agent-brains.md says '{model}'")
        if not (fm.get("description") or "").startswith(f"{first} - "):
            errors.append(f"{path}: description should start with '{first} - '")
        if first in first_names:
            errors.append(f"first name '{first}' used by both {first_names[first]} and {name}")
        first_names[first] = name
    if "## Personality" not in body:
        errors.append(f"{path}: missing '## Personality' section")
    if f"knowledge/{name}/" not in body:
        errors.append(f"{path}: system prompt must tell the agent to read knowledge/{name}/")
    if not (KNOWLEDGE / name / "README.md").exists():
        errors.append(f"knowledge/{name}/README.md is missing")
for x in sorted(set(brains) - set(agents)):
    errors.append(f"docs/agent-brains.md lists unknown agent `{x}`")
if KNOWLEDGE.exists():
    for d in sorted(p.name for p in KNOWLEDGE.iterdir() if p.is_dir()):
        if d not in agents:
            warnings.append(f"knowledge/{d}/ has no matching agent")

for doc, label in [(ROSTER, "docs/expert-roster.md"), (CLAUDE_MD, "CLAUDE.md")]:
    text = doc.read_text(encoding="utf-8") if doc.exists() else ""
    for x in sorted(agents):
        if f"`{x}`" not in text:
            errors.append(f"{label} does not list agent `{x}`")

for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\n{n} agents, {len(skills)} skills, {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
