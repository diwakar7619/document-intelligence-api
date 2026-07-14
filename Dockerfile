FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv
ENV UV_PROJECT_ENVIRONMENT=/usr/local
RUN uv sync --frozen 
COPY . .
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Docker cache demo