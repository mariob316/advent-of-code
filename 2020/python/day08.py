from collections import defaultdict
import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = f.read().splitlines()
        


def part1():
    accum = 0
    i = 0
    seen = set()
    while i not in seen:
        seen.add(i)
        l = input[i]
        code = l[:3]
        num = int(l[3:])
        if code == "acc":
            accum += num
            i += 1
        elif code == "jmp":
            i += num
        else:
            i += 1
    else:
        return accum

    

def part2():
    accum = 0
    i = 0
    seen = set()
    code_map = defaultdict(list)
    while i < len(input):
        if i in seen:
            break
        seen.add(i)
        l = input[i]
        code = l[:3]
        num = int(l[3:])
        code_map[code].append(i)
        if code == "acc":
            accum += num
            i += 1
        elif code == "jmp":
            i += num
        else:
            i += 1

    def swap():
        cp = input.copy()
        for code, idx_list in code_map.items():
            if code == "nop" and idx_list:
                i = idx_list.pop()
                num = cp[i].split()[1].strip()
                cp[i] = f"jmp {num}"
            elif code == "jmp" and idx_list:
                i = idx_list.pop()
                num = cp[i].split()[1].strip()
                cp[i] = f"nop {num}"
        return cp

    def loop(input):
        accum = 0
        i = 0
        seen = set()
        while i < len(input):
            if i in seen:
                accum = loop(swap())
                break
            seen.add(i)
            l = input[i]
            code = l[:3]
            num = int(l[3:])
            if code == "acc":
                accum += num
                i += 1
            elif code == "jmp":
                i += num
            else:
                i += 1
        return accum
    
    del code_map['acc']
    a = loop(input)
    return a


if __name__ == '__main__':
    print(part1())
    print(part2())
    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
