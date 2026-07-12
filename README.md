# Document Intelligence API

A production-oriented FastAPI project built to learn the fundamentals of backend development for AI applications. This project focuses on request handling, validation, file uploads, and API documentation before introducing LLMs, RAG, or document parsing.

---

## Purpose

Build a solid FastAPI foundation for future AI systems by understanding how APIs receive, validate, and process client requests.

---

## Problem Solved

AI applications require a reliable backend that can:

- Accept client requests
- Validate incoming data
- Receive uploaded documents
- Return structured JSON responses
- Expose well-documented APIs

This project implements these core backend capabilities.

---

## Features

- Health check endpoint
- Request validation using Pydantic
- Automatic OpenAPI documentation
- Interactive Swagger UI
- File upload support
- File metadata extraction
- File size calculation
- File byte preview

---

## API Endpoints

### GET `/health`

Checks whether the API is running.

#### Response

```json
{
    "status": "healthy"
}
```

---

### POST `/analyze`

Accepts text and returns its word count.

#### Request

```json
{
    "text": "FastAPI makes backend development simple."
}
```

#### Response

```json
{
    "word_count": 5
}
```

---

### POST `/upload`

Uploads a document and returns metadata.

#### Response

```json
{
    "filename": "sample.pdf",
    "content_type": "application/pdf",
    "size_in_bytes": 25341,
    "preview": "b'%PDF-1.7...'"
}
```

---

## Project Structure

```
document-intelligence-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
│
├── .venv/
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- python-multipart
- uv

---

## How to Run

### Clone Repository

```bash
git clone <repository-url>
cd document-intelligence-api
```

### Install Dependencies

```bash
uv sync
```

### Start Development Server

```bash
uv run uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

OpenAPI Specification

```
http://127.0.0.1:8000/openapi.json
```

---

## Example Requests

### Health Check

```bash
curl http://127.0.0.1:8000/health
```

---

### Analyze Text

```bash
curl -X POST \
http://127.0.0.1:8000/analyze \
-H "Content-Type: application/json" \
-d "{\"text\":\"Hello FastAPI\"}"
```

---

### Upload File

```bash
curl -X POST \
http://127.0.0.1:8000/upload \
-F "file=@sample.pdf"
```

---

## Engineering Concepts Learned

- FastAPI application object
- ASGI architecture
- Uvicorn server
- Route handlers
- HTTP GET vs POST
- Decorators
- Request lifecycle
- Pydantic models
- Automatic request validation
- JSON serialization
- Multipart form-data
- UploadFile
- Async route handlers
- Swagger/OpenAPI generation

---

## Key Learnings

- FastAPI automatically generates OpenAPI documentation.
- Pydantic validates incoming request data without manual checks.
- UploadFile efficiently handles uploaded files.
- FastAPI converts Python dictionaries into JSON responses.
- Async endpoints are well suited for I/O-bound AI workloads.
- Clear separation between routes and data models improves maintainability.

---

## Future Improvements

- PDF text extraction
- DOCX support
- Document summarization
- Named entity extraction
- OCR integration
- Embedding generation
- Vector database integration
- Retrieval-Augmented Generation (RAG)
- LLM-powered document analysis
- Authentication and authorization

---

## Repository Goals

This project is part of a project-first AI Engineering curriculum.

The objective is not only to build a working API, but also to understand:

- every file,
- every dependency,
- every engineering decision,
- and every architectural trade-off,

so the entire application can be rebuilt from scratch without referring to the source code.

---

## License

This project is intended for educational and portfolio purposes.