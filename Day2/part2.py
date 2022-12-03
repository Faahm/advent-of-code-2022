input = open("c:\\Users\\fatim\\Documents\\repos\\advent of code\\Day2\\input.txt", "r")
total = 0
for line in input:
    round = line.split()
    match round[1]:
        case 'X':
            if round[0] == 'A':
                total = total + 3 + 0
            elif round[0] == 'B':
                total = total + 1 + 0
            elif round[0] == 'C':
                total = total + 2 + 0
        case 'Y':
            if round[0] == 'A':
                total = total + 1 + 3
            elif round[0] == 'B':
                total = total + 2 + 3
            elif round[0] == 'C':
                total = total + 3 + 3
        case 'Z':
            if round[0] == 'A':
                total = total + 2 + 6
            elif round[0] == 'B':
                total = total + 3 + 6
            elif round[0] == 'C':
                total = total + 1 + 6

print(total)