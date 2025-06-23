from collections import defaultdict, deque
g = defaultdict(list)
n, m = map(int, input().split())
into = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    into[v] += 1
q = deque([])
for i in range(n):
    if into[i] == 0: q.append(i)
cnt = 0
while q:
    t = q.popleft()
    cnt += 1
    for i in g[t]:
        into[i] -= 1
        if into[i] == 0:
            q.append(i)

print("No" if cnt == n else "Yes")