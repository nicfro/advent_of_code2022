with open('Day_1_Calorie_Counting/input.txt') as f:
    lines = f.readlines()

total = 0
max_calories = []
for line in lines:
    number = line.strip()
    if number:
        total += int(number)
    else:
        max_calories.append(total)
        total = 0
max_calories = sorted(max_calories, reverse=True)

print(max_calories[0])
print(sum(max_calories[0:3]))

