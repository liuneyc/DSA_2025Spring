from collections import defaultdict, deque

g = defaultdict(list)
n = int(input())
for _ in range(n):
    w = input()
    for i in range(4):
        t = w[:i] + "*" + w[i+1:]
        g[t].append(w)

def find(w):
    ans = set()
    for i in range(4):
        t = w[:i] + "*" + w[i+1:]
        for j in g[t]:
            ans.add(j)
    return ans


q = deque([])
x, y = input().split()
q.append([x, [x]])
vis = set()
flag = 0
while q:
    w0, way = q.popleft()
    if w0 in vis: continue
    if w0 == y:
        flag = 1
        print(*way)
        break
    vis.add(w0)
    for w1 in find(w0):
        way1 = way + [w1]
        if w1 not in vis:
            q.append([w1, way1])

if flag == 0: print("NO")