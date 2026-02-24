---
title: "LLM-as-judge Evaluation"
stage: trial
category: AI Tooling Setup
description: "Using a powerful LLM to evaluate quality of outputs from another LLM. Scales automated quality assessment but requires careful calibration."
strategic_value: supporting
devops_phases: [test, monitor]
---

# LLM-as-Judge Evaluation

## Problem

How do you objectively evaluate the quality, correctness, and safety of thousands of AI-generated code snippets or modernization plans without creating a massive manual review bottleneck for your senior developers?

*This problem is difficult because:*

- Human evaluation (manually reading and scoring every line of AI-generated code) is slow, expensive, and subjective—different reviewers will have different standards for "good" or "idiomatic" code.
- Traditional "pass/fail" unit tests are not enough to judge "quality," "style," "maintainability," or "architectural alignment."
- Scaling modernization involves generating thousands of pull requests; manual review of all of them would negate the speed gains of using AI in the first place.
- LLMs can produce code that is "technically correct" (it runs) but violates subtle project-specific security rules or architectural patterns that only an expert would notice.

*Yet, solving this problem is feasible because:*

- A powerful, independent LLM (e.g., GPT-5.3-Codex or Claude Sonnet 4.6) can be used as a "Judge" to evaluate the outputs of a smaller, faster model against a detailed rubric.
- LLM-as-a-Judge can provide structured, consistent scores and detailed reasoning for its evaluations, making its decisions auditable and tunable.
- Automated "evaluations" (evals) can run in parallel across thousands of samples, providing immediate feedback on model or prompt changes during a modernization project.

## Solution

Deploy an "LLM Judge" to perform the first pass of quality assessment for all AI-generated modernization outputs:

1. **Define a detailed Rubric** — Create a clear, multi-dimensional scoring guide for the judge (e.g., "Score 1-5 on Correctness, Idiomaticness, Security, and Architectural Alignment"). Provide examples of "good" and "bad" outputs (few-shot prompting).
2. **Use a "frontier" model as the Judge** — Always use a more capable model for judging than the one that produced the output (e.g., use Claude 3.5 Sonnet to judge an output from Claude 3 Haiku).
3. **Task the Judge with providing "Reasoning"** — Instruct the judge to output a JSON object containing both the score and a detailed explanation of its reasoning. This makes the evaluation auditable.
4. **Calibrate against human labels** — Have a senior developer review a small subset (e.g., 50-100) of the judge's evaluations to ensure they correlate with human expert judgment.
5. **Implement "A/B" and "Regression" testing** — Use the judge to compare the performance of different prompts or models on a "golden set" of modernization tasks.

**Common Judge evaluation criteria:**

- **Correctness** — Does the code actually solve the problem? (Often combined with test execution).
- **Idiomaticness** — Does the code follow the target language's modern patterns and style?
- **Security** — Are there any obvious vulnerabilities (e.g., SQL injection, hardcoded secrets) in the new code?
- **Architectural Alignment** — Does the code respect the boundaries defined in the **Anti-Corruption Layer**?
- **Completeness** — Did the agent complete all steps of the plan?

## Tradeoffs

**Pros:**

- Dramatically scales the quality assessment of AI-generated code, enabling a much faster modernization loop.
- Provides a consistent, objective standard for "quality" that is not subject to human reviewer fatigue or individual bias.
- Enables rapid iteration on prompts and models by providing immediate feedback on the impact of changes.

**Cons:**

- Judge LLMs have their own biases (e.g., "Self-preference bias" where a model rates its own outputs higher, or "Position bias" where it prefers the first option in a list).
- Costs can be significant if using a frontier model (like GPT-4o) to judge every single output.

**Difficulties:**

- Developing a rubric that is precise enough to be useful without being so rigid that it misses creative, correct solutions.
- Ensuring the judge has enough "global context" of the codebase to make accurate architectural judgments.

## Rationale

Modernization is a high-volume activity. If we only rely on human review, the human is the bottleneck. If we only rely on unit tests, we miss the "soft" qualities of the code (style, architecture, security) that are critical for long-term maintainability. LLM-as-a-Judge provides the middle ground: it offers a scalable, nuanced "expert-level" review that can handle 90% of the routine quality assessment, freeing up human experts for the final 10% of high-stakes decisions.

## Known Uses

- [MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) — foundational research on using LLMs to evaluate other LLMs in conversational contexts.
- [RAGAS](https://docs.ragas.io/) — an open-source framework specifically for using LLM-as-a-Judge to evaluate RAG (Retrieval-Augmented Generation) pipelines.
- [Anthropic — Evaluations guide](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests) — practical guidance on building and running automated evaluations for agentic systems.

## References

- [LlamaIndex — Evaluation](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluation/) — tools and patterns for evaluating LLM-based applications.
- [LangSmith — Evaluation](https://docs.smith.langchain.com/concepts/evaluation) — a platform for tracking and evaluating LLM workflows.

## Related Patterns

- [Human in the Loop](../human-in-the-loop/) — LLM-as-a-Judge is the primary assistant for the human reviewer, performing the first pass of quality control.
- [AI-powered Code Review](../ai-powered-code-review/) — the "Judge" is the engine that drives the automated code review bot.
- [LLM Observability & Tracing](../llm-observability-and-tracing/) — the evaluation scores from the judge are a key metric to track in an observability platform.

## What Next

After establishing a basic evaluation rubric, implement [LLM Observability & Tracing](../llm-observability-and-tracing/) to track your judge's scores over time and identify which modules are the hardest for your agents to modernize correctly.

## Staging History

**Trial (Feb 2026):** LLM-as-a-Judge is being trialed to scale the quality assessment of agentic modernization outputs. Early results show high correlation with human expert judgment for routine tasks, but teams are still calibrating rubrics for complex architectural decisions.
