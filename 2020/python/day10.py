import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = sorted([int(f) for f in f.read().splitlines()])
        
def part1(input):
    results = {1: 0, 3: 1} # device is always 3 higher
    start = 0
    r = range(1, 4) # 1-3 inclusive
    for jolt in input:
        results[jolt - start] += 1 if jolt in r else 0
        r = range(jolt + 1, jolt + 4)
        start = jolt

    return results[1] * results[3]

def part2():
    ...



if __name__ == '__main__':
    print(part1(input))
    # print(part2())
    import timeit
    print(timeit.timeit("part1(input)", number=1000, globals=globals()))
    # print(timeit.timeit("part2()", number=1000, globals=globals()))
