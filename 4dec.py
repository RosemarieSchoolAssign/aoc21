def getBingo(filename):
    bingo = []
    board = []
    numbers = []
    first_line = True
    f = open(filename, 'r')
    for line in f:
        if first_line:
            first_line = False
            n = line.split(',')
            for i in n:
                numbers.append(int(i))
        else:
            if line == '\n':
                if len(board) > 1:
                    bingo.append(board)
                board = []
            else:
                line = line.strip('\n')
                r = line.split(' ')
                row = []
                for i in r:
                    try:
                        row.append(int(i))
                    except:
                        continue
                board.append(row)
    return [numbers, bingo]


def check_winning_board(board, number):
    for row in board:
        for n in range(len(row)):  # iterates over complete row
            if row[n] == number:  # inserts -1 if number exists
                row[n] = -1
                if complete_column(board, n):
                    return True
                if complete_row(row):
                    return True
    else:
        return False


def get_score(board, number):
    score = number * summarize(board)  # checking if row is complete and summarizes numbers of rest of it
    return score


def complete_row(row):
    for i in row:
        if i != -1:
            return False
    return True


def complete_column(board, i):
    for row in board:
        if row[i] != -1:
            return False
    return True


def summarize(board):
    s = 0
    for row in board:
        for number in row:
            if number >= 0:
                s += number
    return s


def play(numbers, bingo):
    winning_scores = []
    winning_boards = []
    for number in numbers:
        for board in bingo:
            if check_winning_board(board, number):
                score = get_score(board, number)
                winning_scores.append(score)
                winning_boards.append(board)
                bingo.insert(bingo.index(board), [])
                bingo.pop(bingo.index(board))

    return [winning_boards, winning_scores]


puzzle = getBingo('4dec.txt')
res = play(puzzle[0], puzzle[1])
#result = play(numbers, bingo)

#print(res[0])
print(res[1])
