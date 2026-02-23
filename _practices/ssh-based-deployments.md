---
title: "SSH-based Deployments"
stage: remove
category: Architecture & Delivery
description: "Manually deploying via SSH scripts. No audit trail, no rollback, incompatible with any AI-assisted or automated delivery pipeline."
---

## Why Remove

SSH deployments are manual, error-prone, and invisible to any automation. There is no atomic rollback, no deployment history, no way for an AI agent to participate in the delivery process, and no consistent state guarantee.

## Migration Path

1. Wrap existing SSH scripts in a CI/CD pipeline job (minimum viable improvement)
2. Containerize the application
3. Move to [CI/CD Pipelines](/technologies/ci-cd-pipelines/) with a proper deploy step
4. Adopt [GitOps](/technologies/gitops/) for declarative, auditable deployments

## Risks of Keeping It

- Anyone with SSH access can deploy anything at any time — no governance
- "Works on my machine" deployments create environment drift
- Debugging production issues is harder without deployment records
- Incompatible with feature flags, canary releases, or AI-assisted change

## Exception

Debugging sessions that SSH into a running box are different — that's acceptable for investigation. The anti-pattern is using SSH as the deployment mechanism itself.
