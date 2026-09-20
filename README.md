# DevOps Task Manager

A deliberately small API used to practice the entire DevOps lifecycle. Its job is to manage tasks; your job is to progressively build, ship, secure, observe, and operate it.

## Milestone 1: run it locally

Prerequisites: Python 3.12+ for the direct option, or Docker Desktop for the container option.

### Direct Python run (SQLite)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` to use the interactive API documentation.

### Docker Compose run (PostgreSQL)

```powershell
docker compose up --build
```

In a second terminal:

```powershell
Invoke-RestMethod http://localhost:8000/health
Invoke-RestMethod http://localhost:8000/tasks -Method Post -ContentType "application/json" -Body '{"title":"Learn Docker"}'
```

Stop containers with `docker compose down`. Add `-v` only when you intentionally want to delete the local database volume.

## Your DevOps learning path

1. **Application and Git:** run tests, create a Git repository, work with branches and pull requests.
2. **Docker:** inspect images, logs, networks, volumes, and rebuild after a code change.
3. **CI:** add GitHub Actions to run tests and build the image for every pull request.
4. **Registry:** publish the image to Amazon ECR, using short-lived AWS credentials through OIDC.
5. **Terraform:** provision VPC, ECR, RDS, EKS, IAM, and remote state in AWS.
6. **Kubernetes:** create Deployment, Service, ConfigMap, Secret, Ingress, resource limits, probes, and HPA.
7. **CD:** safely deploy an image tag to EKS, then practice rollout status and rollback.
8. **Operations:** add structured logs, metrics, alerts, dashboards, backups, and runbooks.

Each milestone should be understood and verified before moving to the next one. We will build the next milestone after you can run this locally.
