# Practice Template

```yaml
---
title: "Practice Name"
stage: apply           # Roadmap stage: hold-on, assess, trial, apply, stop, remove
category: Category Name  # e.g., AI Tooling Setup, Testing & Quality, Legacy Modernization
description: "Intent statement: One sentence explaining why this practice exists and what it achieves."
strategic_value: core  # core (AI-unique), supporting (enabler), generic (commodity)
evolution: product     # Wardley stage: genesis, custom-built, product, commodity
devops_phases: [code]  # any of: plan, code, build, test, release, deploy, operate, monitor
---
```

> **Roadmap context:** Every practice in this roadmap is about modernizing legacy software systems using AI coding tools and AI agents. The `description` (Intent) and the **Problem** must fit this theme — not general software engineering advice, but guidance for teams actively replacing, refactoring, or augmenting legacy systems with the help of LLMs and autonomous agents.

> **Note on Intent:** The `description` field in a practice's front matter serves as the **Intent** statement. It is rendered prominently on the detail page by the layout, so it is **not** repeated in the body.

> **Evolution Stage:** Every practice must include an `evolution` field in its front matter, based on Simon Wardley's Evolution stages. This signals how mature and common the practice is in the industry:
> - **Genesis:** Brand new, unique, experimental, and high uncertainty.
> - **Custom-Built:** Patterns are emerging; teams are often building their own versions.
> - **Product:** Standardized tools or well-defined, repeatable patterns exist.
> - **Commodity:** Ubiquitous and standardized; a basic expectation for any modern project.

## [Practice Name]
> The name is typically a noun phrase — a tool, technique, or concept (e.g., "Anti-Corruption Layer", "Agent Sandboxing", "Strangler Fig Migration").

---

## Problem

[Phrased as a simple question rooted in legacy modernization. What challenge do teams face when replacing, refactoring, or augmenting legacy systems — and how do AI tools or agents make it newly solvable?]

*This problem is difficult because:*

- [Forces: why the problem is difficult and interesting]
- [...]

*Yet, solving this problem is feasible because:*

- [Key to solving the problem — often because AI tools or agents change the economics or feasibility]
- [...]

## Solution

[How to apply this practice in a legacy modernization context. Where relevant, explain how AI coding tools or agents are used to implement or accelerate the solution.]

## Tradeoffs

> Each practice entails some positive and negative tradeoffs.

**Pros:** [Positive consequences of applying this practice. This section could contain a list of multiple items (2 - 5).]

- Item 1
- Item 2
- Item 3

**Cons:** [Negative consequences or risks. This section could contain a list of multiple items (2 - 5).]

- Item 1
- Item 2
- Item 3

**Difficulties:** [Practical challenges in applying this practice — including any specific to AI-assisted execution. This section could contain a list of multiple items (2 - 5).]

- Item 1
- Item 2
- Item 3

## Rationale

> We explain why the solution makes sense.

[Justification for why this approach works — in particular, why it is the right response to the legacy modernization problem it addresses.]

## Known Uses

> Documented instances of this practice in the wild — case studies, field reports, and published accounts of real adoption. **Every entry must link to a source.** Unverifiable anecdotes do not belong here. **Prefer open-source projects and community adoptions over proprietary vendor case studies.**

## References

> Reading and watching material for practitioners who want to go deeper. **Prefer open-source tools and community resources over vendor or commercial products.** When a commercial product is the only meaningful example, name it but note the open-source alternative where one exists.

[Books, papers, blog posts, talk recordings, and documentation relevant to this practice. Each entry should include a brief note on why it is worth reading.]

## Related Patterns

> Related practices may suggest alternative actions. Other practices may suggest logical follow-up actions.

[List of related practices in this roadmap and how they connect in a modernization journey.]

## What Next

[The next logical practice to adopt after this one — a step forward in a legacy modernization or AI adoption journey.]

## Staging History

> Record why this practice was placed at its initial stage, and the motivation behind any subsequent stage changes.

**[Stage] ([Month Year]):** [Reason for initial placement.]

**[Stage] ([Month Year]):** [Reason for the stage change.]  ← only when applicable

---
---

# Example: AI-Generated Characterization Tests

```yaml
---
title: "AI-Generated Characterization Tests"
stage: apply
category: Testing & Quality
description: "Creating an automated safety net for untested legacy code by using AI agents to capture and codify current behavior before refactoring."
strategic_value: core
evolution: product
devops_phases: [test, code]
---
```

---

## Problem

How do you safely refactor or replace legacy code that has no test coverage and whose full behavior cannot be understood from reading the source alone?

*This problem is difficult because:*

- Legacy codebases often have zero test coverage for critical paths — the original authors relied on manual testing or never wrote tests at all.
- Reading the code is insufficient: years of implicit behavior (special cases, silent error suppression, undocumented rounding) is invisible until something breaks.
- Without a safety net, every refactoring step is a gamble — and AI agents making autonomous changes to untested code amplify this risk dramatically.

*Yet, solving this problem is feasible because:*

- LLMs can read a legacy function and generate test cases that call it with varied inputs and assert on its current outputs, capturing behavior without requiring the developer to understand it first.
- Generating mechanical test coverage is exactly the repetitive, pattern-following work where AI agents outperform humans in speed while requiring little domain knowledge.

## Solution

Use an AI coding agent to generate characterization tests — also called golden master tests — before any modernization change is made:

1. **Identify the target unit** — select a function, class, or module that must change. Prefer units with clear inputs and outputs.
2. **Generate tests against current behavior** — prompt an agent to call the code with diverse inputs and assert on whatever the code currently produces, right or wrong.
3. **Run and commit the baseline** — confirm all generated tests pass against the unchanged code, then commit them as the refactoring safety net.
4. **Modernize under the net** — make the change; any deviation from captured behavior immediately causes a failure.
5. **Replace incrementally** — as domain understanding grows, swap characterization tests for intentional unit tests that assert on correct behavior rather than current behavior.

## Tradeoffs

**Pros:**

- Provides a refactoring safety net in minutes rather than days for untested legacy code.
- Once in place, AI agents can make further autonomous changes with the characterization tests as a guard rail.
- No domain knowledge required to generate the initial suite — the agent reads the code, not the requirements.

**Cons:**

- Characterization tests codify bugs alongside correct behavior and must not be treated as a specification.
- Test quality depends on input diversity — an agent may miss edge cases that only appear in production data.

**Difficulties:**

- Output-sensitive code (timestamps, random IDs, external calls) requires manual wrapping or mocking before tests can be stabilized.
- Agents tend toward happy-path inputs; prompting explicitly for boundary conditions and error paths is necessary for useful coverage.

## Rationale

Autonomous AI agents changing legacy code without a test harness is the highest-risk combination in modernization work. Characterization tests change the economics: an agent can generate them faster than any human, and once in place they make subsequent agentic changes safe and auditable. This practice is the prerequisite that unlocks confident agentic refactoring — not a nice-to-have, but the foundation the rest of the agentic workflow depends on.

## Known Uses

- [Diffblue Cover — automated Java test generation](https://www.diffblue.com/products/) — generates characterization tests for legacy Java codebases automatically; adopted by large financial institutions to establish baseline coverage before modernization programs.

## References

- [Michael Feathers — *Working Effectively with Legacy Code*](https://www.oreilly.com/library/view/working-effectively-with/0131177052/) — introduced characterization testing as the primary technique for safely modifying untested legacy code; the conceptual foundation for this practice.
- [Approval Tests](https://approvaltests.com/) — a test framework built specifically for golden master / characterization testing; useful when AI-generated assertions need a structured output-comparison mechanism.

## Related Patterns

- **Harness Engineering** — characterization tests are the inner loop of a broader test harness; this practice provides the automated safety net that makes the harness trustworthy.
- **Agentic Coding Workflows** — agents making autonomous refactoring changes depend on characterization tests as their guard rail; this practice is a prerequisite for safe agentic operation on legacy code.
- **Human-in-the-Loop Review** — reviewing AI-generated characterization tests before committing is a critical checkpoint; a missed edge case in the baseline propagates silently into every subsequent change.

## What Next

With a characterization test baseline in place, apply **Agentic Coding Workflows** to begin autonomous refactoring — the agent now has a safety net it can run after every change.

## Staging History

**Apply (Feb 2026):** AI-assisted characterization test generation is well-validated in practice and directly addresses the most dangerous gap in agentic legacy modernization: agents changing untested code. The underlying technique is proven; LLMs make the generation step fast enough to apply routinely. Immediate adoption is recommended for any team running agents against a legacy codebase.
