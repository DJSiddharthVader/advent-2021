def read_input(infile):
    inputs = [x.strip('\n') for x in open('../inputs/P03.txt').readlines()]
    return inputs


def most_common(inputs):
    ratios = [sum(int(x[i]) for x in inputs)/len(inputs)
              for i in range(len(inputs[0]))]
    return [1 if r >= 0.5 else 0 for r in ratios]


def least_common(inputs):
    ratios = [sum(int(x[i]) for x in inputs)/len(inputs)
              for i in range(len(inputs[0]))]
    return [1 if r < 0.5 else 0 for r in ratios]


def bin_to_int(binary):
    return sum([2**i if int(r) == 1 else 0 for i, r in enumerate(binary)])


def star1(inputs):
    most_common_bits = most_common(inputs)[::-1]
    least_common_bits = [0 if b == 1 else 1 for b in most_common_bits]
    gamma = bin_to_int(most_common_bits)
    epsilon = bin_to_int(least_common_bits)
    print(gamma, epsilon, gamma*epsilon)


def getRating(inputs, pos, mode):
    if len(inputs) == 1:
        return inputs[0]
    else:
        if mode == 'o2':
            bit = str(most_common(inputs)[pos])
        elif mode == 'co2':
            bit = str(least_common(inputs)[pos])
        inputs_left = [x for x in inputs if x[pos] == bit]
        return getRating(inputs_left, pos+1, mode)


def star2(inputs):
    o2 = bin_to_int(getRating(inputs, 0, 'o2')[::-1])
    co2 = bin_to_int(getRating(inputs, 0, 'co2')[::-1])
    print(o2, co2, o2*co2)


if __name__ == '__main__':
    infile = '../inputs/P03.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
