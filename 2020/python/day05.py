import pathlib

p = pathlib.Path(__file__).parent.parent.joinpath("input")
with open(f'{p / pathlib.Path(__file__).stem}.txt', "r") as f:
    input = f.read().splitlines()
        

def part1():
    ids = []
    for boarding_pass in input:
        rows = list(range(128))
        columns = list(range(8))
        halfcolumns = int((len(columns)/2))
        halfrow = int((len(rows)/2))
        
        for l in boarding_pass:
            if l == "F":    
                rows = rows[0:halfrow]
                halfrow = int((len(rows)/2))
            elif l == "B": 
                rows = rows[halfrow:]
                halfrow = int((len(rows)/2))
            elif l == "L": 
                columns = columns[0:halfcolumns]
                halfcolumns = int((len(columns)/2))
            elif l == "R": 
                columns = columns[halfcolumns:]
                halfcolumns = int((len(columns)/2))
        ids.append(rows[0] * 8 + columns[0])
    return max(ids)

def part1a():
    return max(int(b.translate(str.maketrans("FBLR", "0101")), 2) for b in input)


def part2():
    ids = sorted(int(b.translate(str.maketrans("FBLR", "0101")), 2) for b in input)
    my_id = set(range(min(ids), max(ids))) - set(ids)
    return my_id


if __name__ == '__main__':
    print(part1a())
    print(part2())
    import timeit
    print(timeit.timeit("part1()", number=1000, globals=globals()))
    print(timeit.timeit("part2()", number=1000, globals=globals()))
