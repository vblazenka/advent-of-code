"""Tests for Advent of Code 2015 - Day 2"""

import pytest
from .solution import part1, part2


class TestPart1:
    """Tests for part 1."""

    def test_one(self):
        assert part1("2x3x4") == 58

    def test_two(self):
        assert part1("1x1x10") == 43


class TestPart2:
    """Tests for part 2."""

    def test_one(self):
        assert part2("2x3x4") == 34

    def test_two(self):
        assert part2("1x1x10") == 14
