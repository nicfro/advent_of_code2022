from collections import defaultdict
from collections import deque


arr = []
with open("day_12_Hill_Climbing_Algorithm/test.txt") as f:
    i = 0
    for line in f:
        x = line.strip()
        transformed_line = [ord(i) - 96 for i in x]
        if -13 in transformed_line:
            j_start = transformed_line.index(-13)
            start = (i, j_start)
            transformed_line[j_start] = 0
        if -27 in transformed_line:
            j_end = transformed_line.index(-27)
            end = (i, j_end)
            transformed_line[j_end] = 27
        arr.append(transformed_line)
        i += 1

width = len(arr)
height = len(arr[0])


def get_adjacent(i, j):
    value = arr[i][j]
    res = []
    if i > 0 and abs(arr[i - 1][j] - value) <= 1:
        res.append((i - 1, j))
    if i < (width - 1) and abs(arr[i + 1][j] - value) <= 1:
        res.append((i + 1, j))
    if j > 0 and abs(arr[i][j - 1] - value) <= 1:
        res.append((i, j - 1))
    if j < (height - 1) and abs(arr[i][j + 1] - value) <= 1:
        res.append((i, j + 1))
    return res


graph = defaultdict(lambda: defaultdict(list))

for i in range(width):
    for j in range(height):
        graph[(i, j)] = set(get_adjacent(i, j))


def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        vertex, path = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for next in graph[vertex]:
                if next == end:
                    return path + [next]
                if next not in visited:
                    queue.append((next, path + [next]))
    return []


"""
def bfs(graph, start, end):
    queue = deque([(start, [start], set())])
    while queue:
        vertex, path, visited = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for next in graph[vertex]:
                if next == end:
                    return path + [next]
                if next not in visited:
                    queue.append((next, path + [next], visited))
    return []
"""

path = bfs(graph, start, end)
print(path)

# for i, j in res[1]:
#    print(arr[i][j], end=" ")
