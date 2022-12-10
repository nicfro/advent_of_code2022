with open('test/input.txt') as f:
    lines = f.readlines()

class Node: 
    def __init__(self, parent = None):
        self.parent = parent
        self.children = []
        self.size = 0

    def add_file(self, file_size):
        self.size += file_size
        temp = self.parent
        while temp:
            temp.size += file_size
            temp = temp.parent
  
root = Node()
current = root
for line in lines:
    files = []
    if line[0] == "$":
        command = line.split()
        if command[1] == "cd":
            if command[2] == "..":
                current = current.parent
            else:
                temp = Node(parent=current)
                current.children.append(temp)
                current = temp
    else:
        file_size, _ = line.split()
        if file_size.isnumeric():
            current.add_file(int(file_size))
        
res1 = 0
res2 = []
queue = [root.children[0]]
while queue:
    current = queue.pop()
    if current.size < 100000:
        res1 += current.size
    res2.append(current.size)
    queue.extend(current.children)

print(res1)
res2 = sorted(res2)
minimum = 30000000 - (70000000 - res2[-1])
print([i for i in res2 if i > minimum][0])