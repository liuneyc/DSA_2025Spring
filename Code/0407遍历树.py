class node:
    def __init__(self, val, son=None):
        self.val = val
        self.son = [] if son == None else son


n = int(input())
a = {}
rt = set()
s = set()
for i in range(n):
    tmp = list(map(int, input().split()))
    v = tmp[0]
    son = tmp[1:]
    rt.add(v)
    for t in son: s.add(t)
    if v not in a:
        a[v] = node(v)
    for j in son:
        if j not in a:
            a[j] = node(j)
        a[v].son.append(a[j])

root = a[list(rt-s)[0]]
ans = []

def dfs(root: node):
    # print(f"root={root.val}")
    tmp = [root]+root.son
    # for i in root.son: tmp.append(i)
    tmp.sort(key=lambda x: x.val)
    # print([i.val for i in tmp])
    for i in tmp:
        if i == root:
            ans.append(i.val)
        else: dfs(i)
    pass



# def dfs(root: node):
#     ans.append(root.val)  # 先处理当前节点
#     # 对子节点按值排序后递归处理
#     for son in sorted(root.son, key=lambda x: x.val):
#         dfs(son)


dfs(root)
for i in ans:
    print(i)