# Python Project Setup with UV

This tutorial will guide you through setting up a Python project using `uv` with common data science dependencies.

## What is UV?

UV is an extremely fast Python package installer and resolver written in Rust. It's a drop-in replacement for pip and pip-tools that can be 10-100x faster.

## Prerequisites

- Python 3.12.1 (already installed)
- UV installed on your system

## Step 1: Install UV

If you haven't installed UV yet, install it using one of these methods:

### macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Alternative (using pip):
```bash
pip install uv
```

### Verify installation:
```bash
uv --version
```

## Step 2: Create a New Project

Navigate to your desired directory and create a new project:

```bash
# Create a new project directory
mkdir my-data-project
cd my-data-project

# Initialize a new UV project
uv init
```

This creates a basic project structure with a `pyproject.toml` file.

## Step 3: Set Python Version

Ensure you're using Python 3.12.1:

```bash
uv python pin 3.12.1
```

This creates a `.python-version` file that locks your project to Python 3.12.1.

## Step 4: Add Dependencies

Add the data science dependencies you need:

```bash
# Add core data science libraries
uv add jupyter pandas scikit-learn

# Optional: Add additional common libraries
uv add numpy matplotlib seaborn
```

This will:
- Update your `pyproject.toml` with the dependencies
- Create/update `uv.lock` with resolved versions
- Install packages in a virtual environment

## Step 5: Verify Installation

Check that everything is installed correctly:

```bash
# Activate the virtual environment (UV does this automatically in commands)
# But you can also activate manually:
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

# Verify packages
uv pip list
```

## Step 6: Start Jupyter

Launch Jupyter to start working:

```bash
# Run jupyter using UV (automatically uses the project's environment)
uv run jupyter notebook

# Or if you activated the venv:
jupyter notebook
```

## Project Structure

Your project should now look like this:

```
my-data-project/
├── .python-version      # Python version lock
├── .venv/              # Virtual environment
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Locked dependency versions
└── README.md          # Project documentation
```

## Working with the Project

### Running Python scripts:
```bash
uv run python script.py
```

### Running Jupyter:
```bash
uv run jupyter notebook
```

### Adding more dependencies:
```bash
uv add package-name
```

### Removing dependencies:
```bash
uv remove package-name
```

### Updating dependencies:
```bash
uv lock --upgrade
```

## Example pyproject.toml

Your `pyproject.toml` should look something like this:

```toml
[project]
name = "my-data-project"
version = "0.1.0"
description = "Data science project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "jupyter>=1.0.0",
    "pandas>=2.0.0",
    "scikit-learn>=1.3.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Quick Start Script

Create a `start.sh` script for easy setup:

```bash
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
```

Make it executable:
```bash
chmod +x start.sh
./start.sh
```

## Benefits of UV

1. **Speed**: 10-100x faster than pip
2. **Reproducibility**: `uv.lock` ensures consistent installs
3. **Simplicity**: Single command for most operations
4. **Disk efficient**: Smart caching of packages
5. **Drop-in replacement**: Works with existing pip workflows

## Common Commands Cheat Sheet

| Task | Command |
|------|---------|
| Create new project | `uv init` |
| Add dependency | `uv add package` |
| Remove dependency | `uv remove package` |
| Install all dependencies | `uv sync` |
| Run script | `uv run python script.py` |
| Run command in venv | `uv run command` |
| Update dependencies | `uv lock --upgrade` |
| List installed packages | `uv pip list` |

## Troubleshooting

### Issue: UV not found after installation
**Solution**: Restart your terminal or run:
```bash
source $HOME/.cargo/env
```

### Issue: Wrong Python version
**Solution**:
```bash
uv python pin 3.12.1
uv sync
```

### Issue: Dependencies conflict
**Solution**:
```bash
uv lock --upgrade
uv sync
```

## Next Steps

1. Create a `notebooks/` directory for Jupyter notebooks
2. Create a `src/` directory for Python modules
3. Add a `.gitignore` file (UV creates one by default)
4. Initialize git repository: `git init`
5. Start coding!

## Additional Resources

- UV Documentation: https://docs.astral.sh/uv/
- UV GitHub: https://github.com/astral-sh/uv
- Python Packaging Guide: https://packaging.python.org/
