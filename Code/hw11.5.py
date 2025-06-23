from collections import defaultdict
from heapq import *

g = defaultdict(dict)
points = []

for _ in range(int(input())): points.append(input())

for _ in range(int(input())):
    x, y, l = input().split()
    l = int(l)
    g[x][y] = l
    g[y][x] = l

for _ in range(int(input())):
    start, end = input().split()

    dis = {i: int(1e10) for i in points}
    dis[start] = 0

    path = defaultdict(str)
    path[start] = start

    h = [(0, start)]
    while h:
        d, p = heappop(h)
        if d > dis[p]: continue
        for nei in g[p]:
            wei = g[p][nei]
            d1 = d + wei
            if d1 < dis[nei]:
                dis[nei] = d1
                heappush(h, (d1, nei))
                path[nei] = path[p] + f"->({g[p][nei]})->" + nei
    print(path[end])
