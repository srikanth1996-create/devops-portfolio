# CI/CD Pipeline Automation

## What I built

Designed, built, and operated CI/CD pipelines serving **20–25 applications and services**
for a team of roughly 15–25 engineers. Pipelines ran on **Jenkins** (primary) with
**GitHub Actions** for newer services.

## Impact

- Deployment time: **1–2 hours → 15–30 minutes**
- Standardized build → test → deploy stages across all services
- Automated quality gates (unit tests, lint, image vulnerability scan) before every deploy

## How it worked

1. Developer pushes → webhook triggers the pipeline
2. Build stage compiles/tests the service and builds a Docker image
3. Quality gates: unit tests, lint, image scan — any failure stops the deploy
4. Deploy stage rolls out to staging, runs smoke tests, then promotes to production
5. Team channel notified on success/failure

## Demo code

- `Jenkinsfile` — declarative pipeline recreating the stage structure
- `.github/workflows/deploy.yml` — equivalent GitHub Actions workflow
- `deploy_helper.py` — small Python helper that promotes an image tag and waits for the rollout to report healthy

> Generic recreations for illustration, not production pipeline code.
