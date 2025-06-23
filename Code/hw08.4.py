class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        pass

def build(a: str, b: str):
    # print(f"{a}-{b}")
    if len(a) == 1: return node(a) 
    if len(a) == 0: return None
    tmp = node(a[0])
    d = b.index(a[0])
    tmp.left = build(a[1: d+1], b[0: d])
    tmp.right = build(a[d+1:], b[d+1:])
    return tmp

ans = ""

def dfs(root: node):
    global ans
    if root.left: dfs(root.left)
    if root.right: dfs(root.right)
    ans += root.val

while 1:
    try:
        a = input()
        b = input()
        t = build(a, b)
        ans = ""
        dfs(t)
        print(ans)
        pass
    except EOFError:
        break