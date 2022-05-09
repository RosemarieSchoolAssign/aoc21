import re
from collections import Counter


def getPuzzle(filename):
    signal_patterns = []
    output = []
    f = open(filename, 'r')
    for line in f:
        a = line.split('|')
        signal_patterns.append(re.split("\s", a[0]))
        output.append(re.split('\s', a[1]))
    for i in range(len(output)-1):
        output[i].pop(len(output[i]) - 1)
        output[i].pop(0)
    output[len(output) - 1].pop(0)
    for signal in signal_patterns:
        signal.pop(len(signal) - 1)
    return [signal_patterns, output]


def part_1(opt):
    dig_freq = 0
    for out in opt:
        for i in out:
            if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
                dig_freq += 1
    return dig_freq


def compare(s, t):
    return Counter(s) == Counter(t)


def get_zero(s, six, eight, nine):
    for i in s:
        if len(i) == len(eight) - 1:
            missing = 0
            for j in nine:
                if j not in i:
                    missing += 1
            if missing == 1:
                missing = 0
                for k in six:
                    if k not in i:
                        missing += 1
                if missing == 1:
                    return i


def get_one(s):
    for i in s:
        if len(i) == 2:
            return i


def get_two(s, five, eight):
    for i in s:
        if len(i) == len(eight) - 2:
            missing = 0
            for j in five:
                if j not in i:
                    missing += 1
            if missing == 2:
                return i


def get_three(s, one, eight):
    for i in s:
        if len(i) == len(eight) - 2:
            correct = 0
            for j in one:
                if j in i:
                    correct += 1
            if correct == 2:
                return i


def get_four(s):
    for i in s:
        if len(i) == 4:
            return i


def get_five(s, six, eight):
    for i in s:
        if len(i) == len(eight) - 2:
            missing = 0
            for j in six:
                if j not in i:
                    missing += 1
            if missing == 1:
                return i


def get_six(s, one, eight):
    for i in s:
        if len(i) == len(eight) - 1:
            for j in one:
                if j not in i:
                    return i


def get_seven(s):
    for i in s:
        if len(i) == 3:
            return i


def get_eight(s):
    for i in s:
        if len(i) == 7:
            return i


def get_nine(s, four, eight):
    for i in s:
        if len(i) == len(eight) - 1:
            correct = 0
            for j in four:
                if j in i:
                    correct += 1
            if correct == 4:
                return i


def get_digits(s):
    d = {}
    d.update({1: get_one(s)})
    d.update({4: get_four(s)})
    d.update({7: get_seven(s)})
    d.update({8: get_eight(s)})
    d.update({3: get_three(s, d.get(1), d.get(8))})
    d.update({9: get_nine(s, d.get(4), d.get(8))})
    d.update({6: get_six(s, d.get(1), d.get(8))})
    d.update({5: get_five(s, d.get(6), d.get(8))})
    d.update({2: get_two(s, d.get(5), d.get(8))})
    d.update({0: get_zero(s, d.get(6), d.get(8), d.get(9))})
    temp = {}
    for i in range(10):
        temp.update({''.join(sorted(d.get(i))): str(i)})
    return temp


def get_signal_output(d, opt):
    value = ''
    for i in opt:
        value += d.get(''.join(sorted(i)))
    return value


def part_2(sp, opt):
    values = 0
    for i in range(len(sp)):
        digits = get_digits(sp[i])
        values += int(get_signal_output(digits, opt[i]))
    return values


puzzle = getPuzzle('8dec.txt')
signal_patterns = puzzle[0]
output = puzzle[1]
print(part_1(output))
print(part_2(signal_patterns, output))
