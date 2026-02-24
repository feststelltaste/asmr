---
title: "Formal Verification for AI Code"
stage: assess
category: AI Tooling Setup
description: "Using automated reasoning and mathematical proofs to ensure agent-generated refactorings are logically equivalent to the legacy code."
strategic_value: supporting
devops_phases: [test, build]
---

# Formal Verification for AI Code

## Problem

How do you ensure that an AI agent-generated refactoring is 100% logically equivalent to the original legacy code—especially in mission-critical systems where even a single subtle regression is unacceptable?

*This problem is difficult because:*

- Legacy systems often lack comprehensive test suites, and "passing the tests" is not sufficient evidence of correctness for high-stakes logic (e.g., pricing engines, regulatory compliance, security protocols).
- AI agents can produce code that is "plausibly correct" and passes all existing tests but contains subtle bugs in edge cases that the tests don't cover.
- Proving that two different implementations of the same logic are identical for all possible inputs is a mathematically complex task that exceeds human capabilities for non-trivial functions.
- Modernization often involves changing languages (e.g., COBOL to Java or C to Rust), which makes direct code comparison or "diffing" impossible.

*Yet, solving this problem is feasible because:*

- Formal verification tools (like Z3, Dafny, or symbolic execution engines) use mathematical logic to prove properties about the code and its equivalence.
- AI agents can be tasked with "invariant generation"—identifying the mathematical rules and constraints the code must follow—which can then be verified by a formal solver.
- Modern SMT (Satisfiability Modulo Theories) solvers can process millions of logical assertions in seconds, providing a level of certainty that testing alone can never reach.
- AI agents can be used to translate legacy code into formal specifications that can then be compared with the new implementation.

## Solution

Deploy formal verification and automated reasoning tools to mathematically prove the correctness of agent-generated refactorings:

1. **Identify "High-Stakes" Logic** — Select modules where the cost of a single regression is extremely high (e.g., a financial calculation or a security check).
2. **Generate Formal Specifications** — Use an AI agent to read the legacy code and generate a formal specification (e.g., in Dafny or a mathematical DSL) that describes its required behavior.
3. **Task the Agent with "Verified" Refactoring** — Instruct the agent to write the new implementation in a language that supports formal proofs (like Dafny or Spark Ada) or to include formal "assertions" in the target language.
4. **Run the Formal Solver** — Use a solver (like Z3) to prove that the new code satisfies the formal specification and is logically equivalent to the legacy version for all possible inputs.
5. **Use Symbolic Execution** — Run symbolic execution tools (like KLEE) to explore all possible paths through the new code and identify edge cases that were missed by both the human and the AI.

**Common formal verification techniques:**

- **Equivalence Checking** — Proving that the "before" and "after" implementations produce identical results for all possible inputs.
- **Model Checking** — Systematically exploring all possible states of a system to find violations of security or safety properties.
- **Invariant Proving** — Proving that certain rules (e.g., "The balance can never be negative") always hold true throughout the execution of the code.
- **Symbolic Execution** — Using symbolic values (rather than concrete inputs) to test every possible execution path through a function.

## Tradeoffs

**Pros:**

- Provides a "mathematical guarantee" of correctness for high-stakes modernization work.
- Catches subtle edge cases and "impossible" states that are missed by even the most thorough test suites.
- Enables autonomous refactoring in industries where human-level verification is too slow or too expensive.

**Cons:**

- Extremely high cognitive load: formal verification requires specialized expertise and is much harder to implement than unit testing.
- State space explosion: for very complex or stateful systems, the number of possible states can overwhelm even the fastest solvers.

**Difficulties:**

- Translating "messy" legacy code (with global state, side effects, and complex I/O) into a formal model that a solver can reason about.
- Keeping the formal specification in sync with the evolving business requirements.

## Rationale

In the era of autonomous AI agents, "it passes the tests" is no longer a high enough bar for mission-critical modernization. Agents are probabilistic; they can generate code that is 99% correct but 1% dangerous. Formal verification is the only technique that can turn a "probabilistic" agentic output into a "deterministic" software engineering result. It is the final safety net that allows for the safe automation of the most sensitive parts of our global infrastructure.

## Known Uses

- [Amazon Web Services (AWS)](https://aws.amazon.com/blogs/opensource/lean-into-verified-software-development/) — uses formal verification (automated reasoning) extensively to prove the security and correctness of their core cloud infrastructure.
- [Dafny](https://github.com/dafny-lang/dafny) — a verification-ready programming language that includes a built-in prover.
- [Z3 Theorem Prover](https://github.com/Z3Prover/z3) — a high-performance theorem prover from Microsoft Research used in many formal verification pipelines.

## References

- [Microsoft Research — Z3](https://github.com/Z3Prover/z3) — foundational tool for many SMT-based verification tasks.
- [KLEE — Symbolic Execution](https://klee-se.org/) — a symbolic execution tool built on LLVM.

## Related Patterns

- [AI-generated Characterization Tests](ai-generated-characterization-tests.md) — characterization tests provide a "best effort" safety net; formal verification provides a "proven" safety net.
- [Harness Engineering](harness-engineering.md) — formal verification is part of the "advanced harness" used to verify agentic output.
- [Agentic Coding Workflows](agentic-coding-workflows.md) — for high-stakes tasks, the agent's workflow must include a "verify with solver" step.

## What Next

After assessing your need for formal verification, start by applying it to a single, high-value function (like a tax calculation) before attempting to verify entire modules or services.

## Staging History

**Assess (Feb 2026):** Formal verification for AI-generated code is being assessed for mission-critical modernization tasks where testing is insufficient. The potential for 'zero-defect' refactoring is high, but the high specialized expertise and tooling required mean it is currently limited to high-stakes scenarios.
