---
title: "AI-assisted Codebase Analytics"
stage: trial
category: Legacy Modernization
description: "Using AI-assisted vibe coding to build custom, situation-specific analysis scripts that reveal how your legacy system actually behaves — hotspots, coupling, change frequency, and more."
strategic_value: core
devops_phases: [plan, monitor]
---

## Overview

Every legacy system has unique problems that generic tools don't surface. Vibe coding makes it practical to build custom analysis tools tailored to your specific situation: a Python notebook that maps which modules change together, a script that identifies the 10% of code causing 80% of bugs, or a query that traces data flows through undocumented tables.

This is Software Analytics applied at development speed — you describe what insight you need, the AI writes the analysis code, and you iterate on the results.

## What You Can Build

- **Hotspot analysis** — Combine code complexity with change frequency (git log) to find where effort concentrates
- **Coupling maps** — Identify files that always change together (logical coupling) even without direct code dependencies
- **Temporal coupling detectors** — Find implicit dependencies not visible in the call graph
- **Dead code finders** — Custom scripts that cross-reference static analysis with production access logs
- **Architecture conformance checks** — Verify that module dependencies match intended architecture
- **Dependency age trackers** — Flag libraries that haven't been updated and assess their risk

## Workflow

1. Identify a question about your system you can't answer with existing tools
2. Describe the analysis to an AI assistant — what data sources, what output format
3. Iterate quickly: run → refine → extend
4. Once useful, share the script with the team or add to your CI pipeline

## Data Sources to Combine

- Git history (change frequency, co-change, authorship)
- Static analysis output (complexity metrics, dependency graphs)
- Test coverage data
- Production logs and traces
- Issue tracker data (bugs per file)

## Risks & Considerations

- Custom scripts need maintenance as the codebase evolves
- Correlation in metrics is not causation — validate findings with the team
- Start with questions you already have a hypothesis for; avoid pure fishing expeditions

## Resources

- [Markus Harrer — Software Analytics](https://softwareanalytics.de/) — practical software analytics for developers, with notebooks and katas
- [Adam Tornhill — Your Code as a Crime Scene](https://pragprog.com/titles/atcrime2/your-code-as-a-crime-scene-second-edition/) — behavioral code analysis techniques using git history
- [CodeScene](https://codescene.com/) — commercial tool built on behavioral code analysis principles
- [jQAssistant](https://jqassistant.org/) — graph-based architecture analysis and constraint checking
- [YouTube — Software analytics and code analysis](https://www.youtube.com/results?search_query=software+analytics+code+hotspot+analysis+legacy+2025)
