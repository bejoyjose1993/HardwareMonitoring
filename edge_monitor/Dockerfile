# Use official Python image
FROM python:3.11-slim

# Set workdir inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy only dependency files first (for caching)
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy source code
COPY src/ ./src/

# Set PYTHONPATH so that Python finds the package
ENV PYTHONPATH=/app/src

# Run as CLI
ENTRYPOINT ["python", "-m", "edge_monitor"]