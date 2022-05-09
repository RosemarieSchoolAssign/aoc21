def get_input():
    input = []
    f = open('12dec.txt', "r")
    for line in f:
        line = line.strip("\n")
        input.append(line.split("-"))
    f.close()
    return input


def find_connections(connections, point):
    points = []
    for pair in connections:
        if point in pair:
            if pair.index(point) == 0:
                points.append(pair[1])
            else:
                points.append(pair[0])
    return points


def add_connections_to_path(path, points):
    temp = []
    for i in points:
        temp.append(path + [i])
    return temp


def update_visited(v, c):
    for i in c:
        if i.islower() and i not in v:
            v.append(i)
    return v


def wrong_duplicates(path, visited):
    temp = []
    for i in path:
        if i in visited:
            if i in temp:
                return True
            else:
                temp.append(i)
    return False


def wrong_duplicates_pt2(path, visited):
    temp = []
    allowed_duplicate = ''
    for i in path:
        if i in visited:
            if i in temp:
                if i != 'end' and i != 'start' and allowed_duplicate == '':
                    allowed_duplicate = i
                else:
                    return True
            else:
                temp.append(i)
    return False


def ride(paths, connections, visited, paths_with_end):
    count = 0
    for path in paths:
        count += 1
        if path[len(path) - 1] == 'end':
            # paths_with_end.append(path)
            paths_with_end.append(path)
            continue
        if wrong_duplicates_pt2(path, visited):
            path.clear()
        else:
            c = find_connections(connections, path[len(path) - 1])
            visited = update_visited(visited, c)  # for part 1
            temp = add_connections_to_path(path, c)
            ride(temp, connections, visited, paths_with_end)


root = 'start'
input = get_input()
p = [['start']]
a = []
ride(p, input, ['start'], a)
print(len(a))
