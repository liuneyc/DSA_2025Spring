m, n, xx, yy = 0, 0, 0, 0
mp = [[0] * 20 for _ in range(20)]
ans, cnt = 0, 0
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def check(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < m and mp[x][y] == 0

def dfs(x: int, y: int):
    global ans, cnt, mp
    if cnt == m * n:
        ans += 1
        return
    for i in range(8):
        x1 = x + dx[i]; y1 = y + dy[i]
        if check(x1, y1) == 0:
            continue
        mp[x1][y1] = 1
        cnt += 1
        dfs(x1, y1)
        cnt -= 1
        mp[x1][y1] = 0
    return

for _ in range(int(input())):
    n, m, xx, yy = map(int, input().split())
    mp = mp = [[0] * 20 for _ in range(20)]
    ans, cnt = 0, 1
    mp[xx][yy] = 1
    dfs(xx, yy)
    print(ans)
