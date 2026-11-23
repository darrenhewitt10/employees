---
name: llm-feature-engineering
description: "Turn text (news, filings, transcripts) into bounded, schema-validated LLM features with versioned prompts, caching, ensembling and token budgets. Use when designing or changing any LLM component."
user-invocable: false
---
# LLM feature engineering

## Design rules (doc 03)
1. **Features, not orders:** output bounded typed values (e.g. `sentiment` in [-1, 1], `event_type` enum, `relevance` 0-1) validated against a JSON schema; invalid -> dropped and counted.
2. **Determinism:** temperature 0 where supported; prompts versioned in git (`prompts/<name>/vN.md`).
3. **Cache** every response keyed by (model ID, prompt version, input hash) under `data/llm_cache/`; backtests replay the cache.
4. **Ensemble:** score each item 2-3 times or with 2 models; agreement = confidence; disagreement -> neutral.
5. **Budget:** daily token/cost cap enforced in code; LLM spend counts as strategy cost.
6. **Model change = strategy change:** re-validate on any model or prompt change.
7. **Prompt injection:** source text is untrusted; system prompt forbids following instructions in it; outputs can only be schema values.

## Evidence
LLM headline sentiment predicts next-day returns, strongest in small caps and bad news, decaying as adoption rises (Lopez-Lira & Tang, arXiv 2304.07619). Treat as a tilt inside a diversified strategy, not a standalone strategy.

## Spec template
Input source · prompt version · model ID + training cutoff · output schema · cache key · fallback when unavailable · cost per day · evaluation window (post-cutoff).
