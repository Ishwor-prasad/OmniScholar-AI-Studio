# ==============================================================================
# OmniScholar AI Studio - Production Dockerfile
# Autonomous Empirical Research Operating System & Typesetting Engine
# ==============================================================================
FROM python:3.11-slim

# Prevent Python from writing .pyc and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Install system dependencies and native Typst compiler (v0.12.0)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    xz-utils \
    ca-certificates \
    && curl -fsSL https://github.com/typst/typst/releases/download/v0.12.0/typst-x86_64-unknown-linux-musl.tar.xz | tar -xJ \
    && cp typst-*/typst /usr/local/bin/typst \
    && chmod +x /usr/local/bin/typst \
    && rm -rf typst* \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Verify typst installation
RUN typst --version

WORKDIR /app

# Copy dependency definition and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy source tree
COPY . /app/

# Expose server port
EXPOSE 8000

# Start production server
CMD ["python", "main.py"]

