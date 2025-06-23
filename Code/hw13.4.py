from heapq import *
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for x, y, p in flights:
            g[x].append((y, p))
        vis = set()
        h = [(0, src, 0)]
        mp = [[1e9]*(k+2) for _ in range(n)]
        while h:
            p, c, k0 = heappop(h)
            if (c, k0) in vis: continue
            # print(p, c, k0)
            vis.add((c, k0))
            mp[c][k0] = min(mp[c][k0], p)
            if k0 > k: continue
            for c1, p1 in g[c]:
                heappush(h, (p+p1, c1, k0+1))
        
        if min(mp[dst]) == 1e9: return -1
        else: return min(mp[dst])
