---
title: "CI/CD Pipelines"
stage: apply
category: Architecture & Delivery
description: "Automated build, test, and deployment pipelines. Non-negotiable for any modernization project — required before AI agents can safely merge code."
strategic_value: supporting
devops_phases: [build, test, release, deploy]
---

## Overview

CI/CD pipelines automate building, testing, and deploying software. They are the foundation that makes all other modernization work safe: without them, AI-generated code has no automated quality gate before reaching production.

## Why It Matters for AI-assisted Development

AI agents produce code that needs verification. A CI/CD pipeline is the automated referee:
- Runs the test suite on every AI-generated PR
- Enforces linting, type checking, security scanning
- Provides a clear pass/fail signal the agent can react to
- Prevents untested AI changes from reaching production

## Tooling

- **GitHub Actions** — Integrated, generous free tier, huge ecosystem
- **GitLab CI** — Full DevOps platform, self-hosted option
- **Jenkins** — Mature, highly customizable, complex to maintain
- **Buildkite** — Fast, scalable, hybrid cloud/on-prem

## Essential Pipeline Steps for Modernization

1. Build & compile
2. Unit + integration tests
3. Static analysis (linting, type checking)
4. Security scanning (SAST, dependency vulnerabilities)
5. Deploy to staging
6. Smoke/contract tests

## Risks & Considerations

- Slow pipelines discourage running them; optimize for feedback speed
- Flaky tests erode trust in the pipeline faster than almost anything else

## Resources

- [GitHub Actions documentation](https://docs.github.com/en/actions) — getting started with CI/CD workflows
- [Martin Fowler — Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) — foundational principles
- [DORA metrics](https://dora.dev/) — measuring software delivery performance
