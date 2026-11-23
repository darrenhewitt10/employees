---
name: us-securities-regulation
description: "Apply US securities and derivatives rules to personal algorithmic trading: FINRA Rule 4210 intraday margin, manipulation prohibitions, adviser/CTA registration triggers, settlement and session changes. Use for any regulatory question."
user-invocable: false
---
# US securities regulation (research, not legal advice)

## Personal trading
- An individual trading their **own** account through a registered broker generally needs no registration, algorithmic or not.
- Trading others' money, selling signals or giving personalized advice can trigger **investment adviser** (SEC/state) or **CTA/CPO** (CFTC/NFA) registration. Default: personal only; counsel must approve anything else.

## Conduct rules that bind bots
Spoofing/layering, wash trading (trading with yourself), marking the close, pump-and-dump are illegal whoever (or whatever) does it; the owner is liable for an algorithm's behavior. No material non-public information (e.g. from the owner's employer).

## Recent changes (verify effective dates)
- **PDT rule replaced:** SEC approved FINRA Rule 4210 amendments on **Apr 15 2026** - no $25k minimum or 4-in-5-days test; risk-based intraday margin instead; broker implementation timing varies (FINRA RN 26-10).
- **SEC predictive data analytics proposal withdrawn** Jun 12 2025 (never applied to individuals' own accounts).
- **T+1 settlement** since May 2024 (cash accounts: avoid good-faith/free-riding violations).
- **23x5 trading** on Nasdaq/NYSE Arca targeted Dec 6 2026.
- CFTC and SEC/NASAA/FINRA warn that "AI bots" promising high or guaranteed returns are a common fraud pattern.

Recommend a securities lawyer for anything beyond personal trading.
