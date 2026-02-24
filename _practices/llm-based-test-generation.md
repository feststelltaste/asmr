---
title: "LLM-based Test Generation"
stage: trial
category: Agentic AI Tools
description: "Generating unit and integration tests from source code using LLMs. Dramatically improves coverage when adding tests to existing legacy code."
strategic_value: supporting
devops_phases: [test]
---

# LLM-based Test Generation

## Problem

How do you rapidly increase the unit and integration test coverage for a massive legacy codebase that currently has little or no automated testing, making any modernization change a high-risk gamble?

*This problem is difficult because:*

- Writing tests for legacy code is often tedious and time-consuming: a developer might spend more time writing the test than they would spend refactoring the code.
- Legacy code is often "hard to test"—it has global state, tight coupling, and hardcoded dependencies that require extensive mocking and setup.
- The original authors are gone, and the intended behavior of the code is often unclear, making it hard to know what to "assert" in a test.
- "Manual testing" is the norm in many legacy environments, leading to slow release cycles and frequent production regressions.

*Yet, solving this problem is feasible because:*

- LLMs can read a function or class and generate a suite of unit tests that cover happy paths, edge cases, and common error conditions in seconds.
- AI agents can autonomously identify and mock the external dependencies (databases, APIs, static methods) needed to make legacy code testable in isolation.
- Test generation is a repetitive, "pattern-following" task that LLMs are highly effective at, even without deep domain knowledge of the specific business rule.
- Generating mechanical test coverage is exactly the kind of "high-volume, low-risk" work that AI can handle better and faster than a human.

## Solution

Deploy an AI-powered test generation pipeline to systematically build a safety net for your legacy codebase:

1. **Target the "Core Logic" first** — Use **AI-assisted Codebase Analytics** to identify the most critical and most frequently changed modules.
2. **Generate "Baseline" Unit Tests** — Task an LLM or a specialized agent (like CodiumAI or Diffblue) to read the source code and generate tests for its *current* behavior.
3. **Automate the "Mocking" process** — Use the agent to identify and generate mocks for the external dependencies (e.g., database calls, network requests) that make the code hard to test.
4. **Iterate and Refine** — Run the generated tests; if they fail, provide the error output to the agent and let it iterate on the fix (autonomous debugging).
5. **Human review for "Intent"** — Have a human developer review the generated tests to ensure they are testing the *correct* behavior, not just codified legacy bugs.

**Common test generation approaches:**

- **Characterization Testing** — Capturing current behavior (right or wrong) as a refactoring safety net (see **AI-Generated Characterization Tests**).
- **Unit Test Generation** — Building isolated tests for individual functions and classes.
- **Integration Test Generation** — Using AI to draft the setup and teardown for complex, multi-service workflows.
- **Mutation-guided testing** — Combining AI generation with mutation testing to find and fill the gaps in the current test suite.

## Tradeoffs

**Pros:**

- Dramatically compresses the time and cost required to build a testing safety net for legacy code.
- Ensures a more consistent and comprehensive set of tests (happy paths + edge cases) than a human often has the patience to write.
- Allows for the safe, automated refactoring of legacy code that was previously considered "untouchable."

**Cons:**

- "Plausible but wrong" assertions: the AI may assert on incorrect behavior if the source code itself is buggy.
- "Mock-heavy" tests can become brittle and detached from the real-world behavior of the system.

**Difficulties:**

- Setting up the test harness (compilers, test runners, mocking libraries) so the AI can actually run and verify its generated tests.
- Preventing "test bloat"—generating thousands of low-value tests that slow down the CI/CD pipeline without providing real protection.

## Rationale

Testing is the "engine" of modernization. Without it, the risks of change are too high to attempt at scale. AI-based test generation changes the economics of testing: it turns a "human-intensive" activity into an "AI-intensive" one, allowing teams to build a comprehensive safety net in days rather than months. This is the prerequisite that unlocks the power of all other agentic modernization practices.

## Known Uses

- [CodiumAI / Qodo](https://www.qodo.ai/) — a purpose-built platform for using LLMs to generate high-quality unit and integration tests.
- [Diffblue Cover](https://www.diffblue.com/) — an automated Java unit test generation tool that uses reinforcement learning and LLMs to build test suites.
- [Symflower](https://symflower.com/) — a tool that uses symbolic execution and AI to generate tests that cover all possible execution paths.

## References

- [Kent Beck — Exploring AI (TDD with AI)](https://tidyfirst.substack.com/p/exploring-ai) — explores the impact of AI on the traditional Test-Driven Development (TDD) workflow.
- [Michael Feathers — Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — the classic text on the importance of building a test harness before making changes.

## Related Patterns

- **AI-Generated Characterization Tests** — the most critical "first step" in legacy test generation.
- **Harness Engineering** — the harness is what allows the AI-generated tests to run and verify the codebase.
- **Agentic Coding Workflows** — test generation is a primary task for an agentic workflow during the initial phase of modernization.

## What Next

After generating your first "baseline" of tests, apply **AI-Generated Characterization Tests** to your most critical modules to create a durable refactoring safety net.

## Staging History

**Trial (Feb 2026):** AI-based test generation is a powerful tool for any modernization team. While the quality of generated tests is high, they must still be reviewed by a human expert to ensure they align with the business's intent, not just the code's current behavior. Start with low-stakes modules to tune your generation prompts.
