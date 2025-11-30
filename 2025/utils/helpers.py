"""Helper functions for Advent of Code puzzles."""

from pathlib import Path


def read_input(day: int, filename: str = "input.txt") -> str:
    """Read input file for a specific day.

    Args:
        day: Day number (1-25)
        filename: Name of the input file (default: input.txt)

    Returns:
        Contents of the input file as a string
    """
    day_dir = Path(__file__).parent.parent / f"day{day:02d}"
    input_path = day_dir / filename
    return input_path.read_text().strip()


def read_lines(day: int, filename: str = "input.txt") -> list[str]:
    """Read input file as a list of lines.

    Args:
        day: Day number (1-25)
        filename: Name of the input file (default: input.txt)

    Returns:
        List of lines from the input file
    """
    return read_input(day, filename).splitlines()


def read_numbers(day: int, filename: str = "input.txt") -> list[int]:
    """Read input file as a list of integers (one per line).

    Args:
        day: Day number (1-25)
        filename: Name of the input file (default: input.txt)

    Returns:
        List of integers from the input file
    """
    return [int(line) for line in read_lines(day, filename)]


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    """Calculate Manhattan distance between two points.

    Args:
        x1, y1: Coordinates of first point
        x2, y2: Coordinates of second point

    Returns:
        Manhattan distance between the points
    """
    return abs(x1 - x2) + abs(y1 - y2)
