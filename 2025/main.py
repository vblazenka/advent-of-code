#!/usr/bin/env python3
"""Advent of Code 2025 - Main CLI"""

import argparse
import importlib
import sys
import time
from pathlib import Path


def run_day(day: int, test_only: bool = False) -> None:
    """Run solution for a specific day.

    Args:
        day: Day number (1-12)
        test_only: If True, only run tests without solving
    """
    if not 1 <= day <= 12:
        print(f"Error: Day must be between 1 and 12, got {day}")
        sys.exit(1)

    day_dir = Path(__file__).parent / f"day{day:02d}"
    solution_file = day_dir / "solution.py"

    if not solution_file.exists():
        print(f"Error: Solution file not found for day {day}")
        sys.exit(1)

    # Import the solution module
    module_name = f"day{day:02d}.solution"
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error importing day {day}: {e}")
        sys.exit(1)

    print(f"\n{'=' * 50}")
    print(f"  Advent of Code 2025 - Day {day}")
    print(f"{'=' * 50}\n")

    # Run tests
    if hasattr(module, "test"):
        print("Running tests...")
        try:
            module.test()
        except AssertionError as e:
            print(f"Test failed: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error running tests: {e}")
            sys.exit(1)

    if test_only:
        return

    # Read input
    input_file = day_dir / "input.txt"
    if not input_file.exists() or input_file.stat().st_size == 0:
        print("Warning: input.txt is empty or missing")
        return

    data = input_file.read_text().strip()

    # Run part 1
    if hasattr(module, "part1"):
        print("\nRunning Part 1...")
        start = time.perf_counter()
        try:
            result = module.part1(data)
            elapsed = time.perf_counter() - start
            print(f"Part 1: {result}")
            print(f"Time: {elapsed:.4f}s")
        except Exception as e:
            print(f"Error in Part 1: {e}")

    # Run part 2
    if hasattr(module, "part2"):
        print("\nRunning Part 2...")
        start = time.perf_counter()
        try:
            result = module.part2(data)
            elapsed = time.perf_counter() - start
            print(f"Part 2: {result}")
            print(f"Time: {elapsed:.4f}s")
        except Exception as e:
            print(f"Error in Part 2: {e}")

    print()


def run_all_days(test_only: bool = False) -> None:
    """Run solutions for all days.

    Args:
        test_only: If True, only run tests without solving
    """
    for day in range(1, 13):
        day_dir = Path(__file__).parent / f"day{day:02d}"
        input_file = day_dir / "input.txt"

        # Skip days without input
        if not input_file.exists() or input_file.stat().st_size == 0:
            continue

        try:
            run_day(day, test_only)
        except Exception as e:
            print(f"Error running day {day}: {e}")
            continue


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Advent of Code 2025 Solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py 1              # Run day 1
  python main.py 1 --test       # Run day 1 tests only
  python main.py --all          # Run all days with input
  python main.py --all --test   # Run all tests
        """
    )

    parser.add_argument(
        "day",
        type=int,
        nargs="?",
        help="Day number (1-12)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all days"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Only run tests, don't solve"
    )

    args = parser.parse_args()

    if args.all:
        run_all_days(args.test)
    elif args.day:
        run_day(args.day, args.test)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
