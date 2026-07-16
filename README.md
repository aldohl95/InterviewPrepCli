# InterviewPrep CLI

A command-line application for organizing and optimizing technical interview preparation. Instead of tracking LeetCode problems, study notes, and review schedules across spreadsheets and multiple apps, everything lives in a single terminal-based tool with spaced repetition built in.

## Features

- **Problem Tracker** — full CRUD for practice attempts with problem name, pattern, difficulty, time taken, and self-assessment fields
- **Spaced Repetition Engine** — automatic scheduling of review dates based on personal difficulty and whether hints were used
- **Progress Dashboard** — aggregated statistics on problems solved, patterns practiced, and difficulty distribution
- **Daily Study Planner** — shows what's due for review today with streak tracking
- **Data Import / Export** — JSON-based backup and restore with merge and replace modes

## Installation

Requires Python 3.11 or higher.

```bash
git clone https://github.com/aldohl95/InterviewPrepCli.git
cd InterviewPrepCli
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install -e ".[dev]" --no-build-isolation
```

Verify the installation:

```bash
interviewprep --help
```

## Usage

### Adding a problem

```bash
interviewprep add
```

Walks through interactive prompts for problem name, pattern (e.g. "hash map"), LeetCode difficulty, personal difficulty (1–10), time taken, whether you needed help, and an optional recognition sentence.

### Listing all problems

```bash
interviewprep list
```

Displays a summary table with problem number, name, date attempted, personal difficulty, and whether it needs resolving.

### Viewing full details

```bash
interviewprep view 1
```

Shows every field for the numbered problem.

### Editing a problem

```bash
interviewprep edit 1
```

Prompts field-by-field with current values as defaults. Press Enter to keep any field unchanged.

### Deleting a problem

```bash
interviewprep delete 1
```

Confirmation prompt before deletion.

### Logging a new review

```bash
interviewprep review 1
```

Creates a new attempt record for an existing problem and calculates the next review date based on the spaced repetition algorithm.

### Progress dashboard

```bash
interviewprep dashboard
```

Displays statistics: total problems solved, breakdown by LeetCode difficulty, top patterns practiced, and problems still needing resolve.

### Daily study planner

```bash
interviewprep today
```

Shows problems due for review today, falls back to upcoming reviews if nothing is due, and tracks your daily streak.

### Exporting data

```bash
interviewprep export --output=backup.json
```

Writes all problems to a JSON file for backup.

### Importing data

```bash
interviewprep import --input=backup.json --mode=merge
interviewprep import --input=backup.json --mode=replace
```

Merge mode adds imported problems to existing data. Replace mode overwrites everything.

## Architecture

### Directory structure
### Full project structure

\`\`\`
interviewprep-cli/
├── src/
│   └── interviewprep/
│       ├── __init__.py
│       ├── cli.py           — Click entry point and command registration
│       ├── models.py        — Problem dataclass and LeetcodeDifficulty enum
│       ├── storage.py       — JSON persistence via platformdirs
│       ├── prompts.py       — shared interactive prompt logic
│       ├── scheduler.py     — spaced repetition algorithm
│       └── commands/        — one file per CLI command
│           ├── __init__.py
│           ├── add.py
│           ├── list.py
│           ├── view.py
│           ├── edit.py
│           ├── delete.py
│           ├── review.py
│           ├── dashboard.py
│           ├── today.py
│           ├── export.py
│           └── import_problems.py
│
├── tests/
│   ├── test_basic.py
│   ├── test_model.py
│   ├── test_storage.py
│   ├── test_scheduler.py
│   └── test_command.py
│
├── docs/
│   └── scheduler.md         — algorithm design and tradeoffs
│
├── README.md
├── SPEC.md
├── LICENSE
└── pyproject.toml           — project config, dependencies, tool settings
\`\`\`

### Data storage

Problems are stored as JSON at the platform-appropriate user data directory (via `platformdirs`):

- **Linux**: `~/.local/share/interviewprep/problems.json`
- **macOS**: `~/Library/Application Support/interviewprep/problems.json`
- **Windows**: `%LOCALAPPDATA%\interviewprep\problems.json`

### Spaced repetition

A custom piecewise algorithm designed for interview preparation. First reviews use gentle intervals (1 or 3 days). Subsequent reviews scale from 1 day (needed help or difficulty ≥ 8) up to 30 days (mastered). Full details in `docs/scheduler.md`.

## Design Decisions

Several deliberate tradeoffs are documented in-code and worth calling out:

- **JSON over SQLite** — chosen for simplicity and human-readable data. SQLite migration is noted as future work.
- **Custom scheduling algorithm over SM-2** — the industry-standard SM-2 algorithm was overkill for the expected data size. The custom algorithm is simpler to test, defend, and reason about.
- **Problem name as identifier** — prior attempts are looked up by name rather than by a separate ID system. Acceptable tradeoff for a single-user tool.
- **New attempts as separate records** — the `review` command creates new records rather than mutating existing ones, preserving history.
- **Edit does not recalculate schedules** — editing a problem is treated as metadata correction. Users who want to update their schedule should use `review` instead.

## Development

### Running tests

```bash
pytest
```

Current test count: **42 tests passing** across models, storage, scheduler, and all commands.

### Formatting and linting

```bash
black src/ tests/
ruff check src/ tests/
```

Configuration lives in `pyproject.toml`.

### Test coverage areas

- Data model validation (boundary values, invalid inputs)
- Storage round-trip (save then load produces equivalent data)
- Scheduler algorithm (every branch and boundary tested)
- Every CLI command (success paths and error cases)

## Future Work

- Migrate storage layer from JSON to SQLite for efficient querying
- Add CSV import/export format
- Refactor to split `Problem` (identity) from `Attempt` (per-session data)
- Recalculate `next_review_date` on edit when scheduling fields change
- Add filtering to `list` command (by pattern, difficulty, date range)
- CI pipeline with GitHub Actions

## Tech Stack

- **Python 3.11+**
- **Click** — CLI framework
- **Rich** — formatted terminal output
- **platformdirs** — cross-platform data directory handling
- **pytest** — testing framework
- **Black** and **Ruff** — code formatting and linting

## License

MIT