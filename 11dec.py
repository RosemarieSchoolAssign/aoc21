def find_neighbours(os, flashing_opts_index):
    max_outer = len(os)
    max_inner = len(os[0])
    neighbours = []
    for e in flashing_opts_index:
        i = e[0]
        j = e[1]
        neighbours.append((i - 1, j - 1))
        neighbours.append((i - 1, j))
        neighbours.append((i - 1, j + 1))
        neighbours.append((i, j + 1))
        neighbours.append((i + 1, j + 1))
        neighbours.append((i + 1, j))
        neighbours.append((i + 1, j - 1))
        neighbours.append((i, j - 1))
    for e in reversed(neighbours):
        q = e[0]
        j = e[1]
        if q >= max_outer or q < 0:
            neighbours.remove(e)
        elif j >= max_inner or j < 0:
            neighbours.remove(e)
    return neighbours


def find_flashing_octps(os, counted_index):
    flashing_opts_index = []
    for i in range(len(os)):
        for j in range(len(os[i])):
            if os[i][j] > 9 and (i, j) not in counted_index:
                t = (i, j)
                flashing_opts_index.append(t)
    return flashing_opts_index


def increase_all(os):
    for i in range(len(os)):
        for j in range(len(os[i])):
            os[i][j] += 1


def increase_neighbours(os, neighbours):
    for e in neighbours:
        i = e[0]
        j = e[1]
        os[i][j] += 1


def set_to_zero(os, counted_index):
    for e in counted_index:
        i = e[0]
        j = e[1]
        os[i][j] = 0


def not_all_flashing(os):
    for i in range(len(os)):
        for j in range(len(os[i])):
            if os[i][j] != 0:
                return True
    return False


def move_forward(os):
    flashes = 0
    steps = 0
    while not_all_flashing(os):
        counted_index = []
        increase_all(os)  # increase all by one
        running_flashes = True
        while running_flashes:
            flashing_opts_index = find_flashing_octps(os,
                                                      counted_index)
            if len(flashing_opts_index) == 0:
                running_flashes = False
                set_to_zero(os, counted_index)
            else:
                flashes += len(
                    flashing_opts_index)
                neighbours = find_neighbours(os, flashing_opts_index)
                increase_neighbours(os, neighbours)
                counted_index = counted_index + flashing_opts_index
        steps += 1
    return steps


puzzle = []
f = open('11dec.txt', 'r')
for line in f:
    line = line.strip('\n')
    temp = []
    for i in line:
        temp.append(int(i))
    puzzle.append(temp)

print(move_forward(puzzle))
