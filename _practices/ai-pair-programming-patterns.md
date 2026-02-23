---
title: "AI Pair Programming Patterns"
stage: apply
category: Agentic AI Tools
description: "Proven patterns for collaborating effectively with AI coding assistants — when to lead, when to delegate, and how to review AI-generated code critically."
strategic_value: core
devops_phases: [code]
---

## Overview

Working with an AI coding assistant is not just autocomplete at scale. It requires a new collaboration style: knowing when to describe intent vs. write code yourself, how to give feedback when output is wrong, and how to critically review generated code without getting anchored on the AI's first attempt.

## Core Patterns

### Prompt-then-review loop
Describe intent → review output → refine. Never accept on the first pass for non-trivial code. The AI's first output is a draft, not a solution.

### Write the tests first, let AI fill the implementation
Write unit tests (or at least describe expected behavior in precise terms), then let the AI implement. This gives you a correctness check you control.

### Use AI for the scaffolding, own the domain logic
AI is excellent at writing boilerplate, data wiring, and routine transformations. Own and write the core domain logic yourself so you understand it.

### Paste errors directly
When the AI's code fails, paste the full error message and stack trace back into the conversation. Don't describe the error — show it. AI responds much better to concrete failures.

### Ask for explanations, not just code
"Explain what this function does and any risks" catches issues that a silent review might miss.

### Reject and re-ask when output is wrong
Don't try to fix AI output line by line. Say "this is wrong because X — try again" and let the AI regenerate from the constraint.

## Anti-patterns

- **Merge without reading** — AI code must be reviewed as carefully as any other PR
- **Accepting hallucinated APIs** — Verify every method and import the AI uses actually exists
- **Over-prompting** — Giant prompts often produce worse results than focused, sequential prompts

## Resources

- [Kent Beck — "Taming the AI"](https://tidyfirst.substack.com/p/taming-the-ai) — practical patterns for AI-assisted TDD
- [Harper Reed — My AI Pair Programming Setup](https://harperreed.com/posts/2024-07-16-my-llm-codegen-workflow/) — real-world workflow
- [YouTube — AI Pair Programming Best Practices](https://www.youtube.com/results?search_query=ai+pair+programming+patterns+best+practices+2025)
- [Alistair Cockburn — Pair Programming Illuminated](http://www.pairprogrammingillumanated.com/) — foundational pair programming principles that translate to human-AI pairs
