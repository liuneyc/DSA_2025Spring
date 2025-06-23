from heapq import *

for __ in range(int(input())):
    m, n = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    heapify(a)
    for _ in range(m-1):
        b = sorted(list(map(int, input().split())))
        h = []
        a1 = []
        for i in range(n):
            heappush(h, [a[i]+b[0], i, 0])
        for _ in range(n):
            num, i0, j0 = heappop(h)
            a1.append(num)
            if j0 + 1 < n:
                heappush(h, [a[i0]+b[j0+1], i0, j0+1])

        a = a1

    # print("".join(sorted(a)))
    print(*a)