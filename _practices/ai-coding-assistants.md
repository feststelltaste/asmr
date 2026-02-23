---
title: "AI Coding Assistants"
stage: apply
category: Agentic AI Tools
description: "GitHub Copilot, Cursor, Windsurf — AI pair-programming that accelerates writing, refactoring, and understanding of existing code."
strategic_value: supporting
devops_phases: [code]
---

## Overview

AI coding assistants embed LLM capabilities directly into the IDE, providing inline completions, chat-based Q&A about code, and whole-function generation. They are now a proven productivity multiplier for most development tasks.

## Key Tools

| Tool | Vendor | Strength |
|------|--------|----------|
| GitHub Copilot | GitHub / Microsoft | Broadest IDE support, team management |
| Cursor | Cursor Inc. | Deep codebase context, multi-file edits |
| Windsurf | Codeium | Fast, free tier, agentic flows |
| JetBrains AI | JetBrains | Native integration with JetBrains IDEs |

## When to Use

- Accelerating routine code (boilerplate, CRUD, tests)
- Understanding unfamiliar legacy code quickly
- Generating first drafts of documentation or migration scripts

## Core Collaboration Patterns

- **Prompt-then-review loop** — Describe intent → review output → refine. Never accept on the first pass for non-trivial code.
- **Write the tests first** — Describe expected behavior or write unit tests, then let the AI implement. This gives you a correctness check you control.
- **Scaffold with AI, own the logic** — Use AI for boilerplate and data wiring; write the core domain logic yourself.
- **Paste errors directly** — Paste the full error message and stack trace back into the conversation for better AI responses.
- **Ask for explanations** — "Explain what this function does and any risks" catches issues that a silent review might miss.
- **Reject and re-ask** — Don't fix AI output line by line. Say "this is wrong because X — try again" and let it regenerate.

## Anti-patterns

- **Merge without reading** — AI code must be reviewed as carefully as any other PR.
- **Accepting hallucinated APIs** — Verify every method and import the AI uses actually exists.
- **Over-prompting** — Giant prompts often produce worse results than focused, sequential prompts.

## Risks & Considerations

- **Hallucinations**: Generated code must be reviewed — LLMs confidently produce plausible-looking but wrong code
- **Over-reliance**: Junior developers may skip learning fundamentals
- **IP / data privacy**: Check whether code is sent to third-party servers; use self-hosted models for sensitive IP

## Resources

- [GitHub Copilot documentation](https://docs.github.com/en/copilot) — official guide and feature reference
- [Cursor — the AI-first code editor](https://www.cursor.com/) — homepage and docs
- [Kent Beck — "Taming the AI"](https://tidyfirst.substack.com/p/taming-the-ai) — practical patterns for AI-assisted TDD
- [Harper Reed — My AI Pair Programming Setup](https://harperreed.com/posts/2024-07-16-my-llm-codegen-workflow/) — real-world workflow
- [Simon Willison — AI-assisted programming](https://simonwillison.net/tags/ai-assisted-programming/) — ongoing critical analysis

