
p = [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
     [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
     [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
     [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
     [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]


def getPuzzle(filename):
    puzzle = []
    f = open(filename, "r")
    for line in f:
        li = []
        for i in line:
            try:
                li.append(int(i))
            except:
                print("could not read from file")
        puzzle.append(li)
    return puzzle


def get_adjacent_pt1(outer_ind, inner_ind, heightmap):
    if outer_ind == 0:
        if inner_ind == 0:
            return [heightmap[outer_ind][inner_ind + 1],
                    heightmap[outer_ind + 1][inner_ind]]
        elif inner_ind == len(heightmap[outer_ind]) - 1:
            return [heightmap[outer_ind][inner_ind - 1],
                    heightmap[outer_ind + 1][inner_ind]]
        else:
            return [heightmap[outer_ind][inner_ind - 1],
                    heightmap[outer_ind][inner_ind + 1],
                    heightmap[outer_ind + 1][inner_ind]]

    elif outer_ind == len(heightmap) - 1:
        if inner_ind == 0:
            return [heightmap[outer_ind][inner_ind + 1],
                    heightmap[outer_ind - 1][inner_ind]]
        elif inner_ind == len(heightmap[outer_ind]) - 1:
            return [heightmap[outer_ind][inner_ind - 1],
                    heightmap[outer_ind - 1][inner_ind]]
        else:
            return [heightmap[outer_ind][inner_ind - 1],
                    heightmap[outer_ind][inner_ind + 1],
                    heightmap[outer_ind - 1][inner_ind]]

    elif inner_ind == 0:
        return [heightmap[outer_ind][inner_ind + 1],
                heightmap[outer_ind - 1][inner_ind],
                heightmap[outer_ind + 1][inner_ind]]

    elif inner_ind == len(heightmap[outer_ind]) - 1:
        return [heightmap[outer_ind][inner_ind - 1],
                heightmap[outer_ind - 1][inner_ind],
                heightmap[outer_ind + 1][inner_ind]]

    else:
        return [heightmap[outer_ind][inner_ind - 1],
                heightmap[outer_ind][inner_ind + 1],
                heightmap[outer_ind - 1][inner_ind],
                heightmap[outer_ind + 1][inner_ind]]


def current_height_lower_than_adjacent_pt1(current_height, adjacent):
    for i in adjacent:
        if current_height >= i:
            return False
    return True


def count_risk_level_pt1(heightmap):
    risk_level = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            #print('cord ', i, ' ', j)
            if current_height_lower_than_adjacent_pt1(heightmap[i][j], get_adjacent_pt1(i, j, heightmap)):
                risk_level += (1 + heightmap[i][j])
    return risk_level


def get_depths_in_row(row):
    b = []
    start = 0
    for i in range(len(row)):
        if row[i] == 9 and row[i-1] != 9 and i != 0:
            b.append([k for k in range(start, i)])
        elif i == len(row) - 1 and row[i] != 9:  # controlling for end of list
            b.append([k for k in range(start, i+1)])
        if row[i] == 9:  # increasing start to have right index value
            start = i + 1
    return b


def update_previous_row(depth, previous_row):
    connected = False
    for i in depth:
        for previous_depth in previous_row:
            if i in previous_depth and not connected:
                previous_depth += depth
                connected = True
    if not connected:
        previous_row.append(depth)
    return previous_row


def connect_rows(row, previous_row):
    for depth in row:
        previous_row = update_previous_row(depth, previous_row)
    return previous_row


def get_basins(heightmap):
    basins = []
    # [[0, 1], [5, 6, 7, 8, 9]]
    previous_row = []
    for i in range(len(heightmap)):
        # [[1, 2, 3, 4, 5], [7], [9]]
        row = get_depths_in_row(heightmap[i])
        if i == 0:
            basins.append(row)
            previous_row = row
        else:
            # [[0], [2, 3, 4], [6], [8, 9]]
            basins = connect_rows(row, previous_row)
            previous_row = row


def get_depths(heightmap):
    d = [get_depths_in_row(i) for i in heightmap]
    for j in d:
        print(j)
    return d


def connect(depth, b, row):
    for i in row:
        for j in i:
            if j in depth:
                b.append(i)
    return b


def part_2(heightmap):
    basins = []
    d = get_depths(heightmap)
    for i in range(len(d)):
        for depth in d[i]:
            b = []
            not_done = True
            while not_done:
                b = connect(depth, b, d[i+1])



#get_depths(p)
puzzle = getPuzzle('9dec.txt')
print(count_risk_level_pt1(puzzle))
#print(count_risk_level(puzzle))
