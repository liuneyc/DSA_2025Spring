from collections import defaultdict
from heapq import *
n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    x, y, d = map(int, input().split())
    g[x].append((y, d))
vis = set()
d = [float('inf')] * (n + 1)
h = [(0, 1)]
while h:
    dis, p = heappop(h)
    if p in vis: continue
    vis.add(p)
    d[p] = min(d[p], dis)
    for p1, d1 in g[p]:
        if d[p1] > dis + d1:
            heappush(h, (dis + d1, p1))
            d[p1] = min(d[p1], dis+d1)


print(d[n])