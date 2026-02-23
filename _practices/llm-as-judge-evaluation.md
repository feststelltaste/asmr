---
title: "LLM-as-judge Evaluation"
stage: trial
category: AI Tooling Setup
description: "Using a powerful LLM to evaluate quality of outputs from another LLM. Scales automated quality assessment but requires careful calibration."
strategic_value: supporting
devops_phases: [test, monitor]
---

## Overview

Human evaluation of LLM outputs is expensive and slow. LLM-as-judge uses a capable model (often GPT-4 or Claude) to evaluate another model's outputs against criteria: correctness, completeness, style, safety. It scales quality assessment across thousands of samples.

## Use Cases

- Evaluating generated code quality and correctness
- Scoring documentation for accuracy and clarity
- Comparing two model outputs head-to-head (A/B)
- Regression testing after model or prompt changes

## Best Practices

- Use explicit, detailed rubrics with examples (few-shot prompting)
- Calibrate against human labels before trusting at scale
- Watch for **position bias** (LLM judges prefer first option)
- Watch for **self-preference bias** (a model rates its own outputs higher)
- Use structured output (scores + reasoning) for auditability

## Risks & Considerations

- Judge LLMs have biases that correlate poorly with human judgment on some tasks
- Expensive if running a powerful judge on every output
- Cannot replace human evaluation for high-stakes decisions

## Resources

- [MT-Bench and Chatbot Arena paper](https://arxiv.org/abs/2306.05685) — foundational LLM-as-judge research
- [RAGAS — RAG evaluation framework](https://docs.ragas.io/) — LLM-as-judge evaluation for RAG pipelines
- [Anthropic — Evaluations guide](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests) — practical guidance on building evals
- [YouTube — LLM-as-judge evaluation explained](https://www.youtube.com/results?search_query=llm+as+judge+evaluation+ai+quality+2025)
