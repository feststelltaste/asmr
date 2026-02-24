---
title: "Agent Sandboxing"
stage: apply
category: AI Tooling Setup
description: "Executing AI agents within secure, ephemeral compute environments to prevent unintended shell side effects or data exfiltration when modifying fragile legacy systems."
strategic_value: supporting
devops_phases: [code, build, test]
---

## Problem

How can teams safely grant AI agents the shell and file system access they need to modernize code without risking destructive, irreversible changes to fragile legacy infrastructure?

*This problem is difficult because:*

- AI agents used for legacy modernization (e.g., Claude Code, Devin, OpenHands) require write access to files and shell access to compile, test, and run code — precisely the capabilities that can cause catastrophic damage in a legacy environment.
- Legacy codebases often contain undocumented scripts, fragile build processes, and environmental dependencies that an agent can trigger unexpectedly.
- A single misguided agent command (`rm -rf`, an unintended DB migration, a leaked credential) can cause irreversible damage to legacy data or host systems.
- Autonomous agents in CI/CD pipelines run unsupervised, increasing the blast radius of any logical or execution error.

*Yet, solving this problem is feasible because:*

- Container and micro-VM technologies have matured to provide fast, disposable environments at low cost.
- Specialized sandboxing SDKs (like E2B or Firecracker-based solutions) are emerging specifically to host agentic workloads.
- Command interception and approval layers can gate high-risk operations on human confirmation without blocking routine agent work.

## Solution

Run each agent session in an ephemeral, isolated environment that constrains the agent's impact on the host and the wider legacy network:

1. **Select an isolation primitive** based on your risk profile: Use ephemeral containers (Docker) for speed in trusted CI environments, or micro-VMs (E2B, Firecracker) for stronger multi-tenant isolation.
2. **Restrict network egress** to block arbitrary outbound connections that could exfiltrate legacy data or credentials, while allowing access to internal registries and necessary legacy APIs.
3. **Implement command interception** to require human approval for high-risk operations like database migrations, schema changes, or infrastructure scripts.
4. **Pre-provision the sandbox** with a mirror of the legacy build environment (compilers, runtimes, test runners, DB clients) to ensure the agent is not blocked by missing dependencies.
5. **Discard the environment after every task** to prevent state accumulation or "jailbreak" attempts from persisting across agent sessions.

## Tradeoffs

**Pros:**

- The blast radius of any agent error is strictly contained.
- Reproducible environments make agent behavior auditable.
- Compliance requirements for automated processes touching legacy infrastructure are more easily satisfied.

**Cons:**

- Spinning up fresh environments adds execution latency.
- Cloud-based sandboxes introduce external infrastructure dependencies.
- Replicating a complex legacy build environment within a sandbox requires significant upfront engineering.

**Difficulties:**

- Granular network isolation is difficult to configure correctly — agents need enough access to build against legacy systems but must be blocked from exfiltration.
- Agents may struggle to troubleshoot environment-related failures inside the sandbox if they lack the context to understand the isolation constraints.

## Rationale

Legacy systems are unpredictable by nature — they contain undocumented side effects, fragile scripts, and implicit dependencies that even experienced developers trigger accidentally. An AI agent operating in this environment without isolation is not just an operational risk; it is a modernization risk, since a destructive agent action can set back the migration effort significantly. Sandboxing applies the principle of least privilege to agents: grant only the access needed for the specific task, and ensure any failure is contained and reversible.

## Known Uses

- [OpenHands (formerly OpenDevin)](https://github.com/All-Hands-AI/OpenHands) — open-source agentic coding platform that publicly documents its sandboxing architecture; each agent session runs in an isolated Docker container with controlled file system and network access.

## References

- [E2B](https://e2b.dev/) — cloud sandbox SDK built specifically for AI agents; supports ephemeral micro-VM environments with fast spin-up for agentic coding workloads.
- [OWASP LLM Top 10 — Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — frames the security risks that sandboxing directly mitigates: unbounded tool use, unintended side effects, and data exfiltration.
- [Anthropic — Claude Code safety and permissions](https://docs.anthropic.com/en/docs/claude-code) — documents the built-in command interception model that gates high-risk tool use on explicit human approval.

## Related Patterns

- [Human in the Loop](../human-in-the-loop/) — complementary control; sandboxing limits what an agent can do autonomously, HITL review adds explicit checkpoints for high-stakes decisions in the legacy environment.
- [LLM Observability & Tracing](../llm-observability-and-tracing/) — sandboxed environments can capture complete audit logs of agent actions; observability tooling makes those logs useful for debugging when agent behavior on legacy code is unexpected.
- [Agentic Coding Workflows](../agentic-coding-workflows/) — sandboxing is a prerequisite for safely running agents against legacy systems at any meaningful scale.

## What Next

After assessing sandboxing options, apply [Human in the Loop](../human-in-the-loop/) to define which agent actions always require explicit human confirmation — particularly those that touch legacy databases, infrastructure scripts, or production-adjacent systems.

## Staging History

**Apply (Feb 2026):** Agent sandboxing has become a foundational security requirement for running autonomous agents in production-adjacent legacy environments. The maturity of micro-VM and container-based isolation has made it a reliable choice for preventing unintended side effects during agentic modernization.
