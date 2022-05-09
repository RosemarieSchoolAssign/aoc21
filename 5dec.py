
def vertical_line():
    return x1 == x2


def horizontal_line():
    return y1 == y2


def get_vertical_coordinates():
    c = []
    if y1 > y2:
        for i in range(y2, y1 + 1):
            c.append(str(x1) + ',' + str(i))
    else:
        for i in range(y1, y2 + 1):
            c.append(str(x1) + ',' + str(i))
    return c


def get_horizontal_coordinates():
    c = []
    if x1 > x2:
        for i in range(x2, x1+1):
            c.append(str(i) + ',' + str(y1))
    else:
        for i in range(x1, x2+1):
            c.append(str(i) + ',' + str(y1))
    return c


def line_going_right_upward():
    return x1 + (y1 - y2) == x2


def line_going_right_downward():
    return x1 - (y1 - y2) == x2


def get_right_upward_coordinates():
    c = []
    if x1 > x2:
        for i in range(x2, x1 + 1):
            c.append(str(i) + ',' + str(y2 - (i - x2)))
    else:
        for i in range(x1, x2 + 1):
            c.append(str(i) + ',' + str(y1 - (i - x1)))
    return c


def get_right_downward_coordinates():
    c = []
    if x1 > x2:
        for i in range(x2, x1 + 1):
            c.append(str(i) + ',' + str(y2 + (i - x2)))
    else:
        for i in range(x1, x2 + 1):
            c.append(str(i) + ',' + str(y1 + (i - x1)))
    return c


def update_visited(v, coordinates):
    for i in coordinates:
        if i not in v.keys():
            v.update({i: 1})
        else:
            v.update({i: v.get(i) + 1})
    return v


def get_crossings():
    c = 0
    for i in visited:
        if visited.get(i) > 1:
            c += 1
    return c


visited = {}
f = open('5dec.txt')
for line in f:
    a_to_b = line.split(' -> ')
    a = a_to_b[0].split(',')
    b = a_to_b[1].strip('\n').split(',')
    x1, y1 = int(a[0]), int(a[1])
    x2, y2 = int(b[0]), int(b[1])

    # part 1
    if vertical_line():
        visited = update_visited(visited, get_vertical_coordinates())
    elif horizontal_line():
        visited = update_visited(visited, get_horizontal_coordinates())

    # part 2
    elif line_going_right_upward():
        visited = update_visited(visited, get_right_upward_coordinates())
    elif line_going_right_downward():
        visited = update_visited(visited, get_right_downward_coordinates())

print(get_crossings())




