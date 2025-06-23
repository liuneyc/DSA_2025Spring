class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r
a = ''
t = 0
def build(x):
    global t
    t = x
    if a[x] == ".": return None
    return Node(a[x], l=build(x+1), r=build(t+1))

a = input()
root = build(0)
ans = []
def dfs(root: Node):
    global ans
    if root.l: dfs(root.l)
    ans.append(root.val)
    if root.r: dfs(root.r)
dfs(root)
print("".join(ans))

ans = []
def dfs2(root: Node):
    global ans
    if root.l: dfs2(root.l)
    if root.r: dfs2(root.r)
    ans.append(root.val)
dfs2(root)
print("".join(ans))
