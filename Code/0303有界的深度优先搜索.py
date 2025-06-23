n, m, l = map(int, input().split())
a, vis = [[0] * n for _ in range(n)], [0] * n
for _ in range(m):
    i, j = map(int, input().split())
    a[i][j], a[j][i] = 1, 1
def dfs(p, c):
    if vis[p] == 1 or c > l:return
    print(p, end=" ")
    vis[p] = 1
    for i in range(n):
        if a[p][i] == 1 and vis[i] == 0:dfs(i, c+1)
s = int(input())
dfs(s, 0)



# n,m,l=map(int,input().split())
# a=[[0]*n for _ in[0]*n]
# v=[0]*n
# exec('i,j=map(int,input().split());a[i][j]=a[j][i]=1;'*m)
# def d(p,c):
#  if v[p]or c>l:return
#  print(p,end=' ')
#  v[p]=1
#  [d(i,c+1)for i in range(n)if a[p][i]and~-v[i]]
# d(int(input()),0)