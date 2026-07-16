# Contributing to InterviewPrep CLI

Contributions are welcome. If you have an idea for a feature or found a bug, 
please open an issue first to discuss it.

## Setup

```bash
git clone https://github.com/aldohl95/InterviewPrepCli.git
cd InterviewPrepCli
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]" --no-build-isolation
```

## Before submitting a PR

- Run tests: `pytest`
- Run formatter: `black src/ tests/`
- Run linter: `ruff check src/ tests/`
- Write tests for new functionality
- Update the README if user-facing behavior changes

## Code style

- Follow the existing patterns in the codebase
- Keep functions small and focused
- Prefer readability over cleverness