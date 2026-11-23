---
name: security-and-secrets
description: "Secure the system: secrets management, broker/exchange key scoping, threat modeling and prompt-injection defense for LLM components. Use for any security review or key handling."
user-invocable: false
---
# Security and secrets

## Checklist (doc 10)
- [ ] Live keys in a secrets manager/encrypted env, injected at runtime; never in git, logs, prompts or LLM context.
- [ ] Broker: 2FA, IP allowlist, trading-only scope, no withdrawals/transfers via API, separate key per service.
- [ ] Crypto: trade-only, withdrawal disabled, IP allowlisted.
- [ ] Agents/MCP servers get paper keys or read-only internal APIs only.
- [ ] Prompt injection: news/filings/web text is untrusted; LLM output is schema-validated and can only produce bounded features.
- [ ] Dependencies pinned and scanned in CI.
- [ ] Least-privilege cloud IAM; SSH keys only; automatic security updates.
- [ ] Backups encrypted; restore tested.
- [ ] Audit log of config, limit and deploy changes.

## Threat model prompts
What if a key leaks? What if a news item contains "sell everything"? What if a dependency is compromised? What if the agent loops placing orders? For each: prevention, detection, response.

## If a secret leaks
Revoke/rotate immediately, check broker activity, freeze trading, write a postmortem.
