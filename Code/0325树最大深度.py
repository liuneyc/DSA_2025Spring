class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
n = int(input())
a = [0] * (n+1)
for i in range(n+1):
    a[i] = Node(i)
for i in range(1, n+1):
    l, r = map(int, input().split())
    if l != -1: a[i].left = a[l]
    if r != -1: a[i].right = a[r]
ans = 0
def dfs(root: Node, x):
    global ans
    ans = max(ans, x)
    if root.left: dfs(root.left, x+1)
    if root.right: dfs(root.right, x+1)
dfs(a[1], 1)
print(ans)