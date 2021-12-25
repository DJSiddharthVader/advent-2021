from collections import Counter
from collections import defaultdict


def read_input(infile):
    inputs = [x.strip('\n') for x in open(infile).readlines()]
    inputs = list(map(int, inputs[0].split(',')))
    return Counter(inputs)


def star1(inputs, duration, thresh):
    for i in range(duration):
        next_gen = defaultdict(int)
        for k in sorted(inputs.keys()):
            if k == 0:
                next_gen[thresh+2] = inputs[0]
                next_gen[thresh] = inputs[0]
            elif k == thresh+1:
                next_gen[k-1] = inputs[k] + inputs[0]
            else:
                next_gen[k-1] = inputs[k]
        inputs = next_gen
    print(sum(inputs.values()))


if __name__ == '__main__':
    infile = '../inputs/P06.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs, 80, 6)
    print('Star 2 result')
    star1(inputs, 256, 6)
