with open('input.txt') as f:
    data = f.read()

for i in range(0, len(data)-3):
    substring = set(data[i:i+4])
    if len(substring) < 4:
        continue
    else:
        print(i+4)
        break