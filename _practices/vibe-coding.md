---
title: "Vibe Coding"
stage: trial
category: Agentic AI Tools
description: "AI-first development where you describe intent in natural language and let the AI implement, then iterate on the result rather than writing code line by line."
strategic_value: core
devops_phases: [code]
---

## Overview

Coined by Andrej Karpathy in 2025, vibe coding is an AI-first programming style: you express *what* you want in natural language, the AI generates an implementation, and you iterate by describing what to change — rather than writing each line manually. You are the director; the AI is the implementer.

This is not about blindly accepting AI output. It's about working at a higher level of abstraction, spending your cognitive energy on architecture, correctness, and judgment rather than syntax.

## When It Works Best

- Prototyping and exploration — try an idea quickly without scaffolding overhead
- Repetitive transformations — "apply this pattern to all 40 of these files"
- Unfamiliar territory — let AI scaffold, then learn by reading and modifying
- Well-scoped tasks with clear acceptance criteria

## When It Doesn't Work

- Complex domain logic where precision matters and AI lacks context
- Security-critical code that must be understood line by line
- Tasks where the AI is consistently wrong and you spend more time correcting than coding

## Effective Patterns

- **Be specific about constraints**: "use no external libraries", "keep it under 50 lines", "handle errors explicitly"
- **Iterate in small steps**: don't ask for everything at once
- **Review everything**: vibe coding does not mean merging without reading
- **Feed failures back**: paste error messages and unexpected output directly into the chat

## Resources

- [Andrej Karpathy — "There's a new kind of coding I call 'vibe coding'"](https://x.com/karpathy/status/1886192184808149176) — the original post that named this
- [Ethan Mollick — One Useful Thing: Co-Intelligence](https://www.oneusefulthing.org/) — practical AI usage patterns for professionals
- [Simon Willison — AI-assisted programming](https://simonwillison.net/) — thoughtful coverage of what AI code generation actually means
- [YouTube — Vibe Coding with Cursor](https://www.youtube.com/results?search_query=vibe+coding+cursor+ai+2025)
