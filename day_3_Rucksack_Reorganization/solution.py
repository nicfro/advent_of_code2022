with open('day_3_Rucksack_Reorganization/input.txt') as f:
    lines = f.readlines()

total = 0
lines = [x.strip() for x in lines]
total = 0
for line in lines:
    length = len(line)//2
    first = line[0:length]
    second = line[length:]
    result = set(first).intersection(second).pop()
    if result.isupper():
        result = ord(result.lower()) - 70
    else:
        result = ord(result) - 96
    total += result

print(total)

total = 0
lines = [x.strip() for x in lines]
current = 0
while current < len(lines):
    first = lines[current]
    second = lines[current+1]
    third = lines[current+2]

    result = set(first).intersection(second).intersection(third).pop()

    if result.isupper():
        result = ord(result.lower()) - 70
    else:
        result = ord(result) - 96
    total += result
    current += 3

print(total)
