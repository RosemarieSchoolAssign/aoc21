def getPuzzle(filename):
    p = []
    f = open(filename, 'r')
    for line in f:
        line = line.strip('\n')
        p.append(line)
    return p

p = ['[({(<(())[]>[[{[]{<()<>>',  # what happens at end of line, when False has not been returned?
     '[(()[<>])]({[<{<<[]>>(',  #
     '{([(<{}[<>[]}>{[]{[(<()>',  # should return True - line is corrupted
     '(((({<>}<{<{<>}{[]{[]{}',
     '[[<[([]))<([[{}[[()]]]',
     '[{[{({}]{}}([{[{{{}}([]',
     '{<[[]]>}<{[{[{[]{()[[[]',
     '[<(<(<(<{}))><([]([]()',
     '<{([([[(<>()){}]>(<<{{',
     '<{([{{}}[<[[[<>{}]]]>[]]']


def corrupted(line):
    opening_chars = ['(', '[', '{', '<']
    chars = {')': '(', ']': '[', '}': '{', '>': '<'}
    passed_chars = []
    for char in line:
        if char in opening_chars:
            passed_chars.append(char)
        else:
            corresponding_opening_char = chars.get(char)
            if passed_chars[len(passed_chars) - 1] != corresponding_opening_char:
                return char
            else:
                passed_chars.pop(len(passed_chars) - 1)
    return passed_chars


def get_syntax_points(c):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return points.get(c)


def get_scores(passed_chars):
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for i in passed_chars[::-1]:
        score *= 5
        score += points.get(i)
    return score


def check_puzzle(puzzle):
    syntax = 0
    autocomplete = []
    for line in puzzle:
        r = corrupted(line)
        if len(r) > 1:
            autocomplete.append(get_scores(r))
        else:
            syntax += get_syntax_points(r)
    return syntax, autocomplete


def sort_scores(scores):
    for current in range(1, len(scores)):
        key = scores[current]
        prev = current - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<scores[prev] to key>scores[prev].
        while prev >= 0 and key < scores[prev]:
            scores[prev + 1] = scores[prev]
            prev = prev - 1

        # Place key at after the element just smaller than it.
        scores[prev + 1] = key

    return scores[(len(scores) - 1) // 2]


puzzle = getPuzzle('10dec.txt')
syntax_points, autocomplete_scores = check_puzzle(puzzle)
print(sort_scores(autocomplete_scores))








