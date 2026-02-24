---
title: "AI-generated Characterization Tests"
stage: apply
category: Legacy Modernization
description: "Using LLMs to generate 'golden master' tests from existing behavior before refactoring. Makes safe modernization possible when there are no existing tests."
strategic_value: core
devops_phases: [test]
---

# AI-Generated Characterization Tests

## Problem

How do you safely refactor or replace legacy code that has no test coverage and whose full behavior cannot be understood from reading the source alone?

*This problem is difficult because:*

- Legacy codebases often have zero test coverage for critical paths — the original authors relied on manual testing or never wrote tests at all.
- Reading the code is insufficient: years of implicit behavior (special cases, silent error suppression, undocumented rounding) is invisible until something breaks.
- Without a safety net, every refactoring step is a gamble — and AI agents making autonomous changes to untested code amplify this risk dramatically.

*Yet, solving this problem is feasible because:*

- LLMs can read a legacy function and generate test cases that call it with varied inputs and assert on its current outputs, capturing behavior without requiring the developer to understand it first.
- Generating mechanical test coverage is exactly the repetitive, pattern-following work where AI agents outperform humans in speed while requiring little domain knowledge.

## Solution

Use an AI coding agent to generate characterization tests — also called golden master tests — before any modernization change is made:

1. **Identify the target unit** — select a function, class, or module that must change. Prefer units with clear inputs and outputs.
2. **Generate tests against current behavior** — prompt an agent to call the code with diverse inputs and assert on whatever the code currently produces, right or wrong.
3. **Run and commit the baseline** — confirm all generated tests pass against the unchanged code, then commit them as the refactoring safety net.
4. **Modernize under the net** — make the change; any deviation from captured behavior immediately causes a failure.
5. **Replace incrementally** — as domain understanding grows, swap characterization tests for intentional unit tests that assert on correct behavior rather than current behavior.

## Tradeoffs

**Pros:**

- Provides a refactoring safety net in minutes rather than days for untested legacy code.
- Once in place, AI agents can make further autonomous changes with the characterization tests as a guard rail.
- No domain knowledge required to generate the initial suite — the agent reads the code, not the requirements.

**Cons:**

- Characterization tests codify bugs alongside correct behavior and must not be treated as a specification.
- Test quality depends on input diversity — an agent may miss edge cases that only appear in production data.

**Difficulties:**

- Output-sensitive code (timestamps, random IDs, external calls) requires manual wrapping or mocking before tests can be stabilized.
- Agents tend toward happy-path inputs; prompting explicitly for boundary conditions and error paths is necessary for useful coverage.

## Rationale

Autonomous AI agents changing legacy code without a test harness is the highest-risk combination in modernization work. Characterization tests change the economics: an agent can generate them faster than any human, and once in place they make subsequent agentic changes safe and auditable. This practice is the prerequisite that unlocks confident agentic refactoring — not a nice-to-have, but the foundation the rest of the agentic workflow depends on.

## Known Uses

- [Diffblue Cover — automated Java test generation](https://www.diffblue.com/products/) — generates characterization tests for legacy Java codebases automatically; adopted by large financial institutions to establish baseline coverage before modernization programs.

## References

- [Michael Feathers — *Working Effectively with Legacy Code*](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — introduced characterization testing as the primary technique for safely modifying untested legacy code; the conceptual foundation for this practice.
- [Approval Tests](https://approvaltests.com/) — a test framework built specifically for golden master / characterization testing; useful when AI-generated assertions need a structured output-comparison mechanism.

## Related Patterns

- [Harness Engineering](harness-engineering.md) — characterization tests are the inner loop of a broader test harness; this practice provides the automated safety net that makes the harness trustworthy.
- [Agentic Coding Workflows](agentic-coding-workflows.md) — agents making autonomous refactoring changes depend on characterization tests as their guard rail; this practice is a prerequisite for safe agentic operation on legacy code.
- [Human in the Loop](human-in-the-loop.md) — reviewing AI-generated characterization tests before committing is a critical checkpoint; a missed edge case in the baseline propagates silently into every subsequent change.

## What Next

With a characterization test baseline in place, apply [Agentic Coding Workflows](agentic-coding-workflows.md) to begin autonomous refactoring — the agent now has a safety net it can run after every change.

## Staging History

**Apply (Feb 2026):** AI-assisted characterization test generation is well-validated in practice and directly addresses the most dangerous gap in agentic legacy modernization: agents changing untested code. The underlying technique is proven; LLMs make the generation step fast enough to apply routinely. Immediate adoption is recommended for any team running agents against a legacy codebase.
