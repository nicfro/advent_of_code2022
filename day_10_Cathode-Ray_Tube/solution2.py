with open('day_10_Cathode-ray_Tube/test.txt') as f:
    lines = f.readlines()

def update_cycle(steps, cycle, x, add, screen, current_line):
    for i in range(steps):
        if abs((cycle-1) - x) <= 1:
            current_line += '#'
        else:
            current_line += "."
        if cycle % 40 == 0:
            screen.append(current_line)
            current_line = ''
            cycle = 0

        cycle += 1

    x += add
    return cycle, x, screen, current_line
    
    
x = 1
cycle = 1
screen = []
current_line = ''

for line in lines:
    program = line.strip().split()
    if len(program) == 1:
        cycle, x, screen, current_line = update_cycle(1, cycle, x, 0, screen, current_line)
    else:
        cycle, x, screen, current_line = update_cycle(2, cycle, x, int(program[1]), screen, current_line)

[print(*x) for x in screen][0]


