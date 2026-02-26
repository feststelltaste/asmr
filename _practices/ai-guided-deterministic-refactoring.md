---
title: "AI-Guided Deterministic Refactoring"
stage: trial
category: Legacy Modernization
description: "Using AI non-deterministically to identify and specify what needs to change, then delegating the actual transformation to deterministic, auditable tooling such as AST rewriters, codemods, or language-server-driven scripts."
strategic_value: core
evolution: custom-built
devops_phases: [code, build]
---

# AI-Guided Deterministic Refactoring

---

## Problem

How do you perform large-scale, repeatable code transformations across a legacy codebase while keeping the changes verifiable, auditable, and safe to re-run — without sacrificing the semantic intelligence needed to identify what actually needs to change?

*This problem is difficult because:*

- LLM-generated edits are powerful but non-deterministic: running the same agent twice on the same file can produce subtly different results, making transformations hard to audit, reproduce, or roll back with confidence.
- Traditional automated refactoring tools (codemods, AST rewriters, OpenRewrite recipes) are precise and reproducible but blind: they must be told exactly which syntactic pattern to match, and they have no semantic understanding of legacy intent, naming inconsistencies, or implicit conventions.
- Legacy codebases often mix dozens of variations of the same bad pattern (three different ways to open a DB connection, four inconsistent date-formatting idioms), making it impossible to write a single deterministic rule without first mapping the variation landscape.
- The cost of a mis-applied transformation at scale is high: an incorrect codemod touching 3 000 files produces 3 000 broken sites simultaneously.

*Yet, solving this problem is feasible because:*

- LLMs excel at the fuzzy, semantic part: surveying the codebase, recognising pattern families, and producing a precise specification of what rule to codify — even when the surface syntax varies.
- Deterministic tools (ast-grep, OpenRewrite, Rector, jscodeshift/ts-morph codemods, Serena via MCP, LSP rename/refactor APIs, or plain bash scripts) excel at the mechanical part: applying a rule exactly, consistently, and verifiably across thousands of files.
- Separating discovery (AI) from execution (deterministic tooling) means each phase can be reviewed and approved independently, preserving human oversight at the architectural boundary.

## Solution

Structure the transformation pipeline as two distinct, hand-off phases:

**Phase 1 — Non-Deterministic Discovery (AI)**

1. **Survey the target pattern** — Prompt an AI agent to scan the codebase and characterise all instances of the problematic pattern: what it looks like syntactically, how many variants exist, where the edge cases are, and what the correct replacement should be.
2. **Produce a transformation specification** — Ask the agent to output a structured spec: the match pattern, the replacement rule, any preconditions, and a list of file paths that should and should not be affected.
3. **Generate the recipe skeleton** — Have the agent draft the initial codemod/recipe/script (e.g., an ast-grep YAML rule, an OpenRewrite Java recipe class, a Rector rule, a jscodeshift transform, or a sed pipeline) from the specification. This output is a *draft* — it must be reviewed, not trusted blindly.

**Phase 2 — Deterministic Execution (Tooling)**

4. **Review and harden the recipe** — A developer reads the generated rule, verifies it against the spec, tightens the match conditions, and adds a dry-run or `--diff` preview.
5. **Run against a test slice** — Apply the recipe to a small, well-tested sub-module first. Confirm the diff matches expectations; run the test suite.
6. **Execute at scale** — Once validated, run the recipe across the full codebase. Because the tool is deterministic, the same command re-run on the same input always produces the same output.
7. **Commit the recipe as an artifact** — Check the recipe file into the repository. Future similar changes can reuse or extend it, and the recipe documents *why* the transformation was made.

**Tool selection guide by context:**

| Scenario | Appropriate tool |
|---|---|
| Language-agnostic structural search/replace | [ast-grep](https://ast-grep.github.io/) |
| Java/Kotlin/Groovy migrations at ecosystem scale | [OpenRewrite](https://docs.openrewrite.org/) |
| PHP legacy upgrades and pattern standardisation | [Rector](https://getrector.com/) |
| JavaScript / TypeScript AST transformations | [jscodeshift](https://github.com/facebook/jscodeshift) / [ts-morph](https://ts-morph.com/) |
| Semantic rename, move, inline via language intelligence | LSP (`workspace/applyEdit`) or [Serena MCP](https://github.com/oramasearch/serena) |
| Simple token-level or line-level replacements | `sed`, `awk`, or purpose-built bash scripts |

## Tradeoffs

**Pros:**

- Combines the semantic intelligence of AI with the precision and reproducibility of deterministic tooling — neither alone achieves both.
- Every transformation is encoded as a reviewable, versionable artifact (recipe, codemod, script) rather than a black-box agent diff.
- Recipes can be re-applied as new code enters the codebase (e.g., in CI), turning a one-time migration into a continuous enforcement gate.
- Reduces per-site review burden: a reviewer reads one recipe rather than thousands of individual diffs.

**Cons:**

- Adds an explicit hand-off step between the AI-discovery phase and the deterministic-execution phase, which slows down the loop compared to a fully autonomous agent.
- The generated recipe skeleton may miss edge cases the AI did not anticipate during the survey phase, requiring manual refinement.

**Difficulties:**

- AST-based tools require a precise understanding of each language's syntax tree; a recipe that looks correct can silently mismatch on uncommon AST shapes.
- Not every transformation is expressible as a composable recipe: deeply imperative logic restructuring (e.g., splitting a god class) still requires agent-level free-form editing.
- Keeping recipes composable and idempotent takes discipline; without it, re-running a recipe on partially-migrated code can corrupt already-converted sites.

## Rationale

The root tension in AI-assisted refactoring is between *intelligence* and *trust*. A fully autonomous LLM agent applies changes that are hard to audit or reproduce; a hand-written codemod is trustworthy but requires a human to enumerate every pattern variant manually. This practice resolves the tension by treating the LLM as a *specification writer* rather than an *executor*: it contributes the semantic survey and the recipe skeleton, but a deterministic tool makes the actual edits. The result is a transformation that a senior engineer can read, challenge, and approve at the recipe level before a single file is touched.

## Known Uses

- [OpenRewrite migration recipes](https://docs.openrewrite.org/running-recipes) — the OpenRewrite community generates and curates hundreds of recipes for Java ecosystem migrations; AI tooling is increasingly used to generate custom recipes for proprietary patterns.
- [Facebook / Meta codemods](https://github.com/facebook/codemod) — jscodeshift was created at Meta to manage large-scale JS transformations; teams routinely use LLM assistance to draft the transform logic before applying it at repository scale.
- [Rector — AI-assisted rule generation](https://getrector.com/) — the Rector community has explored using LLMs to generate new Rector rules from before/after code examples.

## References

- [ast-grep — structural code search and rewrite](https://ast-grep.github.io/) — a fast, language-agnostic tool for writing AST pattern-matching rules in YAML or JavaScript; ideal for polyglot legacy codebases.
- [OpenRewrite documentation](https://docs.openrewrite.org/) — the authoritative guide to writing, testing, and sharing OpenRewrite recipes for Java ecosystem refactoring.
- [jscodeshift](https://github.com/facebook/jscodeshift) — Facebook's JavaScript codemod toolkit; pairs well with AI-generated transform logic.
- [Serena MCP server](https://github.com/oramasearch/serena) — exposes semantic code navigation and editing operations (go-to-definition, rename, find-references) to AI agents via MCP, bridging the gap between LLM reasoning and language-server precision.
- [Language Server Protocol — workspace/applyEdit](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_applyEdit) — the LSP capability that allows tooling to push language-server-validated edits, enabling rename and move operations backed by full type resolution.

## Related Patterns

- [Autonomous Refactoring Agents](../autonomous-refactoring-agents/) — the free-form alternative: agents make all edits themselves. Prefer this practice when auditability and reproducibility are paramount; prefer agents when the transformation is too complex to express as a recipe.
- [AI-driven Technical Debt Detection](../ai-technical-debt-detection/) — the upstream practice that produces the list of patterns worth writing recipes for; feeds directly into Phase 1 of this workflow.
- [Autonomous Pattern Enforcement](../autonomous-pattern-enforcement/) — once a recipe is validated, it can be promoted to an enforcement gate that runs in CI, making the pattern a permanent architectural constraint.
- [Model Context Protocol (MCP)](../model-context-protocol/) — Serena and custom MCP servers expose deterministic tooling (LSP, file system, shell) to the AI agent in Phase 1, tightening the feedback loop between discovery and recipe generation.
- [AI-Generated Characterization Tests](../ai-generated-characterization-tests/) — a complementary safety net: generate tests before applying a recipe to ensure the transformation preserves existing behaviour.

## What Next

After validating a recipe on one module, promote it into [Autonomous Pattern Enforcement](../autonomous-pattern-enforcement/) by adding it to the CI pipeline — the recipe becomes a living architectural rule that rejects non-conforming code on every pull request.

## Staging History

**Trial (Feb 2026):** The individual deterministic tools (OpenRewrite, ast-grep, Rector, jscodeshift) are mature and production-proven. The practice of using AI to *generate* the recipes — the non-deterministic discovery and specification phase — is still being standardised: teams are building their own workflows rather than using a shared platform. Trial is appropriate while these AI-to-recipe pipelines stabilise and early adopters establish patterns for recipe review and idempotency.
