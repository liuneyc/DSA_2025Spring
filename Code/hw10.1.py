class Vertix:
    def __init__(self, name):
        self.name = name
        self.edge = []

    def add_edge(self, v):
        self.edge.append(v)

class Graph:
    def __init__(self, n):
        self.ver = {}
        self.point = n

    def add_ver(self, a):
        self.ver[a] = Vertix(a)

    def add_edge(self, a, b):
        if a not in self.ver: self.add_ver(a)
        if b not in self.ver: self.add_ver(b)
        self.ver[a].add_edge(b)
        self.ver[b].add_edge(a)
    
    def make(self):
        d = [[0]*n for _ in range(n)]
        a = [[0]*n for _ in range(n)]
        for i in self.ver.keys():
            d[i][i] = len(self.ver[i].edge)
            for j in self.ver[i].edge:
                a[i][j] = 1
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[i][j] = d[i][j] - a[i][j]
        return ans


n, m = map(int, input().split())
g = Graph(n)
for _ in range(m):
    a, b = map(int, input().split())
    g.add_edge(a, b)
ans = g.make()
for i in ans: print(*i)