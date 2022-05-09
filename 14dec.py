import sys

from pip._vendor.urllib3.connectionpool import xrange

"""
NNCB

# NNCB
# NCNB CHB
# NBCC NBBB CBHC B

"""
i_p = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NN': 'C', 'NC': 'B', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C',
       'BH': 'H', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}


def get_input():
    s = ''
    ipt = {}
    f = open('14dec.txt', "r")
    for line in f:
        line = line.strip("\n")
        if ' -> ' in line:
            temp = line.split(' -> ')
            ipt.update({temp[0]: temp[1]})
        elif line.isupper():
            s = line
    f.close()
    return [s, ipt]


def find_letter_pairs(polymer_template):
    pairs = []
    for i in range(len(polymer_template) - 1):
        pairs.append(polymer_template[i] + polymer_template[i + 1])
    return pairs


# is: NCNNBCCHB
# should: NCN BCHB

# is: NBCC NBBB CBHC B
# should: NBCC NBBB CBHC B

# is: NBBB CNCC NBBN BNBB CHBH HBCH B
# should: NBBB CNCC NBBN BNBB CHBH HBCH B

# is: NBBN BNBB CCNB CNCC NBBN BBNB BBNB BNBB CBHC BHHN HCBB CBHC B
# should: NBBN BNBB CCNB CNCC NBBN BBNB BBNB BNBB CBHC BHHN HCBB CBHC B

def connect_pairs(pairs, insertion_pairs):
    modified_pairs = []
    for pair in pairs:
        if pair in insertion_pairs.keys():
            modified_pairs.append(pair[0] + insertion_pairs.get(pair) + pair[1])
    return modified_pairs


def put_pairs_together(pairs):
    string_of_pairs = ''
    for pair in pairs:
        if pairs.index(pair) == len(pairs) - 1:
            string_of_pairs += pair
        else:
            string_of_pairs += pair[0] + pair[1]
    return string_of_pairs


def get_letter_freq(polymer_template):
    temp = {}
    for i in polymer_template:
        if i in temp.keys():
            temp.update({i: temp.get(i) + 1})
        else:
            temp.update({i: 1})
    return temp


def find_letter_pairs2(polymer_template, insertion_pairs):
    s = ''
    for i in range(len(polymer_template) - 1):
        if i == len(polymer_template) - 2:
            s += polymer_template[i] + insertion_pairs.get(polymer_template[i] + polymer_template[i + 1]) + \
                 polymer_template[i + 1]
        else:
            s += polymer_template[i] + insertion_pairs.get(polymer_template[i] + polymer_template[i + 1])
    yield s


def calculate_pt_1(polymer_template, insertion_pairs):
    count = 0
    while count < 40:
        polymer_template = find_letter_pairs2(polymer_template, insertion_pairs)
        # p = connect_pairs(p, insertion_pairs)
        # polymer_template = put_pairs_together(p)
        count += 1
    freq = get_letter_freq(polymer_template).values()
    return max(freq) - min(freq)


def find_largest_index(polymer_template):
    largest = 0
    for k, v in polymer_template.items():
        m = max(v)
        if m > largest:
            largest = m
    return largest


def find_last_letter(polymer_template, largest):
    for k, v in polymer_template.items():
        if largest in v:
            return k


def get_result(polymer_template):
    min_letters = find_largest_index(polymer_template)
    max_letters = 0
    k_min = ''
    k_max = ''
    for k, v in polymer_template.items():
        temp = len(v)
        if temp < min_letters:
            min_letters = temp
            k_min = k
        if temp > max_letters:
            max_letters = temp
            k_max = k
    return max_letters - min_letters


def loop(polymer_template, insertion_pairs):
    count = 0
    while count < 40:
        largest = find_largest_index(polymer_template)
        last_letter = find_last_letter(polymer_template, largest)
        polymer_template = calculate_pt_2(polymer_template, insertion_pairs, largest, last_letter)
        count += 1
    return get_result(polymer_template)


def test_loop(polymer_template, insertion_pairs):
    n = 0
    c = 0
    b = 0
    h = 0
    for i in range(len(polymer_template)):
        test(polymer_template[i], polymer_template[i+1], insertion_pairs)


def test(first, second, insertion_pairs):
    n = 0
    c = 0
    b = 0
    h = 0




# NNCB
# NCNB CHB
# NBCC NBBB CBHC B
def calculate_pt_2(polymer_template, insertion_pairs, largest, last_letter):
    s = {}
    new_index = 0
    for number in range(largest):
        first = ''
        second = ''
        for letter, indexes in polymer_template.items():
            if number in indexes:
                temp = s.get(letter)
                if temp is None:
                    s.update({letter: [new_index]})
                else:
                    temp.append(new_index)
                    s.update({letter: temp})
                first = letter
                new_index += 1
            if (number + 1) in indexes:
                second = letter
        temp = s.get(insertion_pairs.get(first + second))
        if temp is None:
            s.update({insertion_pairs.get(first + second): [new_index]})
        else:
            temp.append(new_index)
            s.update({insertion_pairs.get(first + second): temp})
        new_index += 1

    temp = s.get(last_letter)
    if temp is None:
        s.update({last_letter: [new_index]})
    else:
        temp.append(new_index)
        s.update({last_letter: temp})
    return s


input = get_input()
# print(input[0])
# print(input[1])

print(calculate_pt_1(input[0], input[1]))
p_t = {'N': [0, 1], 'C': [2], 'B': [3]}
p_t_input = {}
for i in range(len(input[0])):
    if input[0][i] in p_t_input.keys():
        t = p_t_input.get(input[0][i])
        t.append(i)
        p_t_input.update({input[0][i]: t})
    else:
        p_t_input.update({input[0][i]: [i]})
#print(p_t_input)
#print(loop(p_t_input, input[1]))




