with open('day_10_Cathode-ray_Tube/input.txt') as f:
    lines = f.readlines()

cycle = 1
x = 1
total = 0
cycles_to_report = set([20,60,100,140,180,220])

for line in lines:
    program = line.strip().split()

    if len(program) == 1:
        cycle += 1
        if cycle in cycles_to_report:
            total += cycle * x
    else:
        number = int(program[1])
        cycle += 1
        if cycle in cycles_to_report:
            total += cycle * x
        cycle += 1
        x += number
        if cycle in cycles_to_report:
            total += cycle * x

print(total)