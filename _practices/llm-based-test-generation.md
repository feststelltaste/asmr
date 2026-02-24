---
title: "LLM-based Test Generation"
stage: trial
category: Agentic AI Tools
description: "Generating unit and integration tests from source code using LLMs. Dramatically improves coverage when adding tests to existing legacy code."
strategic_value: supporting
devops_phases: [test]
---

## Overview

LLMs can read a function or class and generate a set of unit tests covering happy paths, edge cases, and error conditions. This is especially valuable when modernizing legacy code that has little or no test coverage.

## Approaches

1. **IDE-based generation** — Ask Copilot/Cursor to generate tests for a selected function
2. **Agentic generation** — Agent reads a whole module and writes a full test file
3. **Mutation-guided** — Combine with mutation testing tools to identify gaps
4. **Characterization tests** — See [AI-generated Characterization Tests](/practices/ai-generated-characterization-tests/)

## When to Use

- Adding coverage to legacy code before refactoring
- Generating a starting point that developers then refine
- Accelerating TDD when writing tests first feels slower

## Risks & Considerations

- Generated tests may test the wrong thing — they reflect the code, not the intent
- Tests that just confirm existing (buggy) behavior give false confidence
- Always review and run generated tests before committing

## Resources

- [CodiumAI / Qodo — AI test generation](https://www.qodo.ai/) — purpose-built LLM test generation tool
- [Kent Beck — Exploring AI (TDD with AI)](https://tidyfirst.substack.com/p/exploring-ai) — practical AI-assisted TDD patterns
- [Diffblue Cover](https://www.diffblue.com/) — automated Java unit test generation
