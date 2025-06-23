ans = 0
a = []
def dfs(cnt: int, x: int) -> None:
    global ans, a
    # print(cnt, x)
    if cnt == k:
        ans += 1
        return
    if x > n:
        return
    for i in range(n):
        if a[x][i] == '#' and a[n][i] == 0:
            a[n][i] = 1
            dfs(cnt+1, x+1)
            a[n][i] = 0
        # if a[x][i] == '.':
        #     continue
        # if a[n][i] == 1:
        #     continue
        # a[n][i] = 1
        # dfs(cnt+1, x+1)
        # a[n][i] = 0
    dfs(cnt, x+1)
    return

if __name__ == '__main__':
    while 1:
        n, k = map(int, input().split())
        if n == k == -1:
            exit()
        a = []
        ans = 0
        for _ in range(n):
            a.append(list(input()))
        a.append([0 for _ in range(n)])
        # print(map)
        dfs(0, 0)
        print(ans)
    
    