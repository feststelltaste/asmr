---
title: "Domain-Driven Refactoring"
stage: apply
category: Legacy Modernization
description: "Using DDD techniques (bounded contexts, ubiquitous language) to find the right cuts when splitting a monolith. LLMs can help identify domain concepts in code."
strategic_value: supporting
devops_phases: [plan, code]
---

# Domain-Driven Refactoring

## Problem

How do you find the "right cuts" when splitting a legacy monolith into modern services, ensuring that the new boundaries align with business logic rather than just historical database constraints?

*This problem is difficult because:*

- Legacy systems are often "spaghetti code" where business logic, data access, and UI are tightly coupled in ways that are hard for a human to untangle without deep expertise.
- The original domain model has often drifted or been corrupted over time, leaving different modules to use the same names for different concepts (e.g., an "Order" in shipping vs. an "Order" in billing).
- Splitting a monolith based on "technical layers" (e.g., UI vs. DB) usually fails to solve the underlying complexity problem; the real value is in splitting by business domain.
- Identifying "Bounded Contexts" in a million-line codebase is a massive "code archaeology" task that requires deep domain knowledge and weeks of manual reading.

*Yet, solving this problem is feasible because:*

- LLMs are excellent at identifying "semantic clusters" in code—noticing where certain names, concepts, and data structures consistently appear together.
- AI can quickly map the "ubiquitous language" used in different parts of a codebase, highlighting where the same word (e.g., "Account") means different things in different contexts.
- Agents can analyze transaction boundaries and data flow to suggest natural "cuts" that minimize cross-service dependencies.
- Frontier LLMs can read entire modules and generate "draft" context maps and domain model diagrams in seconds, providing a starting point for human architects.

## Solution

Utilize DDD principles, assisted by AI-driven analysis, to identify the logical boundaries for your modernization effort:

1. **Perform an AI-assisted "Semantic Audit"** — Task an LLM to identify the core domain entities and their synonyms across the entire codebase. Look for areas of "semantic overlap" where boundaries are currently blurred.
2. **Identify Bounded Contexts** — Use the semantic clusters and data flow analysis to define clear, independent boundaries where a specific "ubiquitous language" is consistent.
3. **Map the "Context Map"** — Document the relationships between these contexts (e.g., Upstream/Downstream, Customer/Supplier) using AI to visualize the current coupling.
4. **Define the target "Ubiquitous Language"** — Use the AI to help formalize the naming and structures for the new services, ensuring they are independent of the legacy database schema.
5. **Implement an Anti-Corruption Layer (ACL)** — Protect the new, domain-pure services from legacy "pollution" by using an ACL at every boundary (see **Anti-Corruption Layer**).

**Key DDD patterns for modernization:**

- **Bounded Context** — A clear, linguistic boundary where a model is valid; the basis for a modern microservice.
- **Ubiquitous Language** — A shared vocabulary between developers and business experts; the AI can help enforce this in generated code.
- **Aggregate Root** — The entry point for a cluster of objects that are treated as a single unit for data changes; identifies natural service boundaries.
- **Context Map** — A visual representation of the relationships between different bounded contexts and how they integrate.

## Tradeoffs

**Pros:**

- Ensures that the modernized system is more aligned with the business's actual needs, rather than historical technical constraints.
- Reduces the complexity of the new system by making boundaries explicit and independent.
- Makes it easier for both human and AI developers to reason about the system in "business terms."

**Cons:**

- Domain modeling requires deep involvement from business experts—it cannot be done by developers or AI in isolation.
- Over-engineering: splitting a monolith into too many tiny contexts can lead to a "distributed monolith" that is even harder to manage.

**Difficulties:**

- Untangling the "technical debt" (shared databases, global state) that currently binds different domain concepts together in the legacy monolith.
- Convincing the business to invest in "domain modeling" when they just want the technical migration to be "done."

## Rationale

Modernization is not just about changing the technology; it is about improving the system's ability to change. Domain-Driven Design (DDD) provides the only proven framework for managing the complexity of large systems by aligning the software architecture with the business architecture. AI changes the math of DDD by making the "discovery" phase (which was previously the most expensive part) fast and nearly free, allowing teams to move from "spaghetti code" to clean, domain-pure services with confidence.

## Known Uses

- [Henning Schwentner — Domain-Driven Refactorings](https://hschwentner.io/domain-driven-refactorings/) — a catalog of concrete refactoring moves based on DDD principles.
- [EventStorming by Alberto Brandolini](https://www.eventstorming.com/) — a collaborative technique for discovering bounded contexts that can be accelerated with AI-assisted documentation.

## References

- [Eric Evans — Domain-Driven Design (Blue Book)](https://www.domainlanguage.com/ddd/) — the foundational text that introduced bounded contexts and ubiquitous language.
- [Vaughn Vernon — Implementing Domain-Driven Design](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/) — practical guidance on applying DDD in real-world systems.

## Related Patterns

- **Anti-Corruption Layer (ACL)** — the primary technical pattern for protecting a new domain model from legacy corruption.
- **Strangler Fig Migration** — DDD provides the "cuts" for the slices that are strangled from the legacy monolith.
- **AI-assisted Legacy Code Reading** — the technique used to perform the initial "semantic audit" of the legacy system.

## What Next

After identifying your first bounded context, apply **Anti-Corruption Layer (ACL)** to protect the new service as you begin to migrate logic using the **Strangler Fig Migration** pattern.

## Staging History

**Apply (Feb 2026):** Domain-Driven Refactoring is a foundational practice for any serious modernization effort. While it requires human expertise to finalize the model, AI-assisted discovery makes the initial " archaeology" step much faster and more accurate. Use this approach to ensure your new services are built on a solid business foundation.
