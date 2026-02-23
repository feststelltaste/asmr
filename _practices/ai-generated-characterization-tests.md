---
title: "AI-generated Characterization Tests"
stage: apply
category: Legacy Modernization
description: "Using LLMs to generate 'golden master' tests from existing behavior before refactoring. Makes safe modernization possible when there are no existing tests."
strategic_value: core
devops_phases: [test]
---

## Overview

Characterization tests (also called golden master tests) capture the *current* behavior of code — right or wrong — and make it detectable when that behavior changes. They are the safety net for refactoring untested legacy code. LLMs can now generate these tests quickly by reading the code.

## How It Works

1. Point an LLM at a legacy function or module
2. Ask it to generate tests that call the code with representative inputs and assert on current outputs
3. Run the tests to capture baseline behavior
4. Refactor with confidence — any change in behavior triggers a test failure
5. Gradually replace characterization tests with proper unit tests as you understand the domain

## Related Concept

Michael Feathers coined characterization testing in *Working Effectively with Legacy Code* (2004). LLMs make the test generation step dramatically faster.

## Risks & Considerations

- Characterization tests codify bugs as well as correct behavior — don't treat them as specifications
- Output-sensitive tests (dates, random values, IDs) need special handling
- Works best for pure functions; stateful or I/O-heavy code requires more setup

## Resources

- [Michael Feathers — Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — the original book introducing characterization tests
- [Approval Tests library](https://approvaltests.com/) — framework specifically built for golden master / characterization testing
