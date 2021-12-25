commands = [x.strip('\n').split(' ')
            for x in open('../inputs/P02.txt').readlines()]
# star 1
h, d = 0, 0
for (f, l) in commands:
    if f == 'forward':
        h += int(l)
    elif f == 'down':
        d += int(l)
    elif f == 'up':
        d -= int(l)
print(h, d, h*d)
# star 2
h, d, a = 0, 0, 0
for (f, l) in commands:
    l = int(l)
    if f == 'forward':
        h += l
        d += l*a
    elif f == 'down':
        a += l
    elif f == 'up':
        a -= l
print(a, h, d, h*d)
