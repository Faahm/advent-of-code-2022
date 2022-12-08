count = 0
# Credits to https://github.com/HellFireInfernoStorm
with open('input.txt') as f:
    for line in f:
        line = [[int(n) for n in pair.split('-')] for pair in line.strip().split(',')]
        a, b = line[0][0], line[0][1]
        c, d = line[1][0], line[1][1]
# End of Credits
        if not (b < c or d < a):
            count += 1

print(count)
