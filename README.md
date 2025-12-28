# Search Engine Workshop

A hands-on workshop project for learning how vector databases and text search engines work under the hood. This project demonstrates the fundamental concepts behind modern search systems using practical examples with real course documentation data.

## What This Project Does

This workshop teaches you how search engines transform text into searchable vectors using two main approaches:

**Bag of Words with CountVectorizer**: Converts documents into numerical vectors by counting word occurrences. Each document becomes a vector where dimensions represent unique words in the vocabulary.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: A more sophisticated approach that weights words based on how frequently they appear in a document versus how rare they are across all documents. This helps identify the most meaningful words that characterize each document.

The project uses real data from DataTalks.Club Zoomcamp courses, containing questions and answers from multiple courses like Data Engineering Zoomcamp and MLOps Zoomcamp.

## Why This Project Exists

Before using vector databases like Pinecone, Weaviate, or Milvus, it's crucial to understand how they work internally. This project demystifies the "magic" behind vector search by implementing the core concepts from scratch using scikit-learn.

**What you'll learn:**

- How text documents are converted into numerical vectors
- The concept of vector spaces and term-document matrices
- Why some words are more important than others (TF-IDF)
- How sparse matrices efficiently represent text data
- The mathematical foundation behind semantic search

Understanding these fundamentals will make you more effective when working with modern vector databases and LLM-powered search systems.

## Setup Instructions

### Prerequisites

- GitHub account
- Basic knowledge of Python and Jupyter notebooks

### Setup in GitHub Codespaces

GitHub Codespaces provides a complete development environment in your browser.

**Step 1: Create a Codespace**

1. Fork or clone this repository to your GitHub account
2. Click the green "Code" button on the repository page
3. Select the "Codespaces" tab
4. Click "Create codespace on main"
5. Wait for the container to build (first time takes 2-3 minutes)

**Step 2: Install UV**

UV is an extremely fast Python package installer and resolver written in Rust. It's a drop-in replacement for pip and pip-tools that can be 10-100x faster.

**Why UV?**
- Speed: 10-100x faster than pip
- Reproducibility: `uv.lock` ensures consistent installs across different environments
- Simplicity: Single command for most operations
- Disk efficient: Smart caching of packages
- Drop-in replacement: Works with existing pip workflows

Open the terminal in Codespaces and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternative installation using pip:
```bash
pip install uv
```

After installation, restart your terminal or run:

```bash
source $HOME/.cargo/env
```

Verify installation:

```bash
uv --version
```

**Step 3: Install Dependencies**

The project uses Python 3.12.1 with several data science libraries. Install everything with one command:

```bash
uv sync
```

This command reads `pyproject.toml` and `uv.lock` to install exact versions of all dependencies including:
- Jupyter for interactive notebooks
- Pandas for data manipulation
- Scikit-learn for machine learning and text vectorization

**Step 4: Start Jupyter Notebook**

Launch Jupyter to start exploring:

```bash
uv run jupyter notebook
```

Or use the quick start script:

```bash
./start.sh
```

The notebook will open in your browser. Open `playground.ipynb` to begin the workshop.

### Alternative: Quick Start Script

If you want everything automated:

```bash
chmod +x start.sh
./start.sh
```

This script will:
1. Install UV if not present
2. Pin the correct Python version
3. Install all dependencies
4. Launch Jupyter notebook

## Project Structure

```
search-engine-workshop/
├── playground.ipynb         # Main workshop notebook with examples
├── main.py                  # Simple Python entry point
├── pyproject.toml          # Project dependencies and configuration
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version specification (3.12.1)
└── start.sh                # Quick start automation script
```

## Workshop Content

The `playground.ipynb` notebook contains:

**Part 1: Data Loading**
- Fetching course documentation from remote JSON
- Structuring data into pandas DataFrames
- Exploring the dataset

**Part 2: Bag of Words**
- Converting text to vectors using CountVectorizer
- Understanding term-document matrices
- Working with sparse matrices
- Filtering stopwords and rare terms

**Part 3: TF-IDF Concepts**
- Understanding Term Frequency and Inverse Document Frequency
- Real-world analogies (restaurant menus, resumes, dating profiles)
- Why TF-IDF improves search relevance

## Working with UV

UV is the package manager for this project. Here are common commands:

### Command Cheat Sheet

| Task | Command |
|------|---------|
| Install all dependencies | `uv sync` |
| Add dependency | `uv add package-name` |
| Remove dependency | `uv remove package-name` |
| Update dependencies | `uv lock --upgrade` |
| Run Python script | `uv run python script.py` |
| Run Jupyter | `uv run jupyter notebook` |
| Run any command in venv | `uv run command` |
| List installed packages | `uv pip list` |
| Pin Python version | `uv python pin 3.12.1` |

### Virtual Environment

UV automatically creates and manages a virtual environment in `.venv/`. You can activate it manually if needed:

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

However, it's recommended to use `uv run` commands instead, which automatically use the project's environment.

## Local Development (Outside Codespaces)

If you want to run this locally instead of Codespaces:

1. Ensure Python 3.12.1 is installed
2. Clone the repository
3. Install UV using the installation command above
4. Run `uv sync` to install dependencies
5. Run `uv run jupyter notebook` to start working

## Learning Path

1. Start with `playground.ipynb` and run cells sequentially
2. Experiment with different CountVectorizer parameters
3. Try changing `min_df` to see how vocabulary size changes
4. Explore the TF-IDF explanations and analogies
5. Modify the code to work with your own text data

## Next Steps

After completing this workshop, you'll be ready to:

- Work with production vector databases like Pinecone or Weaviate
- Understand embedding models and semantic search
- Build RAG (Retrieval-Augmented Generation) systems
- Implement custom search solutions for your applications

## Resources

- UV Documentation: https://docs.astral.sh/uv/
- UV GitHub: https://github.com/astral-sh/uv
- Python Packaging Guide: https://packaging.python.org/
- Scikit-learn Text Feature Extraction: https://scikit-learn.org/stable/modules/feature_extraction.html
- DataTalks.Club: https://datatalks.club/

## Troubleshooting

**Issue: UV command not found after installation**

Solution: Restart your terminal or run:
```bash
source $HOME/.cargo/env
```

**Issue: Wrong Python version**

Solution:
```bash
uv python pin 3.12.1
uv sync
```

**Issue: Dependencies conflict**

Solution:
```bash
uv lock --upgrade
uv sync
```

**Issue: Jupyter kernel not found**

Solution: Make sure you're running Jupyter with `uv run jupyter notebook`, not the system Jupyter

## Contributing

This is a learning project. Feel free to experiment, modify, and extend it for your own learning purposes.

## License

Educational project for learning purposes.
