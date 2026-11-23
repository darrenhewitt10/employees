---
name: ml-modeling
description: "Build tabular ML signal models: labels, point-in-time features, gradient-boosted trees, purged walk-forward validation, drift monitoring. Use for any ML model in the signal layer."
user-invocable: false
---
# ML modeling

## Pipeline (doc 03)
1. **Labels:** forward returns over the holding horizon, volatility-scaled; consider triple-barrier labels. Cross-sectional rank targets reduce market-wide noise.
2. **Features:** multi-lookback returns, volatility, drawdown, volume; point-in-time fundamentals; calendar; macro (FRED); LLM text scores (post-cutoff only).
3. **Model:** LightGBM first (fast, robust); deep learning on daily prices is low priority (overfits); RL is research-only.
4. **Validation:** purged K-fold with embargo / walk-forward; hand to validation-statistician with the trial log.
5. **To portfolio:** scores -> constrained weights (never "buy top 1").
6. **Monitoring:** feature drift (PSI), prediction drift, live information coefficient vs backtest IC.

## Rules
- Always benchmark against the simple rule (e.g. plain momentum rank). If ML doesn't beat it out of sample, ship the rule.
- Fix seeds; record feature-set version, model params, data snapshot.
- Feature importance is a sanity check, not evidence.
- Retrain cadence is a pre-registered parameter, not ad hoc.
