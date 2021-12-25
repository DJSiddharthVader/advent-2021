def read_input(infile):
    inputs = [x.strip('\n') for x in open(infile).readlines()]
    inputs = [x.split(' | ') for x in inputs]
    inputs = [(x[0].split(' '), x[1].split(' '))
              for x in inputs]
    return inputs


def star1(inputs):
    digit_map = {2: 1, 4: 4, 3: 7, 7: 8}
    total = 0
    for signal, output in inputs:
        for digit in output:
            if len(digit) in digit_map.keys():
                total += 1
    print(total)


def sort(signal):
    return ''.join(sorted(signal))


def check_set(x, check):
    return len(set(x).union(set(check))) == len(set(x))


def build_digit_map(signals):
    # get some digits to figure out segment mapping
    digit_map, key_map = {}, {}
    keys = [sort(signal) for signal in signals]
    # get all the keys known by length
    for key in keys:
        if len(key) == 2:
            digit_map[key] = 1
            key_map[1] = key
        elif len(key) == 3:
            digit_map[key] = 7
            key_map[7] = key
        elif len(key) == 4:
            digit_map[key] = 4
            key_map[4] = key
        elif len(key) == 7:
            digit_map[key] = 8
            key_map[8] = key
    # get string for digit 9,3 using 4,7
    keys_left = [x for x in keys if x not in digit_map.keys()]
    for key in keys_left:
        if len(key) == 6 and check_set(key, key_map[4]):
            digit_map[key] = 9
            key_map[9] = key
        elif len(key) == 5 and check_set(key, key_map[7]):
            digit_map[key] = 3
            key_map[3] = key
    # get string for digit 2 using 8,3
    keys_left = [x for x in keys if x not in digit_map.keys()]
    for key in keys_left:
        if set(key)-set(key_map[3]) == set(key_map[8])-set(key_map[9]):
            digit_map[key] = 2
            key_map[2] = key
    # get string for digit 5 by length
    keys_left = [x for x in keys if x not in digit_map.keys()]
    for key in keys_left:
        if len(key) == 5:
            digit_map[key] = 5
            key_map[5] = key
    # get string for digit 6
    keys_left = [x for x in keys if x not in digit_map.keys()]
    for key in keys_left:
        if len(set(key)-set(key_map[5])) == 2:
            digit_map[key] = 0
        elif len(set(key)-set(key_map[5])) == 1:
            digit_map[key] = 6
    return digit_map


def get_number(signals, outputs):
    digit_map = build_digit_map(signals)
    return int(''.join(str(digit_map[sort(digit)])
                       for digit in outputs))


def star2(inputs):
    print(sum(get_number(signals, outputs)
              for signals, outputs in inputs))


if __name__ == '__main__':
    infile = '../inputs/P08.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
