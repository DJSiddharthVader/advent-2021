import numpy as np
from itertools import product
from functools import reduce


def read_input(infile):
    inputs = [list(map(int, list(x.strip('\n'))))
              for x in open(infile).readlines()]
    inputs = np.array(inputs).reshape((len(inputs), len(inputs[0])))
    return inputs


def get_neighbours_indices(i, j, inputs):
    n, m = inputs.shape[0] - 1, inputs.shape[1] - 1
    if i == 0:
        if j == 0:  # top left corner
            return [(0, 1), (1, 0)]
        elif j == m:  # top right corner
            return [(0, m-1), (1, m)]
        else:  # top row
            return [(0, j-1), (0, j+1), (1, j)]
    elif i == n:
        if j == 0:  # bottom left corner
            return [(n, 1), (n-1, 0)]
        elif j == m:  # bottom right corner
            return [(n, m-1), (n-1, m)]
        else:  # botttom row
            return [(n, j-1), (n, j+1), (n-1, j)]
    else:
        if j == 0:  # left row
            return [(i+1, j), (i-1, j), (i, 1)]
        elif j == m:  # right row
            return [(i+1, j), (i-1, j), (i, m-1)]
        else:
            return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]


def get_neighbours(i, j, inputs):
    return [inputs[k][l] for k, l in get_neighbours_indices(i, j, inputs)]


def star1(inputs):
    ns, ms = range(inputs.shape[0]), range(inputs.shape[1])
    low_points = [inputs[i][j] for i, j in product(ns, ms)
                  if inputs[i][j] < min(get_neighbours(i, j, inputs))]
    print(sum(low_points) + len(low_points))


def expand_basin(basin, inputs):
    all_neighbours = set([cell for i, j in basin
                          for cell in get_neighbours_indices(i, j, inputs)])
    frontier = set(all_neighbours) - set(basin)
    if set([inputs[k][l] for k, l in frontier]) == set([9]):
        return basin
    else:
        basin += [(i, j) for i, j in frontier if inputs[i][j] != 9]
        return expand_basin(basin, inputs)


def star2(inputs):
    ns, ms = range(inputs.shape[0]), range(inputs.shape[1])
    low_points = [(i, j) for i, j in product(ns, ms)
                  if inputs[i][j] < min(get_neighbours(i, j, inputs))]
    basin_sizes = [len(expand_basin([cell], inputs)) for cell in low_points]
    print(reduce(lambda x, y: x*y, sorted(basin_sizes)[-3:]))


if __name__ == '__main__':
    infile = '../inputs/P09.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
