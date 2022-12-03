input = open("c:\\Users\\fatim\\Documents\\repos\\advent of code\\Day1\\input.txt", "r")
sum = 0
calList = []
for line in input:
    try:
        sum = sum + float(line)
    except:
        calList.append(sum)
        sum = 0
calList.sort(reverse=True)
print(calList[0])