def getPuzzle(filename):
    crab_pos = []
    f = open(filename, 'r')
    for line in f:
        a = line.split(',')
    for b in a:
        crab_pos.append(int(b))
    return crab_pos


def part1(f):
    maximum = f[0]
    for i in f:
        if i > maximum:
            maximum = i
    fuel_cost = maximum * add_steps2(maximum)
    for goal in range(0, maximum + 1):
        step_cost = 0
        for pos in f:
            steps = abs(pos - goal)
            step_cost += steps
        if fuel_cost > step_cost > 0:
            fuel_cost = step_cost
    return fuel_cost


def part2(f):
    maximum = f[0]
    for i in f:
        if i > maximum:
            maximum = i
    fuel_cost = maximum * add_steps2(maximum)
    for goal in range(0, maximum + 1):
        step_cost = 0
        for pos in f:
            steps = abs(pos - goal)
            cost = add_steps2(steps)
            step_cost += cost
        if fuel_cost > step_cost > 0:
            fuel_cost = step_cost
    return fuel_cost


def add_steps(n):
    if n <= 1:
        return n
    else:
        return n + add_steps(n - 1)


def add_steps2(n):
    s = (n * (n+1))/2
    return s


puzzle = getPuzzle('7dec.txt')
print(part1(puzzle))
print(part2(puzzle))
