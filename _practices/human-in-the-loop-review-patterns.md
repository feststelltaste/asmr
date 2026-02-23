---
title: "Human-in-the-loop (HITL) Review Patterns"
stage: apply
category: Agentic AI Tools
description: "Patterns for effectively reviewing agent-generated code — focusing on architectural intent and edge cases rather than syntax."
strategic_value: core
devops_phases: [code, test]
---

## Overview

As AI agents move from single-line completions to generating whole features or refactoring entire modules, the traditional code review process becomes a bottleneck. HITL Review Patterns define a new collaboration model where the human reviewer acts as a high-level architect rather than a line-by-line editor.

## Core Patterns

- **Architectural Checkpoints** — Reviewing the agent's *plan* (markdown or diagram) before it writes any code.
- **Review-Only Sub-agents** — Using a second, independent agent to perform a first pass of the code review, flagging obvious bugs or style violations for the human.
- **Verification-First Review** — Instead of reading the code first, the reviewer reads the *tests* the agent generated to ensure the intent was understood correctly.
- **Critique-and-Refine Loop** — Giving high-level feedback ("this is too coupled," "use the repository pattern here") and letting the agent perform the tedious mechanical changes.

## Why It Matters

- **Scalability** — Humans cannot keep up with the volume of code an agent can produce using traditional review methods.
- **Quality** — Prevents "reviewer fatigue" where humans start blindly clicking 'Approve' on large AI-generated PRs.
- **Skill Shift** — Shifts the developer's value from "knowing the syntax" to "knowing the system and its constraints."

## Resources

- [Anthropic — Building effective agents: Human-in-the-loop](https://www.anthropic.com/research/building-effective-agents)
- [Hacker News — The future of code review in an AI world](https://news.ycombinator.com/item?id=41567890)
