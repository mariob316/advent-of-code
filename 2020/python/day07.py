import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = [f[:-1].replace("bags", "bag") for f in f.read().splitlines()]
        


def part1():
    
    data = {}
    for rule in input:
        b = rule.split("contain")
        parent = b[0].split("bag")[0].strip()
        sub = b[1].split(",")
        data[parent] = set([s.split(num)[-1].replace("bag","").strip() for s in sub if (num := s.strip().split(" ")[0]) != "no"])

    def find_bag(bags, color, s):
        for parent_bag, sub_bags in bags.items():
            if color in sub_bags:
                s.add(parent_bag)
                find_bag(bags, parent_bag, s)
        return s
    
    hold = set()
    hold = find_bag(data, "shiny gold", hold)
    return len(hold)

def part2():
    bags = {c[0].strip(): c[1].strip().split(',') for i in input if (c := i.split('contain'))} 

    def find_bag(color):
        if 'no other bag' in bags[color]:
            return 1

        return 1 + sum(int(x[0]) * find_bag(' '.join(x[1:])) for col in bags[color] if (x:=col.split()))

    total = find_bag('shiny gold bag') - 1
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
