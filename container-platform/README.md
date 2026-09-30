# Container Platform

## What I built

Containerized **15–20 services** with Docker and Kubernetes: standardized Dockerfiles,
Kubernetes manifests, health checks, and resource limits across dev, staging, and production.

## Impact

- Consistent builds — the same image runs on a laptop, in staging, and in production
- Faster onboarding — new services start from a standard deployment template
- Health probes and resource limits reduced noisy-neighbor incidents

## Demo code

- `Dockerfile` — multi-stage build for a Python service (small, reproducible runtime image)
- `k8s/deployment.yaml` — Deployment + Service template with liveness/readiness probes and resource limits
- `healthcheck.py` — minimal HTTP health probe for CI smoke tests (`python healthcheck.py --url http://localhost:8000/health`)

> Generic recreations for illustration.
