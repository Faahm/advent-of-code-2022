input = [line.strip().split(',') for line in open("input.txt", "r")]
contained = 0
for i in range((len(input))):
    for j in range(0,len(input[i]),2):
        if input[i][j].split('-')[0] <= input[i][j+1].split('-')[0]:
            if input[i][j].split('-')[1] >= input[i][j+1].split('-')[1]:
                contained += 1
        elif input[i][j+1].split('-')[0] <= input[i][j].split('-')[0]:
            if input[i][j+1].split('-')[1] >= input[i][j].split('-')[1]:
                contained += 1

print(contained)