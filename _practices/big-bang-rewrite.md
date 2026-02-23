---
title: "Big Bang Rewrite"
stage: stop
category: Legacy Modernization
description: "Complete rewrites from scratch. Almost always fail to capture edge-case business logic. Prefer incremental modernization strategies."
strategic_value: generic
---

## Why Stop

The "second system" effect is well documented: rewrites take 3-5× longer than estimated, miss thousands of edge cases embedded in the original system, and frequently never go live — or launch to immediate regressions. Joel Spolsky's "Things You Should Never Do" (2000) remains accurate.

LLMs make this *slightly* less painful by helping write boilerplate faster, but they don't solve the fundamental problem: **you don't know what the old system actually does until you've studied it carefully**.

## What to Do Instead

- [Strangler Fig Pattern](/practices/strangler-fig-pattern/) — migrate incrementally
- [AI-assisted Legacy Code Reading](/practices/ai-assisted-legacy-code-reading/) — understand before rewriting
- [AI-generated Characterization Tests](/practices/ai-generated-characterization-tests/) — capture behavior before changing it
- [Database Decomposition](/practices/database-decomposition/) — decouple data ownership incrementally

## When Rewrites Are Justified

- The codebase is genuinely irreparable (no documentation, no tests, no original developers, no ability to run it)
- The domain is completely changing (not just technology)
- Scope is tightly bounded to a single, well-understood component — not the whole system

## Resources

- [Joel Spolsky — Things You Should Never Do](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) — the classic argument against rewrites
- [Martin Fowler — Is High Quality Software Worth the Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html) — the economic case for incremental improvement
- [YouTube — Why software rewrites fail](https://www.youtube.com/results?search_query=software+rewrite+failure+lessons+2025)
