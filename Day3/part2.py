from string import ascii_letters
input =[line.strip() for line in open("input.txt", "r")]
sum = 0
for i in range(0,len(input),3):
    compartment1 = input[i]
    compartment2 = input[i+1]
    compartment3 = input[i+2]
    item = (set(compartment1) & set(compartment2) & set(compartment3)).pop()
    sum += (ascii_letters.index(item) + 1)
print(sum)