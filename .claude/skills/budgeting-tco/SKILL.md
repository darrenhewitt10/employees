---
name: budgeting-tco
description: "Budget the project and compute total cost of ownership versus expected trading value, including break-even capital. Use for cost, budget or is-it-worth-it questions."
user-invocable: false
---
# Budgeting and total cost of ownership

## Cost categories (monthly)
Market data · LLM API tokens · hosting/VM · monitoring/alerts · broker fees and data add-ons · trading costs (spread, impact, commissions) · tax drag · owner time.

Default budget: **<= $150/month** for data + LLM + hosting (doc 12).

## Break-even check
`required_excess_return = annual_fixed_costs / capital`. Example: $1,800/yr costs on $20,000 capital needs +9%/yr **excess** return just to break even - unrealistic. State this explicitly for small accounts and recommend minimizing fixed costs (free data tiers, cached LLM calls) or using the passive benchmark.

## Report
Spend vs budget by category, trend, forecast, cost per strategy, net value (strategy P&L net of costs - benchmark P&L). Flag when costs exceed value for 3 consecutive months.
