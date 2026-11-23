---
name: statistical-validation
description: "Judge whether backtest results are real: purged walk-forward CV, Deflated Sharpe Ratio, Probability of Backtest Overfitting, multiple-testing haircuts, robustness. Use before promoting any strategy or model."
user-invocable: false
---
# Statistical validation

## Protocol (doc 06)
1. Pre-registration exists and predates the tests.
2. Trial log complete: N = number of configurations tried.
3. Splits: development -> walk-forward -> untouched holdout (last 1-2 years, used once).
4. ML: purged K-fold with embargo, or combinatorial purged CV.
5. Compute the statistics below; run robustness; compare to benchmark.

## Probabilistic and Deflated Sharpe Ratio (Bailey & Lopez de Prado 2014)
With per-period Sharpe `SR`, T observations, skew `g3`, kurtosis `g4` (not excess):
`PSR(SR*) = Phi( (SR - SR*) * sqrt(T-1) / sqrt(1 - g3*SR + (g4-1)/4 * SR^2) )`
DSR = PSR with `SR*` = expected maximum Sharpe of N unskilled trials:
`SR* = sqrt(Var[SR_n]) * ( (1-gamma)*Phi^-1(1 - 1/N) + gamma*Phi^-1(1 - 1/(N*e)) )`, gamma ~ 0.5772.
**Gate: DSR >= 0.95.**

## Probability of Backtest Overfitting (CSCV)
Split the trial-return matrix into S even blocks; for each combination of S/2 blocks as in-sample, pick the best in-sample config and find its out-of-sample rank; PBO = share of combinations where that rank is below the median. **Gate: PBO <= 0.2.**

## Also require
- t-stat of mean excess return >= ~3 (Harvey, Liu & Zhu 2016).
- Parameter plateau (not a spike); survives costs x1.5, one-bar delay, removing best 5 days.
- Works across sub-periods (2000-02, 2008, 2015, 2018Q4, 2020, 2022).

## Verdict format
PASS / FAIL / NEEDS-WORK per gate, with numbers, N, and the evidence path. A failed holdout means **reject**, not re-tune.
