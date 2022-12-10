with open('day_8_Treetop_Tree_house/input.txt') as f:
    lines = f.readlines()

tree_rows = []
for line in lines:
    tree_rows.append([int(x) for x in line.strip()])

def calculate_points(tree_rows, i, j):
    value = tree_rows[i][j]
    visible = False

    left_counter = 0
    #check from left
    for k in range(j-1,-1, -1):
        if tree_rows[i][k] < value:
            left_counter += 1
        else:
            left_counter += 1
            break
    else:
        visible = True

    right_counter = 0
    #check from right
    for k in range(j+1, len(tree_rows[0])):
        if tree_rows[i][k] < value:
            right_counter += 1
        else:
            right_counter += 1
            break
    else:
        visible = True

    top_counter = 0
    #check from top
    for k in range(i-1,-1, -1):
        if tree_rows[k][j] < value:
            top_counter += 1
        else:
            top_counter += 1
            break
    else:
        visible = True

    bottom_counter = 0
    #check from bottom
    for k in range(i+1, len(tree_rows)):
        if tree_rows[k][j] < value:
            bottom_counter += 1
        else:
            bottom_counter += 1
            break
    else:
        visible = True
    return left_counter * right_counter * top_counter * bottom_counter, visible

res = 0
seen = 0
for i in range(len(tree_rows)):
    for j in range(len(tree_rows[0])):

        points, visible = calculate_points(tree_rows, i, j)
        seen += visible
        res = max(res, points)

print(res, seen)
