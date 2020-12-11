import pathlib
from itertools import *

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    lines = f.readlines()

report = set(map(int, lines))

def part1():
    for i in report:
        if (2020 - i) in report:
            return i * (2020 - i)


def part2():
    for i in report:
        j = i + 1
        for j in report:
            if (2020 - i - j) in report:
                return i * j * (2020 - i - j);

if __name__ == '__main__':
    print(part1())
    print(part2())

    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
