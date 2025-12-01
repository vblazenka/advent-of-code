"""Advent of Code 2025 - Day 1"""

def parse_rotation(line: str) -> int:
    return int(line.lstrip("L").lstrip("R"))

def part1(data: str) -> int | None:
    dial = 50
    count = 0

    for cmd in data.splitlines():
        cmd_val = parse_rotation(cmd)
        match(cmd[0]):
            case "L":
                dial = (dial - cmd_val) % 100
                count += 1 if dial == 0 else 0
            case "R":
                dial = (dial + cmd_val) % 100
                count += 1 if dial == 0 else 0
            case _:
                return 0

    return count


def part2(data: str) -> int | str | None:
    dial = 50
    count = 0

    for cmd in data.splitlines():
        cmd_val = parse_rotation(cmd)
        match(cmd[0]):
            case "L":
                if dial == 0:
                    count += cmd_val // 100
                elif cmd_val >= dial:
                    count += (cmd_val - dial) // 100 + 1
                dial = (dial - cmd_val) % 100
            case "R":
                count += (dial + cmd_val) // 100
                dial = (dial + cmd_val) % 100
            case _:
                return 0

    return count


if __name__ == "__main__":
    pass
    # Read input and solve
    with open("input.txt") as f:
        data = f.read().strip()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
