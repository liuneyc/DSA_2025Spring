fa = []
def find(x):
    global fa
    if fa[x] == x:return x
    else:fa[x] = find(fa[x]); return fa[x]
while 1:
    n, m = map(int, input().split())
    if n == 0: exit()
    fa = list(range(n+1))
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) != find(b): fa[find(a)] = find(b)
    cnt = 0
    for i in range(n):
        if fa[i+1] == i+1: cnt += 1
    print(cnt)