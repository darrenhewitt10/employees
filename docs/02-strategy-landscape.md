# 02 — Strategy Landscape

> **Purpose for agents:** The menu of strategy families that are realistic for a
> single-person, retail-scale, automated account — with evidence, typical
> holding periods, and failure modes. Quant Researcher and Risk agents own this.

## Selection principles

1. **Economic rationale first.** Prefer strategies with a known reason to work
   (risk premium, behavioral bias, structural flow, limits to arbitrage). Pure
   data-mined patterns rarely survive out of sample.
2. **Low-to-moderate turnover.** At retail scale we have no speed edge; costs
   and short-term tax rates punish high turnover.
3. **Capacity is not our constraint, latency is.** We can trade small and
   illiquid names institutions can't, but we cannot compete on microseconds.
4. **Published anomalies decay.** McLean & Pontiff (*Journal of Finance*, 2016)
   found anomaly returns are ~26% lower out of sample and ~58% lower after
   publication. Assume any textbook edge is weaker than its paper says.
5. **Multiple-testing haircut.** Harvey, Liu & Zhu (*Review of Financial
   Studies*, 2016) argue a new factor should clear t ≳ 3.0, not 2.0, given how
   many have been tried.

## Strategy families

| Family | Idea | Horizon | Evidence / notes | Main risks |
|---|---|---|---|---|
| **Passive core + rebalancing** | Hold diversified ETFs, rebalance on schedule/threshold | Months–years | The benchmark everything else must beat | Market drawdowns |
| **Time-series momentum / trend following** | Long assets trending up, flat/short those trending down (e.g., 12‑month return, moving-average filters) | Weeks–months | Moskowitz, Ooi & Pedersen (*JFE*, 2012) across 58 futures; works well on ETFs/futures | Whipsaw in choppy markets; long flat periods |
| **Cross-sectional momentum** | Long recent winners vs. losers among stocks | 1–12 months | Jegadeesh & Titman (1993); strong but crash-prone | Momentum crashes in sharp reversals |
| **Volatility targeting / risk parity** | Scale exposure inversely to recent volatility | Daily–weekly rebalance | Moreira & Muir (*JF*, 2017) "Volatility-Managed Portfolios" | Gap risk; vol regime shifts |
| **Factor tilts** (value, quality, low-vol, size) | Systematic tilts toward rewarded characteristics | Months | Large literature; long, painful underperformance spells | Factor crowding/decay |
| **Mean reversion / short-term reversal** | Fade extreme short-term moves (RSI, Bollinger, z-scores) | Days | Works in some regimes, especially liquid ETFs/large caps | Catching falling knives; high turnover costs |
| **Pairs / statistical arbitrage** | Trade spread between cointegrated assets | Days–weeks | Edge has decayed since 2000s; needs careful cost modeling | Relationship breakdown; short-borrow costs |
| **Event-driven** (earnings, PEAD, index changes) | Trade predictable post-event drift | Days–weeks | Post-earnings-announcement drift is long documented; weaker recently | Event data quality; crowding |
| **Text/NLP signals** (news, filings, transcripts) | LLM-scored sentiment or surprise | Hours–days | Lopez-Lira & Tang: real but decaying; strongest in small caps | Look-ahead bias; latency vs. faster players; cost in small caps |
| **Options income** (covered calls, cash-secured puts) | Harvest volatility risk premium | Weeks | Persistent VRP, but negatively skewed payoff | Tail losses; assignment mechanics |
| **Crypto trend/carry** | Trend following, funding-rate carry | Days–weeks | 24/7, high vol, fee-sensitive | Exchange/counterparty risk; extreme gaps |

**Avoid at our scale:** high-frequency market making, latency arbitrage, order
book microstructure scalping, and anything requiring co-location.

## Recommended starting portfolio of research ideas

Ordered by expected robustness and simplicity:

1. **Baseline:** passive ETF portfolio + periodic rebalance (benchmark).
2. **Trend filter on the baseline:** hold equities only when above a long-term
   moving average / positive 12‑month return; otherwise T-bills/bond ETF.
3. **Volatility targeting** overlay on (1)/(2).
4. **Multi-asset time-series momentum** across ~10–20 liquid ETFs.
5. **LLM text signal as a tilt** (not a standalone strategy): news/filings
   sentiment used to adjust weights within (4), measured strictly out of
   sample (post model training cutoff).

Each is cheap to test, low turnover, and gives the agent team a working
end-to-end pipeline before attempting anything exotic.

## Instrument universe considerations

- **ETFs:** Best starting universe — liquid, diversified, low single-name risk.
- **Single stocks:** Needed for cross-sectional and NLP strategies; requires
  survivorship-bias-free data and corporate-action handling
  ([04-market-data.md](04-market-data.md)).
- **Options:** Add only after equity pipeline is stable; requires Greeks,
  assignment handling, and broker options approval.
- **Futures:** Efficient for trend following, favorable US tax treatment
  (Section 1256), but leverage and margin need careful controls.
- **Crypto:** 24/7 ops burden, higher fees, exchange risk; treat as a separate
  sleeve with its own limits.

## Session hours note

Nasdaq and NYSE Arca are targeting **23×5 extended trading from
December 6, 2026** ([Harvard Law Forum, Oct 2026](https://corpgov.law.harvard.edu/2026/10/21/nyse-arca-and-nasdaq-to-launch-extended-trading-what-companies-should-consider/)).
Overnight liquidity will be thin initially; strategies should default to
regular-session execution unless overnight fills are explicitly modeled.
