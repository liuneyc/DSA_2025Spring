from collections import defaultdict, deque

class bnode:
    def __init__(self, val, left=None, right=None, fa=None):
        self.val = val
        self.left = left
        self.right = right
        self.fa = fa
    
    def add(self, son):
        print(self.val, son.val)
        if self.left == None: self.left = son
        else: self.right = son

class cnode:
    def __init__(self, val, son=None, fa=None):
        self.val = val
        self.son = [] if son == None else son
        self.fa = fa

def build(root: bnode):
    if root.val == "$": return None
    ans = cnode(root.val)
    son = []
    cur = root.left
    while cur != None:
        if cur.val == "$": break
        son.append(build(cur))
        cur = cur.right
    ans.son = son[::-1]
    return ans
    

n = int(input())
a = deque([])
for i in list(input().split()):
    a.append([i[0], int(i[1])])

def make():
    global a
    x, y = a.popleft()
    tmp = bnode(x)
    if y == 1: return tmp
    else:
        tmp.left = make()
        tmp.right = make()
        return tmp

root = make()

b = build(root)

q = deque([])
q.append(b)
ans = []
while q:
    for _ in range(len(q)):
        tmp = q.popleft()
        ans.append(tmp.val)
        for i in tmp.son:
            q.append(i)

print(*ans)
