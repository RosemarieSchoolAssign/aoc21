def getPuzzle(filename):
    p = []
    f = open(filename, "r")
    for line in f:
        p.append(line)
    f.close()
    return p


def get_most_common_value(b_n, i):
    freq = 0
    amount_binary_numbers = len(b_n)
    for binary_number in b_n:
        freq += int(binary_number[i])
    if freq >= amount_binary_numbers / 2:
        return 1
    else:
        return 0


def get_binary_selection(b_n, i, binary):
    new_b_n = []
    for binary_number in b_n:
        if binary_number[i] == str(binary):
            new_b_n.append(binary_number)
    return new_b_n


def get_o_gen_rating(b_n):  # add another while loop at start if needed
    for i in range(len(b_n[0]) - 1):
        most_common_value = get_most_common_value(b_n, i)
        b_n = get_binary_selection(b_n, i, most_common_value)
        if len(b_n) < 2:
            return b_n


def get_co2_scrubber_rating(b_n):
    for i in range(len(b_n[0]) - 1):
        most_common_value = get_most_common_value(b_n, i)
        if most_common_value == 1:
            b_n = get_binary_selection(b_n, i, 0)
        else:
            b_n = get_binary_selection(b_n, i, 1)
        if len(b_n) < 2:
            return b_n


def get_binary(b_n, i):
    freq = 0
    amount_binary_numbers = len(b_n)  # 3
    for binary_number in b_n:  # a list
        freq += int(binary_number[i])  #
    if freq > amount_binary_numbers / 2:
        return [1, 0]
    else:
        return [0, 1]


def get_gamma_epsilon(b_n):
    gamma = ""
    epsilon = ""
    for i in range(len(b_n[0]) - 1):
        a = get_binary(b_n, i)
        gamma += str(a[0])
        epsilon += str(a[1])
    return [gamma, epsilon]

#binary_numbers = [['00100\n'], ['11110\n'], ['10110\n']]
puzzle = getPuzzle("3dec.txt")
o = get_o_gen_rating(puzzle)
c = get_co2_scrubber_rating(puzzle)
o_gen_rating = int(o[0], 2)
co2_scrubber_rating = int(c[0], 2)
print(o_gen_rating * co2_scrubber_rating)


#b = get_gamma_epsilon(puzzle)
# print(int(b[0], 2) * int(b[1], 2))
