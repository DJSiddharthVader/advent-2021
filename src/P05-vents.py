import numpy as np


def read_input(infile):
    inputs = [x.strip('\n').replace(' -> ', ',').split(',')
              for x in open(infile).readlines()]
    inputs = [list(map(int, x)) for x in inputs]
    return inputs


def enumerate_line(line):
    x1, y1, x2, y2 = line
    positions = [(x2, y2)]
    while not (x1 == x2 and y1 == y2):
        positions += [(x1, y1)]
        if x1 > x2:
            x1 -= 1
        elif x1 < x2:
            x1 += 1
        if y1 > y2:
            y1 -= 1
        elif y1 < y2:
            y1 += 1
    return positions


def star1(inputs, thresh):
    n = max(max(x) for x in inputs) + 1
    diagram = np.zeros((n, n))
    for line in inputs:
        x1, y1, x2, y2 = line
        if x1 == x2 or y1 == y2:
            for i, j in enumerate_line(line):
                diagram[i][j] += 1
    overlaps = 0
    for row in diagram:
        for cell in row:
            if cell >= thresh:
                overlaps += 1
    print(np.sum(diagram), overlaps)


def star2(inputs, thresh):
    n = max(max(x) for x in inputs) + 1
    diagram = np.zeros((n, n))
    for line in inputs:
        for i, j in enumerate_line(line):
            diagram[i][j] += 1
    overlaps = 0
    for row in diagram:
        for cell in row:
            if cell >= thresh:
                overlaps += 1
    print(np.sum(diagram), overlaps)


if __name__ == '__main__':
    infile = '../inputs/P05.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs, 2)
    print('Star 2 result')
    star2(inputs, 2)
