with open('input.txt') as f:
    lines = f.readlines()

total_score = 0
for line in lines:
    p1, p2 = line.split()
    
    result = 0
    if p2 == "X":
        result += 1
        if p1 == "A":
            result += 3
        if p1 == "C":
            result += 6
    if p2 == "Y":
        result += 2
        if p1 == "B":
            result += 3
        if p1 == "A":
            result += 6
    if p2 == "Z":
        result += 3
        if p1 == "C":
            result += 3
        if p1 == "B":
            result += 6

    total_score += result

print(total_score)

total_score = 0
for line in lines:
    p1, p2 = line.split()
    
    result = 0
    if p1 == "A":
        if p2 == "X":
            result += 3
        if p2 == "Y":
            result += 1
            result += 3
        if p2 == "Z":
            result += 2
            result += 6
    if p1 == "B":
        if p2 == "X":
            result += 1
        if p2 == "Y":
            result += 2
            result += 3
        if p2 == "Z":
            result += 3
            result += 6
    if p1 == "C":
        if p2 == "X":
            result += 2
        if p2 == "Y":
            result += 3
            result += 3
        if p2 == "Z":
            result += 1
            result += 6
    total_score += result

print(total_score)