from collections import deque

a, b, c = map(int, input().split())
q = deque([])
q.append([0, 0, []])
vis = {}
vis[(0, 0)] = 1
ans = []
while q:
    # print(q)
    a0, b0, way = q.popleft()

    if a0 == c or b0 == c:
        ans = way
        break

    if 0 <= a0 < a and (a, b0) not in vis:
        way1 = way + ["FILL(1)"]
        vis[(a, b0)] = 1
        q.append([a, b0, way1])

    if 0 <= b0 < b and (a0, b) not in vis:
        way1 = way + ["FILL(2)"]
        vis[(a0, b)] = 1
        q.append([a0, b, way1])

    if 0 < a0 <= a and (0, b0) not in vis:
        way1 = way + ["DROP(1)"]
        vis[(0, b0)] = 1
        q.append([0, b0, way1])

    if 0 < b0 <= b and (a0, 0) not in vis:
        way1 = way + ["DROP(2)"]
        vis[(a0, 0)] = 1
        q.append([a0, 0, way1])
    
    if a0 < a and b0 > 0:
        d = min(a - a0, b0)
        a1 = a0 + d
        b1 = b0 - d
        if (a1, b1) not in vis:
            way1 = way + ["POUR(2,1)"]
            vis[(a1, b1)] = 1
            q.append([a1, b1, way1])

    if b0 < b and a0 > 0:
        d = min(b - b0, a0)
        b1 = b0 + d
        a1 = a0 - d
        if (a1, b1) not in vis:
            way1 = way + ["POUR(1,2)"]
            vis[(a1, b1)] = 1
            q.append([a1, b1, way1])

if ans != []:
    print(len(ans))
    for i in ans:
        print(i)
else:
    print("impossible")
