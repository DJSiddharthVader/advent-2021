from functools import reduce
lefts, rights = '([{<', ')]}>'
pairs = {left: right for left, right in zip(lefts, rights)}


def read_input(infile):
    inputs = [x.strip('\n') for x in open(infile).readlines()]
    return inputs


def get_first_illegal(symbols):
    stack = ''
    for symbol in symbols:
        if symbol in lefts:
            stack += symbol
        elif symbol in rights:
            if symbol == pairs[stack[-1]]:
                stack = stack[:-1]
            else:
                return symbol
    return ''.join([pairs[symbol] for symbol in stack[::-1]])


def star1(inputs):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    illegals = []
    for symbols in inputs:
        first_illegal = get_first_illegal(symbols)
        if len(first_illegal) == 1:
            illegals.append(first_illegal)
    print(sum(scores[s] for s in illegals))


def star2(inputs):
    score_chart = {')': 1, ']': 2, '}': 3, '>': 4}
    line_scores = []
    for symbols in inputs:
        result = get_first_illegal(symbols)
        if len(result) > 1:
            scores = [0] + [score_chart[x] for x in result]
            line_scores.append(reduce(lambda x, y: x*5+y, scores))
    print(sorted(line_scores)[int(len(line_scores)/2)])


if __name__ == '__main__':
    infile = '../inputs/P10.txt'
    inputs = read_input(infile)
    print('Star 1 result')
    star1(inputs)
    print('Star 2 result')
    star2(inputs)
