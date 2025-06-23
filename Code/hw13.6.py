from collections import defaultdict, deque
n, m = map(int, input().split())
g = defaultdict(list)
ru = [0] * n
w = [100] * n
for _ in range(m):
    x, y = map(int, input().split())
    g[y].append(x)
    ru[x] += 1

q = deque([])
for i in range(n):
    if ru[i] == 0: q.append(i)

while q:
    p = q.popleft()
    for i in g[p]:
        ru[i] -= 1
        w[i] = max(w[i], w[p] + 1)
        if ru[i] == 0: q.append(i)

print(sum(w))
