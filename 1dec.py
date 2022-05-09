
def getPuzzleAsList(filename):
    p = []
    f = open(filename, "r")
    for x in f:
        p.append(int(x))
    f.close()
    return p


def part1():
    nr_of_larger = 0
    for i in range(1, len(puzzle)):
        if puzzle[i] > puzzle[i - 1]:
            nr_of_larger += 1
    return nr_of_larger


def part2():
    nr_of_larger = 0
    remainder = len(puzzle) % 3
    for i in range(1, len(puzzle)-remainder):
        s = puzzle[i] + puzzle[i + 1] + puzzle[i + 2]
        sum_before = puzzle[i - 1] + puzzle[i] + puzzle[i + 1]
        if s > sum_before:
            nr_of_larger += 1
    return nr_of_larger


puzzle = getPuzzleAsList("1dec.txt")
print(part1())
print(part2())