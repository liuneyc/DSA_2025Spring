from collections import defaultdict
from heapq import *

n = int(input())
g = defaultdict(list)
zs = dict()
sz = []
pts = set()
for c in range(n-1):
    t = list(input().split())
    p = t[0]
    zs[p] = c
    pts.add(p)
    g[p] = []
    sz.append(p)
    t = t[2:]
    for i in range(len(t)//2):
        g[p].append([t[i*2], int(t[i*2+1])])
        pts.add(t[i*2])
        # g[t[i*2]].append([p, int(t[i*2+1])])
# print(zs)
for i in pts:
    if i not in g:
        zs[i] = n-1
        sz.append(i)
# print(zs)

f = [i for i in range(n)]
def find(x):
    if f[x] == x: return x
    f[x] = find(f[x])
    return f[x]
h = []
for i in g.keys():
    for j, d in g[i]:
        heappush(h, [d, i, j])
# print(h)
ans = 0
for _ in range(n-1):
    # print(h)
    # print(f)
    # print(find(zs["E"]), find(zs["F"]))
    while find(zs[h[0][1]]) == find(zs[h[0][2]]): heappop(h)
    d, x, y = heappop(h)
    ans += d
    f[find(zs[x])] = find(zs[y])
    # print(ans)
print(ans)