input = open("c:\\Users\\fatim\\Documents\\repos\\advent of code\\Day 1\\input.txt", "r")
sum = 0
calList = []
for line in input:
    try:
        sum = sum + float(line)
    except:
        calList.append(sum)
        sum = 0
calList.sort(reverse=True)
print(calList[0] + calList[1] + calList[2])