FROM mcr.microsoft.com/devcontainers/python:{{ cookiecutter.python_version }}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"
ENV UV_LINK_MODE=copy

RUN pip install --no-cache-dir pre-commit

WORKDIR /workspace
