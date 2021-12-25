import numpy as np


def read_input(infile):
    inputs = list(map(int, open(infile).readlines()[0].strip('\n').split(',')))
    return np.array(inputs)


def total_cost(inputs, pos):
    return np.sum(np.abs(inputs - pos))


def total_cost2(inputs, pos):
    return np.sum([np.sum(np.arange(1, x+1)) for x in np.abs(inputs - pos)])


def star1(inputs):
    costs = {p: total_cost(inputs, p)
             for p in range(np.min(inputs), np.max(inputs))}
    min_pos, min_cost = np.inf, np.inf
    for pos, cost in costs.items():
        if cost < min_cost:
            min_pos, min_cost = pos, cost
    print(min_pos, min_cost)


def star2(inputs):
    costs = {p: total_cost2(inputs, p)
             for p in range(np.min(inputs), np.max(inputs))}
    min_pos, min_cost = np.inf, np.inf
    for pos, cost in costs.items():
        if cost < min_cost:
            min_pos, min_cost = pos, cost
    print(min_pos, min_cost)


if __name__ == '__main__':
    infile = '../inputs/P07.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
