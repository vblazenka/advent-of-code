"""Tests for Advent of Code 2015 - Day 1"""

import pytest
from .solution import part1, part2


class TestPart1:
    """Tests for part 1: finding the final floor."""

    def test_balanced_nested(self):
        """(()) results in floor 0."""
        assert part1("(())") == 0

    def test_balanced_sequential(self):
        """()() results in floor 0."""
        assert part1("()()") == 0

    def test_three_floors_up_repeated(self):
        """((( results in floor 3."""
        assert part1("(((") == 3

    def test_three_floors_up_mixed(self):
        """(()(()( results in floor 3."""
        assert part1("(()(()(") == 3

    def test_three_floors_up_with_downs(self):
        """))(((( results in floor 2."""
        assert part1("))((((") == 2

    def test_basement_single(self):
        """) results in floor -1."""
        assert part1(")") == -1

    def test_basement_multiple(self):
        """()()) results in floor -1."""
        assert part1("()())") == -1

    def test_three_floors_down(self):
        """))) results in floor -3."""
        assert part1(")))") == -3

    def test_three_floors_down_mixed(self):
        """)())()) results in floor -3."""
        assert part1(")())())") == -3


class TestPart2:
    """Tests for part 2: finding when Santa first enters the basement."""

    def test_enters_basement_immediately(self):
        """) causes Santa to enter the basement at position 1."""
        assert part2(")") == 1

    def test_enters_basement_at_position_5(self):
        """()()) causes Santa to enter the basement at position 5."""
        assert part2("()())") == 5
