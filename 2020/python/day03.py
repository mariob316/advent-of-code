import pathlib

with open(f"input/{pathlib.Path(__file__).stem}.txt", "r") as f:
    input = f.read().splitlines()


def part1():
    width = len(input[0])
    x = 0
    nbr_trees = 0

    for y in input:
        if y[x] == "#":
            nbr_trees += 1
        x = (x + 3) % width
    return nbr_trees


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    width = len(input[0])

    total = 1
    for slope in slopes:
        nbr_trees = 0
        y = 0
        x = 0
        while y < len(input):
            if input[y][x] == "#":
                nbr_trees += 1
            x = (x + slope[0]) % width
            y += slope[1]
        total *= nbr_trees
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())

    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
