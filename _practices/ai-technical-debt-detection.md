---
title: "AI-driven Technical Debt Detection"
stage: assess
category: Agentic AI Tools
description: "Using LLMs to systematically identify, classify, and prioritize technical debt across a codebase — turning a slow manual process into an automated, prioritized backlog."
strategic_value: core
evolution: custom-built
devops_phases: [plan, code]
---

# AI-driven Technical Debt Detection

## Problem

How do you systematically identify, categorize, and prioritize the technical debt hidden within a legacy codebase without spending months on a manual, subjective architectural audit?

*This problem is difficult because:*

- Technical debt is often "invisible"—it hides in complex dependencies, inconsistent naming, and "tribal knowledge" that isn't documented anywhere.
- Manual audits of large legacy codebases are prohibitively expensive and reflect the subjective biases of the auditors.
- Traditional static analysis tools (like linters or SonarQube) are good at finding simple "code smells" but fail to identify deeper architectural debt or implicit business rule violations.
- Prioritizing debt is a business decision, but the empirical data needed to make that decision (risk vs. effort) is often buried deep in the code.

*Yet, solving this problem is feasible because:*

- LLMs can read entire modules or bounded contexts and identify complex patterns of "debt" that violate modern design principles (e.g., excessive coupling, low cohesion, SOLID violations).
- AI can process thousands of files in parallel, producing a structured, prioritized debt report that would take a human architect months to compile manually.
- LLMs can explain the *rationale* behind a debt finding, helping developers understand not just what is wrong, but why it matters for the modernization effort.

## Solution

Utilize an AI-driven approach to perform a systematic "debt scan" of your legacy system:

1. **Define your "Modernization Standard"** — Provide the LLM with the target architectural standards you are moving toward (e.g., "Flag any logic that is tightly coupled to our legacy mainframe schema").
2. **Execute module-by-module scans** — Feed the LLM code at the level of a module or bounded context to ensure it has enough local context to identify architectural debt.
3. **Generate structured debt reports** — Use structured output (JSON/CSV) to capture each finding, including its location, severity, type of debt, and the estimated effort to refactor.
4. **Prioritize via cross-referencing** — Combine the AI's findings with behavioral data (see **AI-assisted Codebase Analytics**) to find the "hotspots" where debt is most frequently touched by developers.
5. **Feed findings into the backlog** — Automatically import the prioritized debt reports into your issue tracker (Jira, GitHub Issues) to create an actionable modernization roadmap.

**Common debt types detected by AI:**

- **Architectural violations** — Code that bypasses the defined layers or boundaries.
- **Implicit business logic** — Complex, undocumented validation or transformation rules.
- **Inconsistent domain concepts** — Using different names for the same entity across modules.
- **Missing or weak test coverage** — Identifying areas where current tests only cover the "happy path."
- **Outdated patterns** — Use of deprecated libraries or archaic language features that hinder modernization.

## Tradeoffs

**Pros:**

- Provides an objective, systematic view of the entire codebase's debt profile.
- Drastically reduces the time and cost of performing a comprehensive architectural audit.
- Helps teams move from "guessing" what to refactor to making data-driven prioritization decisions.

**Cons:**

- LLMs can flag "false debt" where they misinterpret complex-but-necessary legacy logic as a code smell.
- The debt report can be overwhelming if not filtered and prioritized by a human expert.

**Difficulties:**

- Ensuring the AI has enough "global context" to understand if a local code pattern is part of a larger, intentional architecture.
- Balancing the AI's findings with the business reality: some debt is "safe" to leave if that part of the system is scheduled for decommissioning.

## Rationale

Modernization projects often fail because they try to fix everything at once, or they fix the wrong things first. AI-driven detection changes the math: it makes the "invisible" debt visible and quantifiable. By providing a structured, prioritized view of the codebase's debt, it allows teams to apply their limited modernization budget where it will have the greatest impact on future agility and risk reduction.

## Known Uses

- [SonarQube / SonarCloud](https://www.sonarsource.com/products/sonarqube/) — increasingly incorporating LLM-based "Deep Code Analysis" to find complex issues that traditional rules-based engines miss.
- [Glean](https://www.glean.com/) — uses AI to index and understand internal knowledge, which can be applied to identifying "documentation debt" and missing knowledge in legacy code.

## References

- [Martin Fowler — Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — the foundational framework for classifying different types of debt.
- [Ward Cunningham — The Debt Metaphor](http://wiki.c2.com/?WardExplainsDebtMetaphor) — the original concept of technical debt.

## Related Patterns

- [AI-assisted Codebase Analytics](../ai-assisted-codebase-analytics/) — provides the empirical data (hotspots, churn) used to prioritize the debt identified by the AI.
- [AI-assisted Legacy Code Reading](../ai-assisted-legacy-code-reading/) — the technique used to feed the "debt detector" the context it needs to be accurate.
- [Agentic Coding Workflows](../agentic-coding-workflows/) — once debt is identified and prioritized, agents can be tasked with the mechanical work of refactoring it.

## What Next

After identifying and prioritizing technical debt, apply [AI-assisted Codebase Analytics](../ai-assisted-codebase-analytics/) to verify which debt items are in the most active parts of the codebase, then use [Agentic Coding Workflows](../agentic-coding-workflows/) to begin the refactoring work.

## Staging History

**Assess (Feb 2026):** AI-driven technical debt detection is being assessed as a strategic tool for modernization planning. The ability to scan an entire codebase for deep architectural violations is transformative, but teams must still evaluate the signal-to-noise ratio and calibrate the findings against their specific business context.
