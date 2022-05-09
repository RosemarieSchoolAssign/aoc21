from operator import itemgetter

p = [[6, 10], [0, 14], [9, 10], [0, 3], [10, 4], [4, 11], [6, 0], [6, 12], [4, 1],
     [0, 13], [10, 12], [3, 4], [3, 0], [8, 4], [1, 10], [2, 14], [8, 10], [9, 0]]


def get_input():
    ipt = []
    instr = []
    f = open('13dec.txt', "r")
    for line in f:
        line = line.strip("\n")
        if 'fold' in line:
            temp = line.split(" ")
            instr.append(temp[len(temp) - 1].split("="))
        elif line != "":
            ipt.append(line.split(","))
            ipt[len(ipt) - 1] = [int(i) for i in ipt[len(ipt) - 1]]
    f.close()
    return ipt, instr


def display(points):
    print('*************')
    for i in points:
        print(i)


def get_points_for_display(points, m_x, m_y):
    temp = []
    for y in range(0, m_y):
        s = ""
        for x in range(0, m_x):
            if [x, y] in points:
                s += '#'
            else:
                s += '.'
        temp.append(s)
    return temp


def find_max(index, ipt):
    temp = []
    for i in ipt:
        temp.append(i[index])
    return max(temp)


def get_new_index(n, fold):
    return fold - (n - fold)


def remove(ipt, to_remove):
    to_remove = sorted(to_remove, reverse=True)
    for i in to_remove:
        ipt.pop(i)
    return ipt


def remove_duplicates(ipt):
    temp = []
    for i in ipt:
        if i not in temp:
            temp.append(i)
    return temp


def get_new_pos(coordinate, fold, ipt):
    to_be_removed = []
    for i in ipt:
        if i[coordinate] > fold:
            if coordinate == 0:
                ipt.append([get_new_index(i[coordinate], fold), i[1]])
            else:
                ipt.append([i[0], get_new_index(i[coordinate], fold)])
            to_be_removed.append(ipt.index(i))
    # r = remove(ipt, to_be_removed)
    return remove_duplicates(remove(ipt, to_be_removed))


def read_instructions(ins, ipt, max_x, max_y):
    for i in ins:
        if i[0] == 'y':
            ipt = get_new_pos(1, int(i[1]), ipt)
            max_y = max_y // 2
        else:
            ipt = get_new_pos(0, int(i[1]), ipt)
            max_x = max_x // 2
    display(get_points_for_display(ipt, max_x, max_y))


input1, instructions = get_input()
p = sorted(p, key=itemgetter(1, 0))
maximum_x = find_max(0, input1) + 1
maximum_y = find_max(1, input1) + 1
read_instructions(instructions, input1, maximum_x, maximum_y)
#display(get_points_for_display(p, maximum_x, maximum_y))

first_fold = get_new_pos(1, 7, p)
#first_fold = sorted(first_fold, key=itemgetter(1, 0))
# print(first_fold)
#display(get_points_for_display(first_fold, maximum_x, maximum_y//2))
# print(len(first_fold))
