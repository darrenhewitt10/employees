---
name: model-risk-governance
description: "Govern models and prompts: inventory, change control, independent validation, version pinning, monitoring and retirement. Use when adding, changing or reviewing any model or LLM prompt."
user-invocable: false
---
# Model risk governance

## Model inventory (`docs/models/inventory.md`)
Per model/prompt: ID, purpose, owner agent, type (rule/ML/LLM), inputs, outputs, LLM model ID + training cutoff, prompt version, validation report link, approval date, monitoring metrics, status (research/paper/live/retired).

## Change control
- Any change to model, features, prompt, LLM version or retrain schedule = new version -> re-validation by validation-statistician -> risk sign-off -> owner approval if live.
- Pin LLM versions; track provider deprecation dates.

## Independence
The validator is never the developer. Findings are recorded and closed with evidence.

## Monitoring
Drift (inputs, outputs), live vs backtest performance, LLM schema failures and cost. Breach -> fall back to non-LLM signal or hold.

## Retirement
Criteria pre-defined (kill criteria); retired models keep their records.
