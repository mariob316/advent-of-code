import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = [int(f) for f in f.read().splitlines()]
        
perm = 5

def part1():
    window = input[:perm]
    for i in input[perm:]:
        for num in window:
            if (i - num) in window:
                window.pop(0)
                window.append(i)
                break
        else:
            return i


def part2(invalid):
    start = 0
    end = 0
    current = input[start]
    while start < len(input):
        if current == invalid:
            result = input[start:end]
            return min(result) + max(result)
        elif current < invalid:
            end += 1
            current += input[end]
        else:
            current -= input[start]
            start += 1



if __name__ == '__main__':
    p1 = part1()
    print(p1)
    p2 = part2(p1)
    print(p2)
    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2(invalid)", number=1000, setup="invalid = part1()", globals=globals()))
