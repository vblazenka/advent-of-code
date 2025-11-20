
"""Advent of Code 2015 - Day 1"""

# ( -> up
# ) -> down
def part1(data: str) -> int:
  return data.count("(") - data.count(")")

def part2(data: str) -> int | None:
    floor = 0
    for position, char in enumerate(data, start=1):
        floor += 1 if char == "(" else -1

        if floor == -1:
            return position

if __name__ == "__main__":
    # Read input and solve
    with open("input.txt") as f:
        data = f.read().strip()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
