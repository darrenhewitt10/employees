---
name: contract-license-review
description: "Review broker agreements, market-data licenses, API terms and LLM provider terms for obligations, restrictions and risks. Use before adopting or changing any vendor or data use."
user-invocable: false
---
# Contract and license review (research, not legal advice)

## Checklist
- **Use rights:** personal vs professional subscriber status; display vs non-display (algorithmic) use; derived data rights.
- **Redistribution:** can data or derived outputs be shared, published, or shown on a website (e.g. the Netlify docs site)? Default: no vendor data published.
- **API terms:** rate limits, automated-trading permissions, prohibited uses, key handling.
- **LLM providers:** data retention, use of inputs for training, confidentiality of prompts, model deprecation notice periods.
- **Liability and indemnity:** who bears losses from outages or errors.
- **Termination/exit:** notice periods, data deletion, export rights.
- **Privacy:** what personal/account data leaves the system.
- **Fees:** auto-renewals, overage charges, exchange fees passed through.

## Output
Table: clause -> what it says -> risk (high/med/low) -> required action. Flag anything that blocks the planned use and route to securities-regulatory-counsel or the owner.
