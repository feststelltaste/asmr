---
title: "Legacy UI Archaeology (Vision-to-Code)"
stage: trial
category: Legacy Modernization
description: "Using multi-modal vision models to reconstruct business rules from legacy screens (Mainframe, VB6, PowerBuilder) and generate modern front-end equivalents."
strategic_value: core
devops_phases: [plan, code]
---

# Legacy UI Archaeology (Vision-to-Code)

## Problem

How do you modernize legacy systems (Mainframe green screens, VB6, PowerBuilder) where critical business logic and process flows are "hidden" within the UI layer and are difficult to extract from the archaic source code alone?

*This problem is difficult because:*

- In many legacy systems, the "UI" and "Business Logic" are inseparable—validation rules, calculation logic, and state transitions are often embedded directly in form definitions or event handlers.
- The source code for these UIs (e.g., COBOL screen maps, VB6 `.frm` files) is often difficult for modern developers to read and trace, making it hard to identify the "rules of the system."
- Documentation for these legacy screens is almost always missing or outdated, leaving the "running application" as the only reliable source of truth.
- Re-implementing a 30-year-old business process in a modern React/Angular stack often fails because subtle "manual" steps and edge cases hidden in the legacy UI are missed.

*Yet, solving this problem is feasible because:*

- Multi-modal frontier models (like Claude Sonnet 4.6 or Gemini 3.1 Pro) can "see" and interpret screenshots or UI recordings of legacy applications.
- AI can reconstruct the "logical intent" of a screen (e.g., "This is an insurance claim entry form with 15 mandatory fields") just by looking at it.
- LLMs can analyze archaic UI definition code (like PowerBuilder or Delphi) and translate it into clean, modern component structures and state models.
- Agents can "watch" a recording of a subject matter expert (SME) using the legacy system and document the end-to-end business process flow automatically.

## Solution

Deploy multi-modal AI agents to perform "archaeology" on the legacy UI layer and generate modern equivalents:

1. **Capture the Evidence** — Collect screenshots, UI definition files, and video recordings of the legacy application in use.
2. **Interpret Intent via Vision** — Feed these visual assets to a multi-modal LLM and task it with identifying all fields, labels, validation rules, and "hidden" business logic.
3. **Map the "State Machine"** — Use the AI to reconstruct the transitions between different screens and identify the underlying business process flow.
4. **Generate Modern Components** — Task an agent to generate React, Angular, or Vue components that match the *functional* requirements of the legacy screen while adopting modern UX patterns.
5. **Extract Validation Logic** — Point the AI at the legacy "event handler" code (e.g., `OnClick`, `OnValidate`) and have it translate those rules into modern TypeScript or backend validation services.

**Key UI Archaeology tasks:**

- **Screen-to-Component Translation** — Converting archaic form definitions into modern UI components.
- **Process Mining via Video** — Reconstructing business workflows from SME screen recordings.
- **Label-to-Domain Mapping** — Using the UI's human-readable labels to identify domain entities in the legacy database.
- **Validation Rule Recovery** — Extracting "hidden" validation logic that isn't documented in the backend code.

## Tradeoffs

**Pros:**

- Recovers critical business knowledge that is "trapped" in the legacy UI layer.
- Dramatically speeds up the "front-end" modernization process by providing a clear starting point for new components.
- Ensures that the new system maintains "functional parity" with the legacy system for the end users.

**Cons:**

- High risk of "visual hallucinations" where the AI misinterprets a legacy UI element or misses a subtle dynamic behavior.
- Functional parity does not mean "pixel-perfect" parity; teams must decide when to follow legacy patterns and when to improve them.

**Difficulties:**

- Handling "dynamic" UI behavior (e.g., fields that only appear when a specific value is entered) that is hard to capture in static screenshots.
- Translating "manual" legacy workflows (e.g., "press F3 to search") into modern web navigation patterns.

## Rationale

The UI is the "face" of the business logic. In many older systems, it is the only part of the system that is actually understood by the people who use it. By using multi-modal AI to bridge the gap between the "visual reality" of the legacy system and the "logical requirements" of the new one, teams can ensure that their modernization effort actually solves the business's needs rather than just moving the same mess to a newer stack.

## Known Uses

- [Mainframe Modernization](https://aws.amazon.com/mainframe-modernization/) — many teams now use vision-based tools to analyze "green screen" terminal emulators and generate modern web interfaces.
- [VB6 to .NET Migrations](https://learn.microsoft.com/en-us/dotnet/architecture/modernize-with-azure-and-containers/modernize-existing-apps-to-cloud-optimized/replatform-visual-basic-6-applications) — a classic use case for automated UI archaeology.

## References

- [Object-Oriented Reengineering Patterns](https://oorp.github.io/) — discusses patterns for extracting business rules from legacy systems.
- [Andrej Karpathy — Vibe Coding](https://x.com/karpathy/status/1886192184808149176) — vision-to-code is a primary example of high-velocity "vibe coding."

## Related Patterns

- [AI-assisted Legacy Code Reading](../ai-assisted-legacy-code-reading/) — UI archaeology provides the "visual" context that complements source code reading.
- [Domain-Driven Refactoring](../domain-driven-refactoring/) — labels and flows in the UI are high-quality signals for identifying Bounded Contexts.
- [AI-generated Characterization Tests](../ai-generated-characterization-tests/) — use the recovered UI rules to generate end-to-end tests for the new front-end.

## What Next

After reconstructing your first legacy screen, apply [Vibe Coding](../vibe-coding/) to quickly iterate on the modern React/Angular implementation of that component.

## Staging History

**Trial (Feb 2026):** Legacy UI archaeology (Vision-to-Code) is placed in the trial phase. Early results from modernizing Mainframe and VB6 screens show that vision models can reliably extract business rules trapped in the UI layer, though human verification is essential for complex workflows.
