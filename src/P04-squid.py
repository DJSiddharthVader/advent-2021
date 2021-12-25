import numpy as np


def parse_line(line):
    return [int(line[i:i+2].strip(' '))
            for i in range(0, len(line), 3)]


def read_input(infile):
    inputs = [x.strip('\n')
              for x in open(infile).readlines() if x != '\n']
    numbers = list(map(int, inputs[0].split(',')))
    boards = []
    for b in range(1, len(inputs), 5):
        board = [parse_line(inputs[j])
                 for j in range(b, b+5)]
        boards.append(np.array(board))
    return numbers, boards


def mark_board(board, num):
    for i, row in enumerate(board):
        for j, cell in enumerate(board[i]):
            if cell == num:
                return i, j
    return False


def is_solved(mboard):
    n, m = mboard.shape
    for i in range(n):
        if sum(mboard[i]) == n:
            return True
    mboard = mboard.T
    for j in range(m):
        if sum(mboard[j]) == m:
            return True
    return False


def score_board(mboard, board, num):
    total = 0
    for i, row in enumerate(mboard):
        for j, cell in enumerate(row):
            if cell == 0:
                total += board[i][j]
    return total * num


def solve_board(board, numbers):
    mboard = np.zeros(board.shape)
    for turn, num in enumerate(numbers):
        tmp = mark_board(board, num)
        if tmp:
            i, j = tmp
            mboard[i][j] = 1
            if is_solved(mboard):
                return turn, score_board(mboard, board, num)
    return None, None


def star1(boards, numbers):
    w_board, w_turn, w_score = np.inf, np.inf, np.inf
    for b, board in enumerate(boards):
        turn, score = solve_board(board, numbers)
        if turn < w_turn:
            w_board, w_turn, w_score = b, turn, score
    print(w_board, w_turn, w_score)


def star2(boards, numbers):
    w_board, w_turn, w_score = -1, 0, 0
    for b, board in enumerate(boards):
        turn, score = solve_board(board, numbers)
        if turn > w_turn:
            w_board, w_turn, w_score = b, turn, score
    print(w_board, w_turn, w_score)


if __name__ == '__main__':
    infile = '../inputs/P04.txt'
    numbers, boards = read_input(infile)
    print('Star 1 result')
    star1(boards, numbers)
    print('Star 2 result')
    star2(boards, numbers)
