def getPuzzle(filename):
    p = []
    f = open(filename, "r")
    for x in f:
        p.append(x.split(" "))
    f.close()
    return p


def part1(puzzle):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in puzzle:
        if i[0] == "forward":
            horizontal_pos += int(i[1])
            depth += (aim * int(i[1]))
        elif i[0] == "up":
            depth -= int(i[1])
        else:
            depth += int(i[1])
    return [horizontal_pos, depth]


def part2(puzzle):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in puzzle:
        if i[0] == "forward":
            horizontal_pos += int(i[1])
            depth += (aim * int(i[1]))
        elif i[0] == "up":
            aim -= int(i[1])
        else:
            aim += int(i[1])
    return [horizontal_pos, depth]


def multiply(horizontal_pos_and_depth):
    return horizontal_pos_and_depth[0] * horizontal_pos_and_depth[1]


puzzle = getPuzzle("2dec.txt")
print(multiply(part1(puzzle)))
print(multiply(part2(puzzle)))
