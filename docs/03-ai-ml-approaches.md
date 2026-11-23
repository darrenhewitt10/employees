# 03 — AI / ML Approaches

> **Purpose for agents:** Which AI techniques to use where, what the research
> says about each, and the specific pitfalls (especially look-ahead bias in
> LLMs). ML/LLM Researcher agents own this.

## Map of techniques to roles

| Technique | Good for | Poor for | Our use |
|---|---|---|---|
| **Rules / classical stats** (moving averages, z-scores, regressions) | Transparent baseline signals, risk models | Nonlinear interactions | Baseline strategies; always the control group |
| **Gradient-boosted trees** (LightGBM, XGBoost, CatBoost) | Tabular features → return/direction forecasts; robust, fast | Raw sequences, text | Primary ML signal model for cross-sectional ranking |
| **Deep learning on prices** (LSTM, temporal CNN, transformers) | Very large datasets, high-frequency data | Low signal-to-noise daily data (overfits easily) | Low priority; only with strong validation |
| **Reinforcement learning** (PPO, SAC, DQN via FinRL etc.) | Execution and position-sizing policies in simulators | Learning alpha from scratch on noisy markets | Research only; reward hacking and sim-to-real gap are severe |
| **LLMs — text understanding** | Scoring news, filings (10‑K/10‑Q/8‑K), earnings calls; extracting events | Numeric forecasting from raw price series | Feature generator feeding the ML/rules layer |
| **LLMs — agents** | Research automation, code generation, monitoring, explaining anomalies, writing reports | Unsupervised live order generation | Agent team (see [11](11-agent-team-and-roadmap.md)); never bypass the risk gateway |

## LLMs in trading: what the evidence supports

**Supported:**
- LLM sentiment/relevance scoring of headlines carries next-day return signal,
  strongest in small caps and negative news, decaying as adoption rises
  ([Lopez-Lira & Tang, arXiv 2304.07619](https://arxiv.org/abs/2304.07619)).
- Multi-agent "trading firm" designs (analyst roles → researcher debate →
  trader → risk team) are an active research area, e.g.
  **TradingAgents** (UCLA/MIT/Tauric Research, [arXiv 2412.20138](https://arxiv.org/abs/2412.20138),
  [GitHub](https://github.com/TauricResearch/TradingAgents), LangGraph-based,
  supports Anthropic/OpenAI/Google/local models). Its README states it is for
  research, not trading advice.

**Not supported (yet):**
- LLMs as autonomous end-to-end traders: Alpha Arena and StockBench results were
  mostly negative or marginal (see [01-reality-check.md](01-reality-check.md)).
- Common failure modes: overtrading, inconsistency across runs with identical
  inputs, sensitivity to prompt wording, degraded performance with larger
  universes.

### Design rules for LLM components

1. **LLM outputs are features, not orders.** Convert to structured, bounded
   values (e.g., sentiment ∈ [−1, 1], event type enum) validated by schema.
2. **Determinism:** temperature 0 where supported, fixed prompts versioned in
   git, cache every LLM response keyed by (model, prompt version, input hash)
   so backtests are reproducible and cheap to rerun.
3. **Ensemble / repeat:** score each item multiple times or with multiple models
   and use agreement as a confidence measure; inconsistency is a known issue.
4. **Cost budget:** per-day token budget enforced in code; LLM spend is part of
   strategy cost when computing net returns.
5. **Model changes are strategy changes.** Swapping model versions requires
   re-validation, exactly like changing a parameter.

## Look-ahead bias in LLMs

This is the single biggest trap in LLM-based backtests. A model trained on
internet data through date *T* may "know" what happened to a stock after a
2019 headline.

- **Gao, Jiang & Yan, "A Test of Lookahead Bias in LLM Forecasts"**
  ([arXiv 2512.23847](https://arxiv.org/abs/2512.23847), Dec 2025, preprint):
  memorization substantially inflates apparent predictive power; the signal
  **collapses toward zero after the model's training cutoff.**
- **Sarkar & Vafa (2024):** Llama 2 mentioned Covid‑19 in >25% of risk
  assessments for *late‑2019* earnings calls — direct leakage (cited in
  [arXiv 2412.07031](https://arxiv.org/abs/2412.07031)).
- **Glasserman & Lin ([arXiv 2309.17322](https://arxiv.org/abs/2309.17322)):**
  decompose in-sample effect into look-ahead bias and a "distraction" effect;
  **anonymizing company names reduces bias.**
- **Chronologically consistent LLMs** ([arXiv 2502.21206](https://arxiv.org/abs/2502.21206))
  train only on data available at each date; authors find the look-ahead
  effect on news-return prediction modest *for their setup*.
- **Look-Ahead-Bench** ([arXiv 2601.13770](https://arxiv.org/abs/2601.13770), Jan 2026)
  proposes a standard benchmark for point-in-time financial LLMs.

**Mitigations we adopt:**
- Only treat LLM-signal results as evidence if the test period is **after the
  model's training cutoff.** Pre-cutoff results are exploratory at best.
- Anonymize entity names and dates in prompts where the task allows.
- Prefer forward (paper) testing for any LLM-derived signal before real money.
- Record the model ID and its published training cutoff with every result.

## Classical ML pipeline (for tabular signals)

1. **Labels:** forward returns over the holding horizon, ideally
   volatility-scaled; consider triple-barrier labeling (López de Prado,
   *Advances in Financial Machine Learning*, 2018).
2. **Features:** price/volume transforms (returns over multiple lookbacks,
   volatility, drawdown), fundamentals (point-in-time only), calendar, LLM text
   scores, macro (FRED).
3. **Model:** start with LightGBM; rank-based cross-sectional targets reduce
   sensitivity to market-wide moves.
4. **Validation:** purged/embargoed walk-forward CV; see
   [06-backtesting-and-validation.md](06-backtesting-and-validation.md).
5. **Portfolio construction:** convert scores to weights with risk constraints
   (position caps, sector caps, volatility target) — never "buy top 1".
6. **Monitoring:** feature drift, prediction drift, live IC (information
   coefficient) vs. backtest IC.

## Open-source projects worth studying

| Project | What it is | Use for |
|---|---|---|
| [TradingAgents](https://github.com/TauricResearch/TradingAgents) | Multi-agent LLM trading-firm simulation (LangGraph) | Reference design for agent roles and debate |
| [FinRL / FinRL-Meta](https://github.com/AI4Finance-Foundation) | Deep RL environments for trading | RL experiments, execution/sizing research |
| [FinGPT](https://arxiv.org/abs/2306.06031) | Open-source financial LLMs, LoRA fine-tuning | Local/cheap sentiment models |
| [FinWorld](https://arxiv.org/abs/2508.02292) | End-to-end financial AI research platform | Survey of baselines |
| [Alpaca MCP server](https://github.com/alpacahq/alpaca-mcp-server) | MCP tools for Alpaca trading/data | Agent access to **paper** account and market data |
