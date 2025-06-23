from heapq import *

f = [0]
def find(x):
    if f[x] == x: return x
    else:
        f[x] = find(f[x])
        return f[x]

while 1:
    try:
        n = int(input())
        g = []
        h = []
        for _ in range(n):
            g.append(list(map(int, input().split())))
        f = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                heappush(h, (g[i][j], i, j))
                
        ans = 0
        for _ in range(n-1):
            while find(h[0][1]) == find(h[0][2]):
                heappop(h)
            d, i, j = heappop(h)
            f[find(i)] = find(j)
            ans += d
        print(ans)

    except EOFError:
        break