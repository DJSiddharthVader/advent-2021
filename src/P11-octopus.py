import numpy as np


def read_input(infile):
    inputs = [list(map(int, list(x.strip('\n'))))
              for x in open(infile).readlines()]
    inputs = np.array(inputs).reshape((len(inputs), len(inputs[0])))
    return inputs


def in_board(i, j, inputs):
    n, m = inputs.shape
    if i >= 0 and i < n and j >= 0 and j < m:
        return True
    else:
        return False


def get_neighbours_indices(i, j, inputs):
    neighbours = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2)]
    neighbours = [(x, y) for x, y in neighbours if in_board(x, y, inputs)]
    return [(x, y) for x, y in neighbours if not (x == i and y == j)]


def flash_octopi(inputs):
    inputs += 1
    flashing, flashed = set([(-1, -1)]), set()  # dummy to enter loop
    while len(flashing) != 0:
        flashing = set(zip(*np.where(inputs > 9)))
        flashing, flashed = flashing - flashed, flashed.union(flashing)
        neighbours = [(i, j) for x, y in flashing
                      for i, j in get_neighbours_indices(x, y, inputs)]
        for i, j in neighbours:
            inputs[i][j] += 1
    return inputs


def star1(inputs, steps=100):
    total_flashes = 0
    for step in range(steps):
        inputs = flash_octopi(inputs)
        total_flashes += len(np.where(inputs > 9)[0])
        inputs = np.where(inputs > 9, 0, inputs)
    print(total_flashes)


def star2(inputs):
    step, n, m = 0, inputs.shape[0], inputs.shape[1]
    step_flashes = 1
    while step_flashes != n*m:
        inputs = flash_octopi(inputs)
        step_flashes = len(np.where(inputs > 9)[0])
        inputs = np.where(inputs > 9, 0, inputs)
        step += 1
    print(step)


if __name__ == '__main__':
    infile = '../inputs/P11.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
