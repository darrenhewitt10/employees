---
name: requirements-spec
description: "Turn owner decisions and design docs into numbered, testable requirements with acceptance criteria and traceability. Use when specifying any component or feature."
user-invocable: false
---
# Requirements specification

## Format
```markdown
### REQ-<AREA>-<NNN>: <short title>
**Source:** docs/12 decision #N | docs/07 section | owner request <date>
**Priority:** must | should | could
**Requirement:** The system shall ...
**Acceptance criteria:**
- Given <state>, when <event>, then <observable result>
**Verification:** unit test | integration test | fire drill | review
**Owner agent:** <name>
```

## Areas
DATA, SIG (signals), PORT (portfolio), RISK, EXEC, RECON, LLM, OPS, SEC, COMP (compliance), TAX, RPT (reporting).

## Rules
- One behavior per requirement; measurable thresholds (numbers, not "fast" or "safe").
- Every risk limit in doc 07 and every default in doc 12 becomes a RISK/COMP requirement.
- Include non-functional requirements: reproducibility, latency of daily cycle, record retention (7 years), secrets handling.
- Keep a traceability table: requirement -> test -> status.
- Mark assumptions explicitly and link them to open doc 12 questions.
