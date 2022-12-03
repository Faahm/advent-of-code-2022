input = open("c:\\Users\\fatim\\Documents\\repos\\advent of code\\Day2\\input.txt", "r")
total = 0
for line in input:
    round = line.split()
    match round[0]:
        case 'A':
            if round[1] == 'X':
                total = total + 1 + 3
            elif round[1] == 'Y':
                total = total + 2 + 6
            elif round[1] == 'Z':
                total = total + 3 + 0
        case 'B':
            if round[1] == 'X':
                total = total + 1 + 0
            elif round[1] == 'Y':
                total = total + 2 + 3
            elif round[1] == 'Z':
                total = total + 3 + 6
        case 'C':
            if round[1] == 'X':
                total = total + 1 + 6
            elif round[1] == 'Y':
                total = total + 2 + 0
            elif round[1] == 'Z':
                total = total + 3 + 3
    print(total)