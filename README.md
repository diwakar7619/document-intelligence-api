# 📄 Document Intelligence API

A production-style REST API built with **FastAPI** and containerized using **Docker**. The project demonstrates modern backend engineering practices including dependency management with `uv`, containerization, Docker Compose, and reproducible development environments.

---

## Features

- FastAPI REST API
- Health check endpoint
- Text analysis endpoint
- File upload endpoint
- Interactive Swagger UI
- Dockerized application
- Docker Compose support
- Reproducible dependency management using `uv`

---

## Live Deployment

API Base URL:
https://document-intelligence-api-production-d8dc.up.railway.app

### Endpoints

- `/health`
- `/docs`
- `/analyze`
- `/upload`

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Docker
- Docker Compose
- uv

---

## Project Structure

```text
document-intelligence-api/
│
├── app/
│   ├── main.py
│   └── ...
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/analyze` | Analyze text |
| POST | `/upload` | Upload a document |

---

## Running Locally

### Clone the repository

```bash
git clone https://github.com/diwakar7619/document-intelligence-api.git
cd document-intelligence-api
```

### Install dependencies

```bash
uv sync
```

### Start the API

```bash
uv run uvicorn app.main:app --reload
```

Visit:

```
http://localhost:8000/docs
```

---

# Running with Docker

Build the image

```bash
docker build -t document-intelligence-api:1.0 .
```

Run the container

```bash
docker run -p 8000:8000 document-intelligence-api:1.0
```

Open

```
http://localhost:8000/docs
```

---

# Running with Docker Compose

Start

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

## Docker Architecture

```
Client
    │
    ▼
Docker Container
    │
    ▼
FastAPI
    │
    ▼
Business Logic
```

---

## Engineering Concepts Demonstrated

- Docker Images
- Docker Containers
- Layer Caching
- Build Context
- Docker Compose
- Port Mapping
- Environment Isolation
- Reproducible Builds
- Dependency Management with `uv`

---

## Lessons Learned

- Containerize applications for consistent execution across environments.
- Optimize Dockerfiles using layer caching.
- Use Docker Compose to manage application services.
- Keep dependencies reproducible with lock files.
- Separate development environment from runtime environment.

---

## Future Improvements

- CI/CD pipeline
- Multi-stage Docker builds
- Non-root containers
- Health checks
- Railway deployment
- Authentication
- Database integration

---

## Author

**Pratham Diwakar**

GitHub: https://github.com/diwakar7619