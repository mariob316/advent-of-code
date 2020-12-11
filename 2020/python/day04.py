import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = f.read().split("\n\n")
        

def part1():
    filter = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return sum(all([key in passport for key in filter]) for passport in input)


def part2():
    filter = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    hgt_map = {"cm": (150, 193), "in": (59, 76)}
    validator = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: hgt_map[x[-2:]][0] <= int(x[:-2]) <= hgt_map[x[-2:]][1] if x[-2:] in {"cm", "in"} else False,
        'hcl': lambda x: all([i.lower() in '0123456789abcdef' for i in x[1:]]) if x[0] == '#' else False,
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: x.isnumeric() and len(x) == 9,
    }
    passports = [dict(line.split(':') for line in pas.split()) for pas in input]
    passports = [p for p in passports if all(k in p.keys() for k in filter)]
    valid = sum(all(validator[k](v) if k != "cid" else True for k, v in passport.items()) for passport in passports)
    return valid


if __name__ == '__main__':
    print(part1())
    print(part2())
    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
