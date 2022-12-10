with open('day_9_Rope_Bridge/input.txt') as f:
    lines = f.readlines()

visited = set()
knots = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
#knots = [(0,0), (0,0)]

def update_tail(head,tail):
    if (((head[0] - tail[0])**2 + (head[1] - tail[1])**2)**0.5) > 1.5:
        up_down = head[0] - tail[0]
        left_right = head[1] - tail[1]

        if up_down > 0 and left_right == 0:
            return (tail[0] + 1 , tail[1])
        elif up_down < 0 and left_right == 0:
            return (tail[0] - 1 , tail[1])

        elif up_down == 0 and left_right > 0:
            return (tail[0] , tail[1] + 1)
        elif up_down == 0 and left_right < 0:
            return (tail[0] , tail[1] - 1)

        elif up_down > 0 and left_right > 0:
            return (tail[0] + 1 , tail[1] + 1)
        elif up_down > 0 and left_right < 0:
            return (tail[0] + 1 , tail[1] - 1)
            
        elif up_down < 0 and left_right > 0:
            return (tail[0] - 1 , tail[1] + 1)
        elif up_down < 0 and left_right < 0:
            return (tail[0] - 1 , tail[1] - 1)
    else:
        return tail

for line in lines:
    direction, length = line.strip().split()
    for i in range(int(length)):
        match direction:
            case "R":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            case "L":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            case "U":
                knots[0] = (knots[0][0] + 1, knots[0][1])
            case "D":
                knots[0] = (knots[0][0] - 1, knots[0][1])

        for i in range(len(knots)-1):
            knots[i+1] = update_tail(knots[i], knots[i+1])
        visited.add(knots[-1])

print(len(visited))