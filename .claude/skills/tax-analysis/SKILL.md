---
name: tax-analysis
description: "Analyze US tax effects on trading: short vs long-term gains, wash sales, Section 1256, trader tax status and 475(f), crypto, IRAs, and after-tax returns. Use for any tax question or tax-aware design."
user-invocable: false
---
# Tax analysis (US federal; research, not tax advice)

| Topic | Rule | Design impact |
|---|---|---|
| Holding period | <= 1 year ordinary rates; > 1 year LTCG | High turnover = large tax drag; report after-tax returns |
| Wash sale (securities) | Loss disallowed if substantially identical bought within 30 days before/after; added to new lot basis; applies across accounts incl. IRA | Ledger tracks lots and wash sales; automated rebuys can trigger them |
| Section 1256 | Regulated futures/broad index options 60/40, MTM at year end | Tax-efficient trend following |
| Trader tax status + 475(f) | MTM election: ordinary gains/losses, no wash sales, no $3k loss cap; election generally due by original due date of prior year's return | Professional decision |
| Crypto | Property; each disposal taxable; wash sale currently not applicable (bills pending in 2026 - re-check); 1099-DA from brokers | Track lots per exchange |
| IRA | No tax on trades inside; limits on margin/shorting | Good home for higher-turnover sleeves |

## After-tax estimate
Apply the owner's marginal rates to realized short- and long-term gains per year; include wash-sale deferrals; compare to buy-and-hold's deferred-gain advantage.

Always recommend confirming material choices with a CPA/tax attorney.
