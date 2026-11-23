---
name: llm-lookahead-audit
description: "Audit LLM-based results for look-ahead bias from memorization: training cutoffs, anonymization, post-cutoff evaluation. Use before trusting any LLM backtest or research claim."
user-invocable: false
---
# LLM look-ahead audit

## Why
An LLM trained through date T may already know outcomes after an older headline. Memorization substantially inflates apparent predictive power and the signal collapses after the training cutoff (Gao, Jiang & Yan, arXiv 2512.23847). Llama 2 mentioned Covid-19 in >25% of late-2019 risk assessments (Sarkar & Vafa 2024).

## Checklist
- [ ] Model ID and **published training cutoff** recorded for every result.
- [ ] Evidence window starts **after** the cutoff; pre-cutoff results labelled "exploratory only".
- [ ] Company names, tickers and dates anonymized in prompts where the task allows (Glasserman & Lin, arXiv 2309.17322).
- [ ] Probe test: ask the model what happened after the event; if it knows, the sample is contaminated.
- [ ] Results compared with a non-LLM baseline over the same window.
- [ ] Forward (paper) test planned before any real money.
- [ ] Model version pinned; upgrades trigger re-audit.

## Verdict
CLEAN / CONTAMINATED / UNKNOWN, with the evidence for each checklist item.
