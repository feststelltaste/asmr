# Practice Template

> **Roadmap context:** Every practice in this roadmap is about modernizing legacy software systems using AI coding tools and AI agents. The `description` (Intent) and the **Problem** must fit this theme — not general software engineering advice, but guidance for teams actively replacing, refactoring, or augmenting legacy systems with the help of LLMs and autonomous agents.

> **Note on Intent:** The `description` field in a practice's front matter serves as the **Intent** statement. It is rendered prominently on the detail page by the layout, so it is **not** repeated in the body.

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

> Documented instances of this practice in the wild — case studies, field reports, and published accounts of real adoption. **Every entry must link to a source.** Unverifiable anecdotes do not belong here.

## References

> Reading and watching material for practitioners who want to go deeper.

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

# Example: Strangler Fig Migration

---

## Problem

How do you replace a legacy system without halting ongoing business operations?

*This problem is difficult because:*

- The legacy system is deeply integrated with many other systems and processes.
- A full rewrite takes years, during which the old system still needs maintenance.
- Stakeholders cannot tolerate extended downtime or feature freezes.

*Yet, solving this problem is feasible because:*

- Most systems can be decomposed into independent functional areas.
- Modern APIs and routing layers allow traffic to be redirected incrementally.

## Solution

1. Identify a functional slice of the legacy system that can be isolated.
2. Build the replacement for that slice in the new system.
3. Route traffic/requests for that slice to the new implementation.
4. Repeat until the legacy system is fully replaced, then decommission it.

## Tradeoffs

**Pros:**

- Risk is reduced because you migrate in small, testable increments.
- The business continues to operate throughout the migration.

**Cons:**

- You must maintain two systems in parallel for a potentially long period, increasing operational complexity.

**Difficulties:**

- Finding clean boundaries in the legacy system to "strangle" can be challenging, especially with tightly coupled code or shared databases.


## Rationale

A big-bang rewrite is one of the riskiest strategies in software engineering. By migrating incrementally, each step is small, reversible, and independently verifiable. The legacy system continues to serve as a fallback until the new system proves itself.

## Known Uses

- [Amazon — decomposing the retail monolith](https://aws.amazon.com/solutions/case-studies/) — routed traffic to new services incrementally over several years while the legacy system remained live; a canonical large-scale strangler fig.
- [Shopify — extracting checkout into a standalone service](https://shopify.engineering/shopify-monolith) — migrated payments and checkout without downtime by strangling the monolith slice by slice.

## References

- [Martin Fowler — "Strangler Fig Application"](https://martinfowler.com/bliki/StranglerFigApplication.html) — the original write-up that named the pattern; explains the biological metaphor and migration mechanics.
- [Sam Newman — *Building Microservices*](https://samnewman.io/books/building_microservices/) — chapter on decomposing monoliths covers the strangler fig as the primary migration strategy.

## Related Patterns

- **If It Ain't Broke, Don't Fix It** — prioritize which parts actually need migration.
- **Fix Problems, Not Symptoms** — ensure you're addressing root causes, not just moving technical debt.
- **Branch by Abstraction** — an alternative incremental migration technique.

## What Next

Consider applying **Most Valuable First** to decide which slice of the legacy system to migrate first.

## Staging History

**Apply (Feb 2026):** The Strangler Fig pattern is well-established, broadly documented, and has extensive real-world validation across major migrations (Amazon, Shopify, Netflix). Teams facing legacy replacement have reliable tooling and implementation guidance. Immediate adoption is recommended.
