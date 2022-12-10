with open('day_5_supply_stacks/input.txt') as f:
    lines = f.readlines()

#supplies = [["Z", "N"], ["M", "C", "D"], ["P"]]
supplies = [["W", "M", "L", "F"],
            ["B", "Z", "V", "M", "F"],
            ["H", "V", "R", "S", "L", "Q"],
            ["F", "S", "V", "Q", "P", "M", "T", "J"],
            ["L", "S", "W"],
            ["F", "V", "P", "M", "R", "J", "W"],
            ["J", "Q", "C", "P", "N", "R", "F"],
            ["V", "H", "P", "S", "Z", "W", "R", "B"],
            ["B", "M", "J", "C", "G", "H", "Z", "W"]]


for line in lines:
    number, from_to = line.strip().split("from")
    number = int(number.split()[1])
    from_stack, _, to_stack = from_to.split()
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1

    for i in range(number):
        supplies[to_stack].append(supplies[from_stack].pop())

for i in supplies:
    print(i[-1], end="")

print()

#supplies = [["Z", "N"], ["M", "C", "D"], ["P"]]
supplies = [["W", "M", "L", "F"],
            ["B", "Z", "V", "M", "F"],
            ["H", "V", "R", "S", "L", "Q"],
            ["F", "S", "V", "Q", "P", "M", "T", "J"],
            ["L", "S", "W"],
            ["F", "V", "P", "M", "R", "J", "W"],
            ["J", "Q", "C", "P", "N", "R", "F"],
            ["V", "H", "P", "S", "Z", "W", "R", "B"],
            ["B", "M", "J", "C", "G", "H", "Z", "W"]]

for line in lines:
    number, from_to = line.strip().split("from")
    number = int(number.split()[1])
    from_stack, _, to_stack = from_to.split()
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1

    idx = len(supplies[from_stack]) - number
    move = supplies[from_stack][idx:]
    supplies[from_stack] = supplies[from_stack][:idx]
    supplies[to_stack].extend(move)


for i in supplies:
    print(i[-1], end="")

    
    