# from bisect import *
# a = []
# for _ in range(int(input())):
#     t = list(input().split())
#     if len(t) == 1: print(a.pop(0))
#     else:
#         n = int(t[1])
#         i = bisect_left(a, n)
#         a = a[: i] + [n] + a[i:]

from bisect import*
a=[]
for _ in range(int(input())):
 t=input().split()
 print(a.pop(0))if t[0]=='2'else a.insert(bisect_left(a,int(t[1])),int(t[1]))
