# Credits to https://github.com/HellFireInfernoStorm
with open('input.txt') as f:
    data = f.read().splitlines()

stacks = {i : [] for i in range(1,10)}

for i in range(7,-1,-1):
    for j in range(1,10):
        c = data[i][j*4-3]
        if c != ' ':
            stacks[j].append(c)
# End of Credits
for line in data[10:]:
    instructions = line.split()
    qty = int(instructions[1])
    start = int(instructions[3])
    end = int(instructions[5])
    # accesses key, gets last n elements
    stacks[end] += stacks[start][-qty:]
    del stacks[start][-qty:]

for stack in stacks:
    print(stacks[stack][-1], end='')
