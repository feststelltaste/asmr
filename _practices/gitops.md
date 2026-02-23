---
title: "GitOps"
stage: apply
category: Architecture & Delivery
description: "Git as the single source of truth for infrastructure and deployments. Enables audit trails and reproducibility essential for AI-assisted change."
---

## Overview

GitOps treats infrastructure and application deployment configuration as code stored in Git. A GitOps controller (ArgoCD, Flux) continuously reconciles the cluster state with what's declared in the repo. All changes flow through Git — and therefore through review and CI.

## Why It Matters for Agentic AI

When AI agents propose infrastructure or deployment changes, GitOps ensures:
- All changes are reviewable before applying
- The change history is auditable
- Drift between desired and actual state is detected automatically
- Rollback is a `git revert` away

## Tools

- **ArgoCD** — Kubernetes-native GitOps, excellent UI
- **Flux** — Lightweight, CNCF graduated project
- **Helm + ArgoCD** — Common combination for Kubernetes application delivery

## Risks & Considerations

- Requires disciplined Git hygiene — direct cluster mutations break the model
- Secrets management needs special handling (never store plaintext secrets in Git)
- GitOps is Kubernetes-centric; applying the pattern to other infrastructure varies
