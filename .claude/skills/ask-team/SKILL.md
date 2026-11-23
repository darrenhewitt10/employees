---
name: ask-team
description: "Ask the whole expert team a question: the orchestrator picks the right experts, has them work together and returns one combined answer. Usage: /ask-team [question]"
context: fork
agent: orchestrator
background: false
disable-model-invocation: true
argument-hint: "[question]"
---
Use the expert team to answer this question:

$ARGUMENTS

Follow your orchestrator procedure: route with the expert-routing skill, consult the chosen experts (in parallel where independent), resolve disagreements with the multi-expert-synthesis rules, and return one combined answer in the synthesis format.
