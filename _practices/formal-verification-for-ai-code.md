---
title: "Formal Verification for AI Code"
stage: assess
category: AI Tooling Setup
description: "Using automated reasoning and mathematical proofs to ensure agent-generated refactorings are logically equivalent to the legacy code."
strategic_value: supporting
devops_phases: [test, build]
---

## Overview

In mission-critical systems, "passing the test suite" is not sufficient evidence that an AI agent hasn't introduced a subtle regression during modernization. Formal verification uses mathematical logic to prove properties about the code — for example, proving that a new Java implementation of a COBOL algorithm produces identical outputs for all possible inputs.

## Emerging Approaches

- **Symbolic Execution** — Tools that explore all possible paths through a function to find edge cases the agent missed.
- **Equivalence Checking** — Proving that the "before" and "after" states of a refactoring are logically identical.
- **LLM-guided Invariant Generation** — Using an agent to suggest the "rules" (invariants) that the code must follow, and then using a formal tool (like Z3 or Dafny) to prove they hold.

## When to Assess

- You are modernizing high-stakes logic (pricing engines, regulatory compliance, security protocols).
- Your legacy code lacks tests, making mathematical equivalence the only reliable safety net.
- You want to move toward "zero-defect" autonomous refactoring.

## Resources

- [Amazon — Using formal methods to verify code at scale](https://aws.amazon.com/blogs/opensource/formal-verification-at-scale/)
- [Dafny — A language for provably correct code](https://github.com/dafny-lang/dafny)
- [Microsoft Research — Z3 Theorem Prover](https://github.com/Z3Prover/z3)
