import pathlib
import re

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    passwords = f.read().splitlines()


def part1():
    nbr_valid = 0
    for password in passwords:
        split = re.split("\\W+", password)

        min = int(split[0])
        max = int(split[1])
        letter = split[2]
        password = split[3]

        count = list(password).count(letter)
        nbr_valid += 1 if min <= count <= max else 0

    return nbr_valid


def part1a():
    return sum(
        [
            int(split[0]) <= list(split[3]).count(split[2]) <= int(split[1])
            for password in passwords if (split := re.split("\\W+", password))
        ]
    )


def part2():
    valid = 0
    for password in passwords:
        rest, word = password.split(":")
        bounds, letter = rest.split(" ")
        low, high = bounds.split("-")
        if int(low) <= len(word.split(letter)) - 1 <= int(high):
            valid += 1
    return valid


def part2a():
    return sum(
        [
            ((split[3][int(split[0])-1] == split[2]) ^ (split[3][int(split[1])-1] == split[2]))
            for password in passwords if (split := re.split("\\W+", password))
        ]
    )


if __name__ == '__main__':
    print(part1())
    print(part1a())
    print(part2())
    print(part2a())

    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part1a()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
    print(timeit.timeit("part2a()", number=1000, globals=globals()))