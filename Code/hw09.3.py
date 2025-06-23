from heapq import *
input()
w = list(map(int, input().split()))
heapify(w)
ans = 0
while len(w) > 2:
    x1, x2 = heappop(w), heappop(w)
    ans += x1 + x2
    heappush(w, x1+x2)
print(ans+sum(w))