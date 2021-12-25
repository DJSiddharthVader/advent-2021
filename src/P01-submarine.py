depths = [int(x.strip('\n')) for x in open('../inputs/P01.txt').readlines()]
# star 1
print(sum([m > depths[i] for i, m in enumerate(depths[1:])]))
# star 2
windows = [depths[0], sum(depths[:2])]
windows += [sum(depths[i-2:i+1]) for i in range(2, len(depths) - 2)]
print(sum([m > windows[i] for i, m in enumerate(windows[1:])]))
