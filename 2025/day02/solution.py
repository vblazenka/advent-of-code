"""Advent of Code 2025 - Day 2"""

# I'll optimize the solution :D
def part1(data: str) -> int | str | None:
    sum = 0
    for line in data.split(','):
        lb, rb = line.split("-")
        for i in range(int(lb), int(rb) + 1):
            if (len(str(i))%2 == 0):
                l, r = str(i)[:len(str(i))//2], str(i)[len(str(i))//2:]
                if (l==r):
                    sum += int(f"{l}{r}")
    return sum


def part2(data: str) -> int | str | None:
    """Solve part 2."""
    pass

if __name__ == "__main__":
    # Read input and solve
    with open("input.txt") as f:
        data = f.read().strip()

    print(f"Part 1: {part1(data)}")
    # print(f"Part 2: {part2(data)}")
