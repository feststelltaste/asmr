---
title: "Feature Flags"
stage: apply
category: Architecture & Delivery
description: "Runtime toggles to release code to subsets of users without deployments. Essential for safely rolling out AI-generated changes incrementally."
---

## Overview

Feature flags decouple deployment from release. Code ships to production but runs only for a configured subset of users or environments. This makes trunk-based development safe and enables gradual rollouts, A/B testing, and instant rollbacks without re-deploys.

## Why They Matter for AI-assisted Development

AI-generated code can be deployed behind a flag:
- Enable for internal users first; verify before broader rollout
- Instantly disable if problems are detected in production
- Run the old and new implementation side-by-side for comparison
- Canary releases with automated rollback if error rates rise

## Tools

- **LaunchDarkly** — Mature, full-featured, managed
- **Unleash** — Open-source, self-hostable
- **Flagsmith** — Open-source, cloud or self-hosted
- **OpenFeature** — Open standard SDK for feature flagging (CNCF)
- **Homegrown** — Environment variables or DB-backed flags (simple, limited)

## Risks & Considerations

- Flag debt: old flags left in code become permanent complexity — enforce flag retirement
- Testing matrix explodes with many flags — be selective
- Flag evaluation must be fast (in-memory or edge-cached) to avoid adding latency
