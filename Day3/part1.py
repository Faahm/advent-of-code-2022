from string import ascii_letters
input = open("c:\\Users\\fatim\\Documents\\repos\\advent of code\\Day3\\input.txt", "r")
total = 0
ch = ''
for line in input:
    compartment1 = line[0:int(len(line)/2)]
    compartment2 = line[int(len(line)/2):len(line)]
    for char in compartment1:
        if char in compartment2:
            ch = char
    ascii_letters.index(ch) + 1
    total = total + (ascii_letters.index(ch) + 1)
print(total)