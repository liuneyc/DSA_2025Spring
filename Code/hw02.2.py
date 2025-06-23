m, n, p, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [list(map(int, input().split())) for _ in range(p)]
ans = [[0] * (n+1-q) for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for x in range(p):
            for y in range(q):
                ans[i][j] += a[x+i][y+j] * b[x][y]
for i in ans:
    print(*i)

# m,n,p,q=map(int,input().split())
# a=[[*map(int,input().split())]for _ in[0]*m]
# b=[[*map(int,input().split())]for _ in[0]*p]
# print('\n'.join(' '.join(map(str,[sum(a[i+x][j+y]*b[x][y]for x in range(p)for y in range(q))for j in range(n-q+1)]))for i in range(m-p+1)))