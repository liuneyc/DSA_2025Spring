from collections import deque
from collections import defaultdict
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sx, sy, ex, ey = 0, 0, 0, 0
for __ in range(int(input())):
    r, c = map(int, input().split())
    m = []
    vis = defaultdict(int)
    for _ in range(r):  m.append(input())
    for i in range(r):
        for j in range(c):
            if m[i][j] == "S":
                sx = i; sy = j
            if m[i][j] == "E":
                ex = i; ey = j
    flag = 0
    q = deque([])
    q.append([sx, sy, 0])
    vis[(sx, sy)] = 1
    while q:
        x0, y0, step0 = q.popleft()
        # print(x0, y0, step0)
        if x0 == ex and y0 == ey:
            print(step0)
            flag = 1
            break
        for i in range(4):
            x1 = x0 + dx[i]
            y1 = y0 + dy[i]
            if 0 <= x1 < r and 0 <= y1 < c and m[x1][y1] != "#" and vis[(x1, y1)] != 1:
                q.append([x1, y1, step0+1])
                vis[(x1, y1)] = 1
    if flag == 0:
        print("oop!")
