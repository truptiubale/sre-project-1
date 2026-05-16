# SRE Project 1 — Containerised Flask App

My first SRE project. A Python Flask API containerised with Docker,
monitored with Prometheus, and visualised with Grafana.

## What this project demonstrates
- Containerising an app with Docker
- Multi-service orchestration with Docker Compose
- Health check endpoints (SRE best practice)
- Metrics collection with Prometheus
- Dashboarding with Grafana
- Basic test coverage

## Project structure
```
sre-project-1/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # How to build the Docker image
├── docker-compose.yml   # All services (app + db + monitoring)
├── prometheus.yml       # Prometheus scrape config
├── .dockerignore        # Files excluded from the image
└── tests/
    └── test_app.py      # Automated tests
```

## Services
| Service    | URL                   | Purpose                  |
|------------|-----------------------|--------------------------|
| Flask app  | http://localhost:5000 | Main application         |
| Prometheus | http://localhost:9090 | Metrics collection       |
| Grafana    | http://localhost:3000 | Dashboards (admin/admin) |
| PostgreSQL | localhost:5432        | Database                 |

## API Endpoints
| Endpoint  | Description                          |
|-----------|--------------------------------------|
| /         | App info and status                  |
| /health   | Health check (used by monitoring)    |
| /info     | App metadata                         |
| /metrics  | Prometheus metrics (auto-generated)  |

## How to run

### Requirements
- Docker Desktop installed
- Git

### Start everything
```bash
git clone https://github.com/YOUR_USERNAME/sre-project-1
cd sre-project-1
docker compose up
```

### Run tests
```bash
pip install flask pytest prometheus-flask-exporter
pytest tests/ -v
```

### Stop everything
```bash
docker compose down
```

## SLO (Service Level Objectives)
| SLI            | Target | Measurement               |
|----------------|--------|---------------------------|
| Availability   | 99.5%  | /health returns 200       |
| Latency (p95)  | <200ms | flask_request_duration    |
| Error rate     | <0.5%  | 5xx responses / total     |

## What I learned
- How Docker images are built layer by layer
- Why `COPY requirements.txt` comes before `COPY . .` (build cache)
- How services communicate inside Docker using service names as hostnames
- The difference between `EXPOSE` (documentation) and port mapping (actual)
- How Prometheus scrapes a `/metrics` endpoint automatically
- What SLOs are and how to define them for a service
