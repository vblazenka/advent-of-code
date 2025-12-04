"""Advent of Code 2025 - Day 2"""

# I'll optimize the solution :D
from math import floor


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
    sum = 0
    for line in data.split(','):
        lb, rb = line.split("-")
        for i in range(int(lb), int(rb) + 1):
            s = str(i)
            found = False
            for pattern_len in range(1, len(s)):
                if len(s) % pattern_len != 0:
                    continue
                pattern = s[:pattern_len]
                is_match = True
                for j in range(0, len(s), pattern_len):
                    chunk = s[j:j+pattern_len]
                    if chunk != pattern:
                        is_match = False
                        break
                if is_match:
                    found = True
                    break
            if found:
                sum += i
    return sum

    total = 0
    for line in data.split(','):
        lb, rb = line.split("-")
        for i in range(int(lb), int(rb) + 1):
            if is_invalid(i):
                total += i
    return total


    return sum

if __name__ == "__main__":
    # Read input and solve
    with open("input.txt") as f:
        data = f.read().strip()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
