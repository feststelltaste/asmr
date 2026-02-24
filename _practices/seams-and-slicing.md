---
title: "Seams and Slicing"
stage: apply
category: Legacy Modernization
description: "Identifying and exploiting 'seams' to break dependencies and extracting vertical 'slices' of functionality to make legacy code testable and refactorable by agents."
strategic_value: core
devops_phases: [plan, code, test]
---

# Seams and Slicing

## Problem

How do you break the tight coupling of a legacy codebase to enable automated testing and refactoring without performing a high-risk, large-scale rewrite of the entire module?

*This problem is difficult because:*

- Legacy systems are often "tangled"—classes and functions have hardcoded dependencies on databases, file systems, or global state that make them impossible to run in isolation.
- Traditional refactoring requires tests, but you can't add tests until you break the dependencies, creating a "chicken-and-egg" paradox.
- Manual dependency breaking is tedious: a single "new" or static call deep in a hierarchy can block the testing of an entire business process.
- AI agents making changes to un-seamed code are highly likely to trigger unexpected side effects that aren't captured by a local test suite.

*Yet, solving this problem is feasible because:*

- Michael Feathers' concept of a **Seam**—a place where you can alter behavior without editing in that place—provides a surgical way to "un-stick" code.
- AI agents are excellent at identifying "link seams" (changing which files are compiled) and "object seams" (extracting interfaces) across a large codebase.
- Agents can autonomously perform the mechanical work of "Slicing"—identifying a vertical path of execution and extracting only the necessary parts into a testable unit.

## Solution

Task your AI agents to identify seams and extract functional slices to create a refactoring safety net:

1. **Identify the Seams** — Use an agent to scan a module for hardcoded dependencies (static calls, `new` keywords). Task it to find "object seams" (e.g., where a class can be replaced by an interface).
2. **Exploit the Seam** — Instruct the agent to perform a "Dependency Breaking" refactor: extract an interface for the dependency and use Constructor Injection to allow a mock to be passed in.
3. **Define the Slice** — Identify a specific business capability (e.g., "Calculate Discount"). Use **AI-assisted Codebase Analytics** to find every line of code involved in that vertical "slice."
4. **Extract the Slice** — Task an agent to move that slice into a new, independent module, redirecting the old call sites to the new implementation via the seam.
5. **Add the Harness** — Once the seam exists, use **LLM-based Test Generation** to inject mocks and build a comprehensive unit test suite around the extracted slice.

**Types of Seams for Agents:**

- **Object Seams** — Using polymorphism and interfaces to swap implementations (the most common).
- **Link Seams** — Changing build configurations to use a different file/library during testing.
- **Preprocessing Seams** — Using macros or compiler flags to redirect calls (common in C/C++).

## Tradeoffs

**Pros:**

- Allows for "surgical" modernization: you only touch what you need to change.
- Unlocks automated testing for code that was previously considered "untestable."
- Dramatically reduces the risk of agent-driven refactoring by providing a clear isolation boundary.

**Cons:**

- Creating too many seams can lead to "abstraction bloat," making the code harder for humans to follow.
- If not managed carefully, slicing can leave "orphaned" code fragments in the legacy system.

**Difficulties:**

- Identifying the *best* seam to exploit in a deeply nested call hierarchy.
- Handling "invisible" dependencies like shared global variables or database triggers.

## Rationale

Modernization projects often fail because they try to fix everything at once. **Seams and Slicing** allow for incrementalism. For an AI agent, a seam is like a "leverage point": it gives the agent a place to stand where it can move the world without breaking it. By focusing on breaking dependencies first, you create the environment where agents can operate with the same confidence as a senior human developer.

## Known Uses

- [Michael Feathers — Working Effectively with Legacy Code](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — the foundational text that defined these concepts.
- [OpenRewrite](https://docs.openrewrite.org/) — recipes often automate the extraction of interfaces to create object seams.

## References

- [Michael Feathers — "Seams"](https://www.informit.com/articles/article.aspx?p=359417&seqNum=2) — a deep dive into the types of seams and how to find them.
- [Vertical Slice Architecture](https://jimmybogard.com/vertical-slice-architecture/) — a modern architectural pattern that builds on the concept of functional slicing.

## Related Patterns

- [Harness Engineering](harness-engineering.md) — seams are the "brackets" that hold the harness in place.
- [AI-generated Characterization Tests](ai-generated-characterization-tests.md) — characterization tests prove the slice is correct; seams allow you to run those tests.
- [Anti-Corruption Layer](anti-corruption-layer.md) — an ACL is often the permanent architectural implementation of an exploited seam.

## What Next

After identifying your first seam, apply [Harness Engineering](harness-engineering.md) to build the automated feedback loop around that specific functional slice.

## Staging History

**Apply (Feb 2026):** Seams and slicing are foundational techniques for legacy work. In the agentic era, they are the primary "maneuvers" used to make code safe for AI-driven transformation. Immediate adoption is recommended for any team touching coupled legacy code.
