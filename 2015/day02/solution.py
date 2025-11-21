"""Advent of Code 2015 - Day 2"""

def parse_and_calculate(dimension: str) -> int:
    l, w, h = map(int, dimension.split('x'))
    areas = [l*w, w*h, h*l]
    return 2 * sum(areas) + min(areas)

def part1(data: str) -> int:
    # if we wrap list comprehension in [] we will create new array in memory
    # this approach is called "generator expression"
    return sum(parse_and_calculate(dim) for dim in data.splitlines())


def part2(data: str) -> int:
    def parse(dimension: str) -> int:
           l, w, h = map(int, dimension.split('x'))
           smallest = 2 * min([l+w, w+h, h+l])
           return sum([smallest, l*w*h])

    return (sum(parse(dim) for dim in data.splitlines()))

if __name__ == "__main__":
    # Read input and solve
    with open("input.txt") as f:
        data = f.read().strip()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
