"""Tests for Advent of Code 2025 - Day 1"""

import pytest
from .solution import part1, part2


class TestPart1:
    """Tests for part 1."""

    def test_example_1(self):
        pass
        # assert part1("R49") == 1

class TestPart2:

    def counts_base_example(self):
        assert part2("""L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82""") == 6

    def counts_all_crossings_per_roration(self):
         assert part2("R1000") == 10
