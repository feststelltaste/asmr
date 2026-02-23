---
title: "Context Engineering"
stage: apply
category: Agentic AI Tools
description: "Designing the information environment for AI agents — project rules files, architecture docs, and conventions that help AI understand your codebase and produce better output."
strategic_value: core
devops_phases: [plan, code]
---

## Overview

The quality of AI-generated code is determined as much by the *context* you provide as by the model itself. Context engineering is the practice of deliberately crafting the information environment in which AI agents operate: project rules, architecture summaries, coding conventions, glossaries, and examples.

In agentic setups, this is the difference between an agent that confidently does the right thing and one that makes plausible but wrong decisions repeatedly.

## Key Artefacts

**Project rules file** (`CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`)
- Project-specific conventions the agent should always follow
- Technology choices and patterns that are established
- Anti-patterns to avoid in this codebase
- How to run tests, build, and verify changes

**Architecture summary**
- High-level description of bounded contexts, key services, and data flows
- Placed in the project root or embedded in the rules file

**Glossary of domain terms**
- Domain-specific terminology so the AI uses the right names in generated code

**Example code snippets**
- Representative examples of how things are done in this project (the right way)

## Practices

- Keep rules files concise — long files get diluted; focus on what's most unique about your project
- Version control all context artefacts alongside the code they describe
- Update context when patterns change — stale context misleads agents
- Layer context: global rules + per-directory rules for large monorepos

## Resources

- [Anthropic — CLAUDE.md best practices](https://docs.anthropic.com/en/docs/claude-code/memory) — official guidance on project memory files
- [Cursor rules documentation](https://docs.cursor.com/context/rules-for-ai) — how to write effective `.cursorrules`
- [YouTube — Context Engineering for AI Coding](https://www.youtube.com/results?search_query=context+engineering+ai+coding+agents+2025)
- [Philipp Schmid — Prompt Engineering Guide](https://www.philschmid.de/prompt-engineering-llms) — practical patterns for shaping LLM behavior
