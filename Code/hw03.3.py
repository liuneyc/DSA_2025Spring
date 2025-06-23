a = [[0] * 100 for _ in range(100)]
dx = [-1, -1, -2, -2, 1, 1, 2, 2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
xx, yy = 0 , 0
ans = []
alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def check(x, y):
    return 0 < x <= xx and 0 < y <= yy

def dfs(x, y, way):
    if len(way) == xx * yy * 2:
        ans.append(way)
        return
    for i in range(8):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if check(x1, y1) and a[x1][y1] == 0:
            a[x1][y1] = 1
            dfs(x1, y1, way + chr(y1+64) + str(x1))
            a[x1][y1] = 0
            
    

cnt = 0
for _ in range(int(input())):
    ans = []
    cnt += 1
    print(f"Scenario #{cnt}:")
    xx, yy = map(int, input().split())
    a[1][1] = 1
    dfs(1, 1, "A1")
    if len(ans) == 0:
        print("impossible")
    else:
        print(sorted(ans)[0])
    print()