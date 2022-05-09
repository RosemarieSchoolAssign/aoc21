from queue import PriorityQueue

"""
start, end, graph, visited, weights, nodes, priority queue for alternatives
"""


def get_input():
    ipt = []
    f = open('15dec.txt', "r")
    for line in f:
        line = line.strip("\n")
        temp = []
        for n in line:
            temp.append(int(n))
        ipt.append(temp)
    return ipt


# path = [[4], [[0,0], [0,1]]]
# neighbours = [[0,0], [0,1]]
def add_to_queue(graph, queue, neighbours, path):
    # [[0], [[0, 0]]]
    for i in neighbours:
        cost = path[0][0]
        temp = []
        x = i[1]
        y = i[0]
        cost += graph[y][x]
        temp.append([cost])
        up = path[1] + [i]
        temp.append(up)
        queue.put(temp)
    return queue


# priority, data structure to hold coord and current path
def get_paths(graph, s):
    paths = []
    q = PriorityQueue()
    n = get_neighbours(graph, s)
    add_to_queue(graph, q, n, s)
    while not q.empty():
        path = q.get()  # important that path is removed from queue once collected here
        if path[1][len(path[1]) - 1] == [len(graph) - 1, len(graph[len(graph) - 1]) - 1]:
            paths.append(path)
        else:
            n = get_neighbours(graph, path)
            add_to_queue(graph, q, n, path)
    return paths


def pt_1_dijkstra(graph, start_vertex):
    lowest_cost_on_nodes = get_cost_for_all_nodes(graph, 2)
    lowest_cost_on_nodes[start_vertex] = 0  # '0000'
    visited = []
    pq = PriorityQueue()
    pq.put((0, start_vertex))  # '0000'
    while not pq.empty():
        (dist, current_vertex) = pq.get()  # '0000'
        visited.append(current_vertex)  # '0000'
        neighbours = get_neighbours(graph, current_vertex, 2)  # '0000'
        for neighbour in neighbours:  # '0000'
            distance = graph[int(neighbour[0:2])][int(neighbour[2:])]  # cost of that place
            if neighbour not in visited:  # '00'
                old_cost = lowest_cost_on_nodes[neighbour]  # cost of that place according to dictionary
                new_cost = lowest_cost_on_nodes[current_vertex] + distance  # '00' + graph[neighbour[0]][neighbour[0]]
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    lowest_cost_on_nodes[neighbour] = new_cost
    return lowest_cost_on_nodes


def get_graph_length(graph):
    count = 0
    for i in graph:
        for j in i:
            count += 1
    return count


def get_cost_for_all_nodes(graph, z):
    cost_for_all_nodes = {}
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            cost_for_all_nodes.update({str(i).zfill(z) + str(j).zfill(z): float('inf')})
    return cost_for_all_nodes


# '000000'
def get_neighbours(graph, current_node, z):
    current_node = [int(current_node[:z]), int(current_node[z:])]
    neighbours = []
    temp = [[current_node[0] - 1, current_node[1]], [current_node[0] + 1, current_node[1]],
            [current_node[0], current_node[1] - 1],
            [current_node[0], current_node[1] + 1]]
    for node in temp:
        correct_node = True
        for i in node:
            if i < 0:
                correct_node = False
            elif i > len(graph) - 1:
                correct_node = False
            elif i > len(graph[0]) - 1:
                correct_node = False
        if correct_node:
            neighbours.append(str(node[0]).zfill(z) + str(node[1]).zfill(z))
    return neighbours


def pt_2_dijkstra(graph, start_vertex):  # 250 000
    lowest_cost_on_nodes = get_cost_for_all_nodes(graph, 3)
    lowest_cost_on_nodes[start_vertex] = 0  # '000000'
    visited = []
    pq = PriorityQueue()
    pq.put((0, start_vertex))  # '000000'
    while not pq.empty():
        (dist, current_vertex) = pq.get()  # '000000'
        visited.append(current_vertex)  # '000000'
        neighbours = get_neighbours(graph, current_vertex, 3)  # '000000'
        for neighbour in neighbours:  # '000000'
            distance = graph[int(neighbour[0:3])][int(neighbour[3:])]  # cost of that place
            if neighbour not in visited:  # '00'
                old_cost = lowest_cost_on_nodes[neighbour]  # cost of that place according to dictionary
                new_cost = lowest_cost_on_nodes[current_vertex] + distance  # '00' + graph[neighbour[0]][neighbour[0]]
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    lowest_cost_on_nodes[neighbour] = new_cost
    return lowest_cost_on_nodes


def increase_graph_left(graph):
    mega = [[0 for _ in range(len(graph) * 5)] for _ in range(len(graph) * 5)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            mega[i][j] = graph[i][j]
            mega[i][j + len(graph)] = mega[i][j] + 1 if graph[i][j] + 1 < 10 else 1
            mega[i][j + (len(graph) * 2)] = mega[i][j + len(graph)] + 1 if mega[i][j + len(graph)] + 1 < 10 else 1
            mega[i][j + (len(graph) * 3)] = mega[i][j + (len(graph) * 2)] + 1 if mega[i][j + (len(graph) * 2)] + 1 < 10 else 1
            mega[i][j + (len(graph) * 4)] = mega[i][j + (len(graph) * 3)] + 1 if mega[i][j + (len(graph) * 3)] + 1 < 10 else 1
    return mega


"""
inc_graph[i + 3][j] = inc_graph[i][j] + 1 if inc_graph[i][j] + 1 < 10 else 1
inc_graph[i + 6][j] = inc_graph[i + 3][j] + 1 if inc_graph[i + 3][j] + 1 < 10 else 1
"""
def increase_graph_down(graph):
    inc_graph = increase_graph_left(graph)
    for i in range(len(graph)):
        for j in range(len(inc_graph)):
            inc_graph[i][j] = inc_graph[i][j]
            inc_graph[i + len(graph)][j] = inc_graph[i][j] + 1 if inc_graph[i][j] + 1 < 10 else 1
            inc_graph[i + (len(graph) * 2)][j] = inc_graph[i + len(graph)][j] + 1 if inc_graph[i + len(graph)][j] + 1 < 10 else 1
            inc_graph[i + (len(graph) * 3)][j] = inc_graph[i + (len(graph) * 2)][j] + 1 if inc_graph[i + (len(graph) * 2)][j] + 1 < 10 else 1
            inc_graph[i + (len(graph) * 4)][j] = inc_graph[i + (len(graph) * 3)][j] + 1 if inc_graph[i + (len(graph) * 3)][j] + 1 < 10 else 1
    return inc_graph


start_v_pt_1 = '0000'
start_v_pt_2 = '000000'
g_ipt = get_input()
g_ipt = increase_graph_down(g_ipt)  # 250 000
print(pt_2_dijkstra(g_ipt, start_v_pt_2))
#result = pt_1_dijkstra(g_ipt, start_v_pt_1)
#print(result['9999'])



