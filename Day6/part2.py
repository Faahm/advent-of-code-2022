with open('input.txt') as f:
    data = f.read()

for i in range(0, len(data)-3):
    substring = set(data[i:i+14])
    if len(substring) < 14:
        continue
    else:
        print(i+14)
        break