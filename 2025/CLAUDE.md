# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Advent of Code 2025 solutions in Python 3.13, managed with uv. The repository uses a dual testing system: pytest for proper unit tests and legacy inline tests via main.py CLI.

## Essential Commands

### Running Solutions
```bash
# Run a specific day's solution (runs inline tests + solves with input.txt)
python main.py 1

# Run all days that have input.txt
python main.py --all

# Run only inline tests for a day (no solving)
python main.py 1 --test

# Run solution directly (bypasses main.py)
cd day01 && python solution.py
```

### Testing
```bash
# Run pytest tests for all days
uv run pytest

# Run tests for a specific day
uv run pytest day01/test_solution.py

# Run tests with verbose output
uv run pytest -v

# Run a specific test class or method
uv run pytest day01/test_solution.py::TestPart1::test_balanced_nested
```

### Setup
```bash
# Install dependencies (pytest)
uv sync
```

## Architecture

### Dual Test System
This codebase has two testing approaches:

1. **Pytest tests** (`test_solution.py`): Modern unit tests with pytest classes and methods. Located in each day's folder alongside the solution.
2. **Legacy inline tests** (`test()` function in `solution.py`): Called by main.py before solving. Some older solutions may still use this pattern.

When adding tests, use pytest format in `test_solution.py`.

### Solution Structure
Each day follows this pattern:
```
dayXX/
├── solution.py      # Implements part1(data: str) and part2(data: str)
├── test_solution.py # Pytest tests organized in TestPart1 and TestPart2 classes
└── input.txt        # Puzzle input
```

Solutions must implement:
- `part1(data: str) -> int | str | None`: Part 1 solution
- `part2(data: str) -> int | str | None`: Part 2 solution
- Optional `test()` function for legacy inline tests (being phased out)

### Utilities Module
`utils/helpers.py` provides input reading utilities:
- `read_input(day: int, filename: str = "input.txt") -> str`
- `read_lines(day: int, filename: str = "input.txt") -> list[str]`
- `read_numbers(day: int, filename: str = "input.txt") -> list[int]`
- `manhattan_distance(x1, y1, x2, y2) -> int`

Import with: `from utils import read_input, read_lines`

### CLI (main.py)
The main.py CLI:
1. Imports `dayXX.solution` module dynamically
2. Runs `test()` function if present (legacy)
3. Reads `input.txt` from day folder
4. Executes `part1()` and `part2()` with timing
5. Skips days without input.txt when using `--all`

### Solution File Direct Execution
Each `solution.py` can run standalone via `if __name__ == "__main__"` block that reads `input.txt` directly. This bypasses main.py CLI.

## Key Patterns

- Solutions accept `data: str` (pre-stripped input) from main.py
- Test files use pytest class structure: `TestPart1`, `TestPart2`
- Input files are required for main.py to run solutions (checked via file size)
- Python 3.13+ syntax is used (e.g., `int | None` type hints)
- No external dependencies in solutions (puzzle logic only)
