# for _ in range(int(input())):
#     m, n = map(int, input().split())
#     a = [sorted(list(map(int, input().split()))) for _ in range(m)]
#     # print(a)
#     ans = [sum([a[i][0] for i in range(m)])]
#     while len(ans) < n:
#         minn, minnp = a[0][1] - a[0][0], 0
#         for i in range(m):
#             if len(a[i]) == 1:continue
#             if a[i][1] - a[i][0] < minn:
#                 minnp = i
#                 minn = a[i][1] - a[i][0]
#         ans.append(ans[-1] + minn)
#         a[minnp].pop(0)
#         # print(minnp, ans)
#     print(*ans)
    

# for _ in range(int(input())):
#     m, n = map(int, input().split())
#     a = [sorted(list(map(int, input().split()))) for _ in range(m)]
#     ans = [sum(row[0] for row in a)]
#     while len(ans) < n:
#         minn = float('inf')
#         minnp = -1
#         for i in range(m):
#             if len(a[i]) >= 2:
#                 diff = a[i][1] - a[i][0]
#                 if diff < minn:
#                     minn = diff
#                     minnp = i
#         if minnp == -1:
#             break  # 无法继续生成更多元素，可能题目保证n合法
#         ans.append(ans[-1] + minn)
#         a[minnp].pop(0)
#     print(*ans)

# import heapq

# t = int(input())
# for _ in range(t):
#     m, n = map(int, input().split())
#     seq1 = sorted(map(int, input().split()))
#     for _ in range(m - 1):
#         seq2 = sorted(map(int, input().split()))

#         # 使用最小堆存储可能的最小和以及对应的索引
#         min_heap = [(seq1[i] + seq2[0], i, 0) for i in range(n)]
#         heapq.heapify(min_heap)
#         result = []
#         for _ in range(n):
#             current_sum, i, j = heapq.heappop(min_heap)
#             result.append(current_sum)
#             if j + 1 < len(seq2):
#                 heapq.heappush(min_heap, (seq1[i] + seq2[j + 1], i, j + 1))
#         seq1 = result
#     print(*seq1)





from heapq import *

for _ in range(int(input())):
    m, n = map(int, input().split())
    a = sorted(map(int, input().split()))
    for _ in range(m-1):
        b = sorted(map(int, input().split()))
        q = [[a[i] + b[0], i, 0] for i in range(n)]
        heapify(q)
        # print(q)
        ans = []
        for i in range(n):
            tmp, aa, bb = heappop(q)
            ans.append(tmp)
            if bb < n - 1:
                heappush(q, [a[aa] + b[bb+1], aa, bb+1])
        a = ans
    print(*a)