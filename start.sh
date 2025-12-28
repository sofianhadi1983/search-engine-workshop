#!/bin/bash
# Quick start script

# Install UV if not present
if ! command -v uv &> /dev/null; then
    echo "Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Pin Python version
uv python pin 3.12.1

# Install dependencies
uv sync

# Start Jupyter
uv run jupyter notebook
