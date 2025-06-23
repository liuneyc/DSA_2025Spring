class Node:
    def __init__(self, val, son=None):
        self.val = val
        self.son = {} if son == None else son
        self.isend = False

for __ in range(int(input())):
    flag = 1
    n = int(input())
    nb = [input() for _ in range(n)]
    root = Node(0)
    for num in nb:
        cur = root
        for i in range(len(num)):
            if cur.isend == True: flag = 0
            elif num[i] in cur.son:
                cur = cur.son[num[i]]
                if i == len(num) - 1:
                    flag = 0
            else:
                cur.son[num[i]] = Node(num[i])
                cur = cur.son[num[i]]
            if i == len(num) - 1:
                cur.isend = True
    print("YES" if flag == 1 else "NO")