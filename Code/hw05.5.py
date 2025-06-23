from collections import deque
while 1:
    n, p, m = map(int, input().split())
    if p == 0: exit()
    q = deque([])
    out = []
    for i in range(p, n+1): q.append(i)
    for i in range(1, p): q.append(i)
    num = 0
    while q:
        num += 1
        if num == m:
            out.append(str(q.popleft()))
            num = 0
        else:
            q.append(q.popleft())
    print(",".join(out))
        