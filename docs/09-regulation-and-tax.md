# 09 — Regulation and Tax (US)

> **Purpose for agents:** Rules the system must comply with and tax effects that
> change net returns. Compliance & Tax agent owns this. **This is research,
> not legal or tax advice** — the owner should confirm material decisions with
> a qualified professional. Assumes a US-resident individual trading their own
> money; revisit if that's wrong (see [12](12-decisions-needed.md)).

## Regulatory status

### Trading your own money with your own algorithm
- Generally **no registration** is required for an individual trading their
  own account through a registered broker, algorithmically or not.
- Trading **other people's money**, selling signals, or giving personalized
  advice can trigger **investment adviser** (SEC/state) or **CTA/CPO** (CFTC/NFA,
  for futures) registration. Keep the system strictly personal unless counsel
  approves otherwise.

### Market conduct rules that apply to bots
- **No manipulation:** spoofing/layering (placing orders intended to cancel),
  wash trading (trading with yourself), marking the close, and pump-and-dump
  are illegal regardless of whether a human or an algorithm does it. An LLM
  "deciding" to do it is still the owner's liability.
- The risk gateway should block self-crossing orders and excessive
  order-to-fill ratios.
- **Insider information / MNPI:** the system must not ingest non-public
  material information (e.g., from the owner's employer).

### Recent changes
- **PDT rule eliminated:** SEC approved FINRA Rule 4210 amendments
  (April 15, 2026) replacing the $25k pattern day trader framework with
  intraday margin requirements; broker implementation timing varies.
  ([FINRA RN 26‑10](https://www.finra.org/rules-guidance/notices/26-10))
- **SEC predictive data analytics proposal withdrawn** (June 12, 2025) along
  with 13 other proposals; it targeted broker/adviser conflicts from AI use and
  never applied to individuals trading their own accounts.
  ([Proskauer](https://www.proskauer.com/alert/sec-withdraws-fourteen-rule-proposals))
- **Extended hours:** 23×5 trading on Nasdaq/NYSE Arca targeted for
  Dec 6, 2026.
- **Settlement T+1** (since May 2024).

### Broker terms
Broker API agreements (Alpaca, IBKR, Schwab) and market data licenses impose
their own rules (rate limits, no redistribution of data, account-type
requirements). The system must respect them.

## Tax considerations (US federal)

| Topic | Rule | Impact on design |
|---|---|---|
| **Short- vs. long-term gains** | Assets held ≤ 1 year taxed at ordinary income rates; > 1 year at lower LTCG rates | High-turnover strategies face a large tax drag; backtests should report **after-tax** returns |
| **Wash sale rule (securities)** | Loss disallowed if substantially identical security bought within 30 days before/after the sale; loss added to the new lot's basis | Ledger must track lots and wash sales; automated rebuy can silently create wash sales, including across accounts (e.g., IRA) |
| **Section 1256 contracts** (regulated futures, broad-based index options) | 60% long-term / 40% short-term regardless of holding period; marked to market at year end | Tax-efficient vehicle for trend following |
| **Trader tax status + §475(f) mark-to-market election** | If the IRS considers you a trader in securities (substantial, frequent, continuous activity), you may elect MTM: gains/losses are ordinary, wash-sale rule doesn't apply, losses not capped at $3k. Election generally due by the original due date of the prior year's return | A decision for a tax professional; affects lot accounting |
| **Crypto** | Property; each trade/disposal is taxable. **Wash sale rule does not currently apply** — bills (reported as H.R. 9172, June 2026; PARITY Act draft) would extend it but were **not enacted** as of latest reporting. Brokers issue **Form 1099‑DA** (first required for 2025 transactions) | Track lots per exchange; monitor legislation |
| **Retirement accounts (IRA)** | No tax on trading inside the account; restrictions on margin/shorting; wash sales can still be triggered across taxable↔IRA | Running high-turnover strategies inside an IRA avoids tax drag but limits instruments |

Sources: [Thomson Reuters on crypto taxation](https://www.thomsonreuters.com/en-us/posts/tax-and-accounting/taxing-crypto-assets/),
[RSM digital asset tax alert (Sep 2026)](https://rsmus.com/insights/tax-alerts/2026/digital-asset-tax-reform-business-implications.html),
[Coin Center on crypto wash sales](https://www.coincenter.org/the-wash-sale-rule-would-break-crypto-tax-compliance/).

## Compliance requirements for the system

1. **Records:** keep every order, fill, cancel, decision record, and LLM input/
   output for at least 7 years (tax audits; reconstructing decisions).
2. **Tax lot ledger:** specific-lot identification support, wash-sale
   detection, year-end realized gain/loss report reconcilable to broker 1099s.
3. **Pre-trade compliance checks** in the risk gateway: no self-crossing,
   restricted-symbol list (e.g., owner's employer), order-to-fill ratio limits.
4. **Annual review** of rule changes (FINRA, SEC, IRS, state) by the
   Compliance agent, with a summary to the owner.
5. **Fraud hygiene:** never integrate third-party "AI bots" or signal sellers
   promising returns — CFTC/SEC have warned these are a common scam pattern.
