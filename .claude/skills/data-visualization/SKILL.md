---
name: data-visualization
description: "Design dashboards and charts that make risk and performance clear at a glance. Use when building reports, dashboards or approval screens."
user-invocable: false
---
# Data visualization

## Standard views
- **Equity curve** vs benchmark (log scale for long periods), with **drawdown** chart underneath.
- **Exposure** over time (gross/net, by asset class or sector) as stacked area.
- **Limits gauge:** each risk metric as % of its limit, colored by threshold (ok / 80% / breach).
- **Live vs backtest** overlay for the same period.
- **Costs:** realized vs modeled slippage over time.
- Tables for positions and orders; sortable.

## Principles
- Lead with the answer (status: OK / ATTENTION / HALTED).
- One idea per chart; label axes and units; show the period and data source.
- Color: consistent semantic colors; accessible contrast; works in light and dark mode; don't encode meaning by color alone.
- No 3D, no dual axes unless unavoidable.
- Approval screens show what will change, the risk impact, and require an explicit confirm.
