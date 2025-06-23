from collections import deque
class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        pass

a = list(map(int, input().split()))
root = node(a[0])
def ad(t, root):
    if t == root.val: return
    if t > root.val:
        if root.right == None:
            root.right = node(t)
            return
        else:
            ad(t, root.right)
    if t < root.val:
        if root.left == None:
            root.left = node(t)
            return
        else:
            ad(t, root.left)

for i in a: ad(i, root)
ans = []
q = deque([])
q.append(root)
while q:
    tmp = q.popleft()
    ans.append(tmp.val)
    if tmp.left: q.append(tmp.left)
    if tmp.right: q.append(tmp.right)
print(*ans)