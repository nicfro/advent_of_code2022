from tqdm import tqdm

with open("day_11_Monkey_in_the_Middle/test.txt") as f:
    lines = f.readlines()

monkeys = {}
for line in lines:
    if line != "\n":
        pattern = line.split(":")[0].strip().split()[0]
        match pattern:
            case "Monkey":
                current_monkey = line.split(":")[0]
                monkeys[current_monkey] = {}
            case "Starting":
                items = [x for x in line.split(":")[1].strip().split(",")]
                monkeys[current_monkey]["items"] = items
            case "Operation":
                operation = line.split("=")[1].strip().split(" ")
                monkeys[current_monkey]["operation"] = operation
            case "Test":
                test = line.strip().split(" ")[-1]
                monkeys[current_monkey]["test"] = int(test)
            case "If":
                to_monkey = line.strip().split(" ")[-1]
                state = True if line.strip().split(" ")[1] == "true:" else False
                monkeys[current_monkey][state] = f"Monkey {to_monkey}"
    monkeys[current_monkey]["inspections"] = 0


def monkey_business(monkey, monkeys):
    while monkeys[monkey]["items"]:
        item = monkeys[monkey]["items"].pop(0)
        operations = monkeys[monkey]["operation"]
        worry = eval("".join([item if x == "old" else x for x in operations])) // 3
        test = worry % monkeys[monkey]["test"] == 0
        to_monkey = monkeys[monkey][test]
        monkeys[to_monkey]["items"].append(str(worry))
        monkeys[monkey]["inspections"] += 1


monkey_queue = list(sorted(monkeys.keys()))
for i in tqdm(range(20)):
    for monkey in monkey_queue:
        monkey_business(monkey, monkeys)

inspections = []
for monkey in monkey_queue:
    inspections.append(monkeys[monkey]["inspections"])

inspections = sorted(inspections, reverse=True)
print(inspections[0] * inspections[1])
