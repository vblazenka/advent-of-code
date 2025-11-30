# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) using Python 3.13.

## Project Structure

```
2025/
   main.py              # CLI to run solutions
   utils/               # Shared utilities
      __init__.py
      helpers.py      # Common helper functions
   day01/              # Day 1 solution
      __init__.py
      solution.py     # Solution code + tests
      input.txt       # Puzzle input
   day02/              # Day 2 solution
      ...
   ...                 # Days 3-12
```

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for Python package management.

```bash
# Install dependencies (includes pytest)
uv sync
```

## Usage

### Run a specific day

```bash
python main.py 1        # Run day 1
python main.py 5        # Run day 5
```

### Run tests only

```bash
python main.py 1 --test    # Run day 1 tests
```

### Run all days

```bash
python main.py --all       # Run all days with input files
python main.py --all --test # Run all tests
```

### Run directly

You can also run individual day solutions directly:

```bash
cd day01
python solution.py
```

### Run tests with pytest

This project uses pytest for testing. Each day has a `test_solution.py` file with test cases.

```bash
# Run all tests for all days
uv run pytest

# Run tests for a specific day
uv run pytest day01/test_solution.py
uv run pytest day05/test_solution.py

# Run tests with verbose output
uv run pytest -v

# Run a specific test class
uv run pytest day01/test_solution.py::TestPart1

# Run a specific test method
uv run pytest day01/test_solution.py::TestPart1::test_balanced_nested

# Run tests and show print statements
uv run pytest -s

# Run tests with coverage (if pytest-cov is installed)
uv run pytest --cov
```

## Solving a Day

1. Create/edit the solution in `dayXX/solution.py`
2. Add your puzzle input to `dayXX/input.txt`
3. Add test cases from the problem to `dayXX/test_solution.py` using pytest
4. Implement `part1()` and `part2()` functions
5. Run tests with `uv run pytest dayXX/test_solution.py`
6. Run with `python main.py XX`

## Utilities

The `utils` module provides common helper functions:

- `read_input(day, filename)` - Read input file for a day
- `read_lines(day, filename)` - Read input as list of lines
- `read_numbers(day, filename)` - Read input as list of integers
- `manhattan_distance(x1, y1, x2, y2)` - Calculate Manhattan distance

Import them in your solutions:

```python
from utils import read_input, read_lines
```

## Progress

| Day | Part 1 | Part 2 | Stars |
|-----|--------|--------|-------|
| 1   | -      | -      | PP   |
| 2   | -      | -      | PP   |
| ... | ...    | ...    | ...   |

## Notes

- Python 3.13+ required
- Each day's solution includes inline tests from the problem statement
- Tests run automatically before solving
