---
title: "LLM-as-judge Evaluation"
stage: assess
category: LLM Infrastructure
description: "Using a powerful LLM to evaluate quality of outputs from another LLM. Scales automated quality assessment but requires careful calibration."
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
