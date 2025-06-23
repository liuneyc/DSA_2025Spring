from heapq import *
from collections import defaultdict, deque
def d(x1, y1, x2, y2):
    return ((x1-x2) ** 2 + (y1 - y2) ** 2) ** 0.5


sx, sy, ex, ey = map(int, input().split())
g = defaultdict(list)
g[(ex, ey)] = []
g[(sx, sy)] = []

md = dict()
md[(sx, sy)] = 0
md[(ex, ey)] = float("inf")

vis = set()

while 1:
    try:
        t = list(map(int, input().split()))
        x0, y0 = t[0], t[1]
        for i in range(1, len(t)//2-1):
            x1, y1 = t[i*2], t[i*2+1]
            g[(x0, y0)].append((x1, y1))
            g[(x1, y1)].append((x0, y0))
            x0, y0 = x1, y1
    except EOFError:
        break
# print(g)
h = [(0, sx, sy)]

while h:
    d0, x0, y0 = heappop(h)
    if d0 > md[(x0, y0)] or (x0, y0) in vis: continue
    if x0 == ex and y0 == ey: break
    for x1, y1 in g.keys():
        if x1 == x0 and y1 == y0: continue
        if (x1, y1) in g[(x0, y0)]:
            d1 = d0 + d(x0, y0, x1, y1) / 4
        else: d1 = d0 + d(x0, y0, x1, y1)
        if (x1, y1) not in md or md[(x1, y1)] > d1:
            md[(x1, y1)] = d1
            heappush(h, (d1, x1, y1))

# print(md[(ex, ey)])
print(round(md[(ex, ey)] / 1000 / 10 * 60))


