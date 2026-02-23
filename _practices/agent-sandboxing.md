---
title: "Agent Sandboxing"
stage: assess
category: Architecture & Delivery
description: "Isolating AI agents in secure, ephemeral environments (E2B, Docker) to prevent destructive shell commands or data exfiltration on developer machines."
strategic_value: supporting
devops_phases: [code, build, test]
---

## Overview

As we move from "Chat" to "Agents" (like Claude Code, Devin, or OpenHands) that have shell and file system access, the security risk increases. Agent sandboxing provides a secure execution environment where an agent can run code, execute shell commands, and access files without risking the host machine.

## When to Assess

- You are adopting agentic coding tools that require `write` or `shell` access.
- You are running autonomous agents in CI/CD pipelines.
- Security and compliance requirements mandate a "blast radius" for any automated execution.

## Core Technologies

- **Ephemeral VMs/Containers** — Tools like E2B or Docker that spin up a clean environment for every agent session.
- **Command Interceptors** — Guardrails that prompt for human approval or block specific dangerous commands (e.g., `rm -rf /`, `curl` to unknown domains).
- **WebAssembly (Wasm)** — Running agent-generated code in a highly restricted, platform-neutral sandbox.

## Risks & Considerations

- Performance overhead of spinning up fresh environments.
- Ensuring the sandbox has the necessary tools (compilers, runtimes, DBs) to be useful for the agent.
- Network isolation: agents may need access to internal APIs but must be blocked from public exfiltration.

## Resources

- [E2B — Sandboxing for AI Agents](https://e2b.dev/) — cloud-based SDK for running agents in secure, ephemeral environments.
- [OpenHands (OpenDevin) Sandboxing](https://github.com/All-Hands-AI/OpenHands) — how open-source agents handle execution safety.
- [OWASP LLM Security Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — focus on "Insecure Output Handling" and "Excessive Agency."
