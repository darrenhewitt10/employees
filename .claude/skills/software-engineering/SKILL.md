---
name: software-engineering
description: "Production Python engineering standards for this project: structure, typing, pure signal functions, config, code review and PR workflow. Use when writing or reviewing code."
user-invocable: false
---
# Software engineering standards

- **Structure:** `src/<package>/{data,signals,portfolio,risk,execution,ledger,reporting}`, `tests/`, `research/`, `strategies/<name>/config.yaml`.
- **Pure core:** signal and portfolio functions are pure (inputs -> outputs), shared by backtest and live.
- **Config:** Pydantic settings + YAML per environment (research/paper/live); validated at startup; no secrets in config files.
- **Types and docs:** type hints everywhere; docstrings on public APIs; `ruff` + `mypy` in CI.
- **Errors:** fail safe - on doubt, do nothing and alert; never swallow exceptions in order paths.
- **Logging:** structured JSON logs with run ID, strategy, rebalance ID.
- **Reviews:** every change is a PR with tests; a second agent reviews; risk-gateway and execution changes also need risk-manager review.
- **Dependencies:** pinned; minimal; vetted for maintenance status.
- Keep functions small; prefer clarity over cleverness; delete dead code.
