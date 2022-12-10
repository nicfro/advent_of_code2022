with open('Day_6_Tuning_Trouble/input.txt') as f:
    lines = f.readlines()[0]

for i in range(len(lines)-3):
    if len(set(lines[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(lines)-13):
    if len(set(lines[i:i+14])) == 14:
        print(i+14)
        break