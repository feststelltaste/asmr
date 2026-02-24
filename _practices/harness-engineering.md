---
title: "Harness Engineering"
stage: assess
category: Agentic AI Tools
description: "Designing structured environments, constraints, and automated feedback loops (the 'harness') that allow AI agents to operate reliably in complex codebases."
strategic_value: core
devops_phases: [plan, code, test, operate]
---

# Harness Engineering

## Problem

How do you design and maintain the "execution environment" that an AI agent needs to safely and reliably interact with a legacy codebase, including the tools, mocks, and feedback loops it needs to self-correct?

*This problem is difficult because:*

- Legacy systems are "brittle"—they have undocumented side effects, fragile build processes, and environmental dependencies that an agent can trigger unexpectedly.
- AI agents need "high-fidelity" feedback (compilers, test runners, linters, error logs) to be effective, but setting up these tools in a secure, isolated environment is a significant engineering challenge.
- Mocks and stubs in legacy systems are often out of sync with reality, leading an agent to "hallucinate" success in its sandbox while failing in production.
- Providing an agent with "too much power" (e.g., direct database access or network egress) is a high security risk, while "too little power" (e.g., no shell access) prevents it from being useful.

*Yet, solving this problem is feasible because:*

- Container and micro-VM technologies (Docker, E2B, Firecracker) provide fast, disposable environments that can be "pre-provisioned" with the legacy build tools an agent needs.
- Modern observability (OpenTelemetry) can capture every tool call and "thought" of an agent, providing the audit log needed to debug a failing harness.
- "Verification loops" can be integrated into the harness, forcing the agent to pass a full suite of tests before its proposed change is even presented to a human.

## Solution

Build a "harness" that surrounds the AI agent, providing it with the necessary tools and feedback while strictly constraining its impact on the system:

1. **Provision an ephemeral sandbox** — Use **Agent Sandboxing** to create a disposable, isolated environment (e.g., a Docker container or E2B micro-VM) for every agent session.
2. **Inject the "high-fidelity" tools** — Pre-install the compilers, test runners, and linters the agent needs to verify its own work. Ensure the environment matches the production environment as closely as possible.
3. **Define strict "verification loops"** — Configure the harness to automatically run a suite of **AI-Generated Characterization Tests** and unit tests every time the agent makes a change.
4. **Implement command guardrails** — Intercept and gate high-risk commands (e.g., database migrations or schema changes) on explicit human approval.
5. **Capture detailed observability** — Record all agent "thoughts," tool calls, and shell output to an audit log for debugging and forensic analysis.

**Core components of an agent harness:**

- **Deterministic Environments** — Ephemeral, reproducible sandboxes where agents can run code without side effects.
- **Verification Loops** — Automated test suites that the agent must pass before proposing a change.
- **Action Guardrails** — Rules that intercept and gate high-risk agent commands.
- **Observability** — Detailed logging of agent behavior and tool usage.

## Tradeoffs

**Pros:**

- Dramatically improves the reliability and "first-time quality" of agent-generated code.
- Reduces the risk of an agent causing "catastrophic damage" to a legacy system.
- Provides a consistent, auditable environment for all agentic modernization tasks.

**Cons:**

- Building a robust harness for a complex legacy system can be as much work as the modernization itself.
- Brittle mocks or environmental mismatches in the harness can lead to "false confidence" in the agent's work.

**Difficulties:**

- Replicating a complex legacy build environment (with archaic compilers and proprietary dependencies) inside a modern containerized sandbox.
- Balancing the agent's need for "real-world" data with the security requirements of data isolation and privacy.

## Rationale

Prompting an LLM to write code is only 20% of the job; the other 80% is the engineering work of making sure that code actually works in the context of a complex system. Harness engineering is the practice of building the "safety net" and "feedback loop" that allows a probabilistic AI agent to behave like a deterministic software engineer. It is the shift from "hoping" the AI is right to "proving" it is right within the constraints of a high-fidelity environment.

## Known Uses

- [E2B](https://e2b.dev/) — a cloud sandbox SDK built specifically for AI agents, providing ephemeral micro-VM environments for agentic coding.
- [OpenHands (formerly OpenDevin)](https://github.com/All-Hands-AI/OpenHands) — an open-source platform that includes a robust Docker-based harness for agentic tasks.
- [Devin by Cognition](https://cognition.ai/) — uses a proprietary "agent environment" that is a classic example of harness engineering.

## References

- [Martin Fowler — Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) — explores the concept of building environments for AI agents to operate in.
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg) — discusses the move from "vibes" to "harnesses" for reliable agentic work.

## Related Patterns

- **Agent Sandboxing** — the "primitive" layer of the harness; providing the isolation.
- **AI-Generated Characterization Tests** — the "verification" layer of the harness; proving the correctness of the work.
- **Agentic Coding Workflows** — the "operational" layer; defining how the agent uses the harness to complete its tasks.

## What Next

After building your first harness, apply **Agentic Coding Workflows** to begin running your first multi-step modernization tasks within that environment.

## Staging History

**Assess (Feb 2026):** Harness engineering is a critical but often overlooked part of the agentic stack. While the underlying tools (Docker, CI/CD) are mature, the specific discipline of building "agent-friendly" environments is new and evolving. Teams should assess their current environment's readiness for agentic automation before attempting broad rollout.
