---
title: "AI-assisted Codebase Analytics"
stage: apply
category: Legacy Modernization
description: "Using AI-assisted vibe coding to build custom, situation-specific analysis scripts that reveal how your legacy system actually behaves — hotspots, coupling, change frequency, and more."
strategic_value: core
evolution: custom-built
devops_phases: [plan, monitor]
---

# AI-assisted Codebase Analytics

## Problem

How do you move beyond generic static analysis to build custom, situation-specific insights that reveal how your legacy system actually behaves—and where its hidden risks lie?

*This problem is difficult because:*

- Legacy systems often have unique, non-standard architectural patterns that generic tools (like SonarQube or standard linters) fail to understand or misinterpret as "clean" code.
- The most dangerous risks in a legacy system are often behavioral—hotspots of frequent change, high coupling, or "tribal knowledge" silos—rather than simple code smells.
- Building custom analysis scripts to extract these behavioral insights from git history, logs, and code has traditionally been too slow and expensive for a modernization team to justify.
- Modernization teams often guess where to focus their effort based on anecdotes rather than empirical data because the data is too hard to reach.

*Yet, solving this problem is feasible because:*

- AI-assisted "vibe coding" makes it practical to generate custom, one-off analysis scripts in minutes, tailored to a specific codebase's quirks.
- LLMs can quickly write complex Python, SQL, or shell queries to cross-reference data sources (git logs, issue trackers, source code) that would take hours for a developer to write manually.

## Solution

Use an AI coding assistant to build "disposable" or situation-specific analysis tools that surface empirical data about your system:

1. **Identify a hypothesis** — ask a specific question (e.g., "Which 10% of our code is involved in 80% of our production incidents?") or identify a hunch about the system's hidden complexity.
2. **Describe the analysis to an LLM** — provide the data sources (e.g., "Write a Python script that combines git log data with our `incidents.csv` to find files with high change frequency and high bug count").
3. **Iterate via vibe coding** — run the script, check the results, and refine the analysis (e.g., "Now filter out files that are mostly auto-generated boilerplate").
4. **Visualize the findings** — use the AI to generate a quick visualization (e.g., "Generate a D3.js treemap or a simple CSV I can import into Excel to show the findings").
5. **Act on the data** — use the resulting "hotspot map" to prioritize which parts of the legacy system to refactor or replace first.

**Types of analysis you can build:**

- **Hotspot analysis** — mapping code complexity against change frequency (git log) to find where effort is concentrated.
- **Coupling maps** — identifying files that always change together (logical coupling) even without direct code dependencies.
- **Temporal coupling** — finding implicit dependencies not visible in the call graph.
- **Dead code finders** — cross-referencing static analysis with production access logs to find truly unused code.

## Tradeoffs

**Pros:**

- Replaces "gut feeling" with empirical data when prioritizing modernization efforts.
- Custom-built scripts are often more accurate than generic tools for specific legacy quirks.
- Low cost: scripts are "disposable" and can be regenerated or updated as the system evolves.

**Cons:**

- Results are only as good as the data sources (e.g., if git history is messy, the analysis will be too).
- Custom scripts require validation to ensure they aren't misinterpreting the data.

**Difficulties:**

- Getting the right data into the AI's context (e.g., providing samples of git log output or CSV headers) to ensure it writes correct queries.
- Avoiding "analysis paralysis"—using data to support decisions rather than delaying them.

## Rationale

Every legacy system has its own unique "scars"—undocumented dependencies, fragile modules, and areas of high churn. Generic tools are designed for general cases, but modernization is a specific, surgical intervention. AI-assisted analytics turns software engineering into an empirical science: by making it nearly free to build custom tools, it allows teams to find and fix the problems that actually matter to their specific system, rather than just fixing whatever the linter flags.

## Known Uses

- [Adam Tornhill — Your Code as a Crime Scene](https://pragprog.com/titles/atcrime2/your-code-as-a-crime-scene-second-edition/) — the conceptual foundation for behavioral code analysis using git history, now made significantly faster with AI.
- [CodeScene](https://codescene.com/) — a commercial tool built on these principles; teams often use AI to build "lite" versions of these analyses for specific tasks.

## References

- [Markus Harrer — Software Analytics](https://softwareanalytics.de/) — practical guidance on using data to drive software engineering decisions.
- [jQAssistant](https://jqassistant.org/) — a graph-based tool for architectural analysis that can be queried with AI-generated Cypher queries.

## Related Patterns

- [AI-driven Technical Debt Detection](../ai-technical-debt-detection/) — analytics provides the empirical data to prioritize the debt that the LLM identifies.
- [Agentic Coding Workflows](../agentic-coding-workflows/) — once hotspots are identified, agents can be tasked with refactoring those specific high-risk areas.
- [Vibe Coding](../vibe-coding/) — the technique used to rapidly build and iterate on these custom analysis scripts.

## What Next

After identifying hotspots, apply [AI-driven Technical Debt Detection](../ai-technical-debt-detection/) to those specific areas to get a detailed, prioritized list of refactoring tasks.

## Staging History

**Apply (Feb 2026):** AI-assisted analytics has become a standard foundational practice for identifying modernization hotspots and measuring technical debt. The ability to generate custom analysis scripts at development speed has made it a proven choice for data-driven prioritization.
