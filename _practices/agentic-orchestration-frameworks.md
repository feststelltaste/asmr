---
title: "Agentic Orchestration Frameworks"
stage: trial
category: AI Tooling Setup
description: "LangGraph, CrewAI, AutoGen — frameworks for multi-step, multi-agent pipelines. Useful but often add complexity; consider starting without them."
strategic_value: supporting
devops_phases: [code, build]
---

# Agentic Orchestration Frameworks

## Problem

How do you coordinate multiple LLM-based agents, manage their shared state, and implement complex multi-step reasoning without building a custom state machine from scratch for every task?

*This problem is difficult because:*

- Complex modernization workflows (e.g., plan → refactor → test → review → fix) involve non-linear branching and decision-making that is difficult to manage with simple sequential LLM calls.
- Agents need persistent memory and shared context across long-running tasks, which becomes brittle when manually passed through nested function calls and prompt templates.
- Debugging "agentic loops" is inherently difficult; without a structured framework, identifying where a multi-step process went wrong is a significant engineering challenge for any team.
- Legacy modernization often requires specialized agents (e.g., a "COBOL expert" and a "Java expert") to collaborate on a single task, which requires a robust handoff mechanism.

*Yet, solving this problem is feasible because:*

- Dedicated orchestration frameworks have emerged that provide standardized primitives (graphs, roles, state containers) for state management and tool routing.
- These frameworks offer built-in observability and tracing, making it possible to visualize and debug the "thinking process" of a multi-agent system.

## Solution

Utilize an orchestration framework to define the control flow and coordination logic for your AI agent teams:

1. **Select a framework based on your workflow pattern** — Use **LangGraph** for complex, stateful graphs; **CrewAI** for role-based multi-agent teams; or **AutoGen** for conversational agent interactions.
2. **Define the agent roles and tools** — Explicitly bound each agent's capabilities and the specific tools (shell, file system, APIs) they can access within the workflow.
3. **Model the state machine** — Map out the transitions between agents, including failure paths and human-in-the-loop checkpoints, using the framework's native graph or sequence primitives.
4. **Implement persistence and memory** — Use the framework's built-in state management to ensure that an agent can "remember" the context of a previous step or recover from a transient failure.
5. **Monitor via tracing** — Connect the framework to an observability tool (like LangSmith or Phoenix) to audit every step of the agent's execution.

## Tradeoffs

**Pros:**

- Provides a structured way to build complex, non-linear agentic workflows.
- Standardizes the way state and memory are handled across different agent sessions.
- Built-in observability makes debugging and auditing agent behavior significantly easier.

**Cons:**

- Adds an abstraction layer that can obscure the underlying LLM calls and make performance tuning harder.
- Fast-moving ecosystem means APIs change frequently, leading to potential maintenance overhead.
- Over-engineering: simple tasks are often better handled with basic scripts rather than a full orchestration framework.

**Difficulties:**

- Learning curve: frameworks like LangGraph have a steep learning curve compared to simple prompt-then-call patterns.
- Integration: connecting a framework to a complex, internal legacy build environment requires significant boilerplate.

## Rationale

As modernization tasks grow from single-file edits to system-wide refactors, the complexity of managing the "agent's brain" increases exponentially. Orchestration frameworks provide the scaffolding needed to build reliable, multi-step systems that can handle the unpredictability of legacy code. However, they should be applied judiciously; the goal is to reduce the cognitive load on the developer, not to add unnecessary architectural layers to an already complex problem.

## Known Uses

- [LangGraph (LangChain)](https://langchain-ai.github.io/langgraph/) — widely used for building stateful agents with complex branching logic; adopted by teams building autonomous coding pipelines.
- [CrewAI](https://docs.crewai.com/) — popular for multi-agent workflows where agents take on specific personas (e.g., "Senior Architect" and "Test Engineer") to collaborate on a PR.

## References

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) — a critical look at agentic patterns that explains when to use (and when to avoid) complex orchestration frameworks.
- [Microsoft — AutoGen](https://microsoft.github.io/autogen/) — a research-led framework for building conversational multi-agent systems.

## Related Patterns

- [Agentic Coding Workflows](agentic-coding-workflows.md) — orchestration frameworks provide the infrastructure for running these workflows at scale.
- [Agent Sandboxing](agent-sandboxing.md) — any framework-orchestrated agent with shell access must still be sandboxed for security.
- [Human in the Loop](human-in-the-loop.md) — orchestration frameworks should include explicit "interrupt" points for human review of agent decisions.

## What Next

After selecting an orchestration framework, implement [Agentic Coding Workflows](agentic-coding-workflows.md) to begin executing your first multi-step modernization tasks.

## Staging History

**Trial (Feb 2026):** Orchestration frameworks like LangGraph and CrewAI are being trialed to manage the complexity of multi-agent modernization tasks. They are currently best suited for teams building custom, high-volume refactoring pipelines that exceed the capabilities of single-agent tools.
