import pathlib
from functools import reduce

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = f.read().split("\n\n")
        

def part1():
    return sum([len(set(x.replace("\n", ""))) for x in input])


def part2():
    inputs = [i.split() for i in input]
    return sum(len(reduce(lambda x, y: x & y, [set(x) for x in i])) for i in inputs)
            


if __name__ == '__main__':
    print(part1())
    print(part2())
    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
