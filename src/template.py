def read_input(infile):
    inputs = [x.strip('\n') for x in open(infile).readlines()]
    return inputs


def star1(inputs):
    print(None)


def star2(inputs):
    print(None)


if __name__ == '__main__':
    infile = '../inputs/P.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
