class Node:
    def __init__(self, name, dir=None, file=None, fa=None):
        self.name = name
        self.dir = [] if dir == None else dir
        self.file = [] if file == None else file
        self.fa = fa

a = []
t = 0

def dfs(root: Node, d: int):
    print("|     "*d + root.name)
    for i in root.dir:
        # print(i)
        dfs(i, d+1)
    for i in sorted(root.file):
        print("|     "*d + i)

cnt = 0
while 1:
    a = []
    cnt += 1
    while 1:
        tmp = input()
        if tmp == "*": break
        elif tmp == "#": exit()
        else: a.append(tmp)
    root = Node("ROOT")
    cur = root
    for tmp in a:
        # print(tmp)
        if tmp == "]":
            cur = cur.fa
        elif tmp[0] == "f":
            cur.file.append(tmp)
        elif tmp[0] == "d":
            new = Node(name=tmp, fa=cur)
            cur.dir.append(new)
            cur = new
    
    print(f"DATA SET {cnt}:")
    dfs(root, 0)
    print()
    
    