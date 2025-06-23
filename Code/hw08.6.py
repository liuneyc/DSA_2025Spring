from heapq import *
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        s = []
        re = 0
        for i in range(1, n):
            s.append([nums[i-1]+nums[i], i-1])
            if nums[i-1] > nums[i]: re += 1
        heapify(s)
        used = [1] * n
        cnt = 0
        left = [i-1 for i in range(n)]
        right = [i+1 for i in range(n)]
        right[-1] = -1

        while re > 0 and s:
            tmp, i = heappop(s)
            if right[i] == -1 or used[i] == 0 or used[right[i]] == 0: continue
            if tmp != nums[i] + nums[right[i]]: continue
            # print(re)

            r = right[i]
            if nums[i] > nums[r]: re -= 1
            if left[i] != -1 and used[left[i]] == 1:
                if nums[left[i]] > nums[i] and nums[left[i]] <= tmp: re -= 1
                if nums[left[i]] <= nums[i] and nums[left[i]] > tmp: re += 1

            if right[right[i]] != -1 and used[right[right[i]]] == 1:
                if nums[right[i]] > nums[right[right[i]]] and tmp <= nums[right[right[i]]]:
                    re -= 1
                    pass
                if nums[right[i]] <= nums[right[right[i]]] and tmp > nums[right[right[i]]]:
                    re += 1
            nums[i] = tmp
            used[r] = 0
            cnt += 1

            right[i] = right[r]
            if right[r] != -1: left[right[r]] = i
            if left[i] != -1 and used[left[i]] == 1: heappush(s, [nums[left[i]]+nums[i], left[i]])
            if right[i] != -1 and used[right[i]] == 1: heappush(s, [nums[i]+nums[right[i]], i])
            # print(i, cnt)

        print(cnt)
        return cnt
        
# from heapq import *
# from collections import defaultdict

# class Solution:
#     def minimumPairRemoval(self, nums: list[int]) -> int:
#         n = len(nums)
#         if n <= 1:
#             return 0
        
#         # Initialize data structures
#         left = list(range(-1, n-1))  # left[i] is the previous index of i
#         right = list(range(1, n)) + [-1]  # right[i] is the next index of i
#         used = [1] * n
#         heap = []
#         re = 0  # count of decreasing pairs
        
#         # Precompute initial decreasing pairs and push adjacent sums to heap
#         for i in range(n-1):
#             if nums[i] > nums[i+1]:
#                 re += 1
#             heappush(heap, (nums[i] + nums[i+1], i, i+1))
        
#         cnt = 0
#         while re > 0 and heap:
#             sum_val, i, j = heappop(heap)
#             if not used[i] or not used[j] or right[i] != j:
#                 continue  # Skip invalid pairs
            
#             # Merge i and j into i
#             cnt += 1
#             used[j] = 0
#             new_val = sum_val
#             left_i_prev = left[i]
#             right_j_next = right[j]
            
#             # Update decreasing pairs count for the merged pair
#             if nums[i] > nums[j]:
#                 re -= 1
            
#             # Check left neighbor (left_i_prev and i)
#             if left_i_prev != -1:
#                 if nums[left_i_prev] > nums[i]:
#                     re -= 1
#                 if nums[left_i_prev] > new_val:
#                     re += 1
            
#             # Check right neighbor (j's next and new i)
#             if right_j_next != -1:
#                 if nums[j] > nums[right_j_next]:
#                     re -= 1
#                 if new_val > nums[right_j_next]:
#                     re += 1
            
#             # Update pointers and values
#             nums[i] = new_val
#             right[i] = right_j_next
#             if right_j_next != -1:
#                 left[right_j_next] = i
            
#             # Push new possible pairs to the heap
#             if left_i_prev != -1:
#                 heappush(heap, (nums[left_i_prev] + new_val, left_i_prev, i))
#             if right_j_next != -1:
#                 heappush(heap, (new_val + nums[right_j_next], i, right_j_next))
        
#         return cnt
# from sortedcontainers import SortedList
# from itertools import pairwise
# class Solution:
#     def minimumPairRemoval(self, nums: list[int]) -> int:
#         sl = SortedList()  # (相邻元素和，左边那个数的下标)
#         idx = SortedList(range(len(nums)))  # 剩余下标
#         dec = 0  # 递减的相邻对的个数

#         for i, (x, y) in enumerate(pairwise(nums)):
#             if x > y:
#                 dec += 1
#             sl.add((x + y, i))

#         ans = 0
#         while dec > 0:
#             ans += 1

#             s, i = sl.pop(0)  # 删除相邻元素和最小的一对
#             k = idx.bisect_left(i)

#             # (当前元素，下一个数)
#             nxt = idx[k + 1]
#             if nums[i] > nums[nxt]:  # 旧数据
#                 dec -= 1

#             # (前一个数，当前元素)
#             if k > 0:
#                 pre = idx[k - 1]
#                 if nums[pre] > nums[i]:  # 旧数据
#                     dec -= 1
#                 if nums[pre] > s:  # 新数据
#                     dec += 1
#                 sl.remove((nums[pre] + nums[i], pre))
#                 sl.add((nums[pre] + s, pre))

#             # (下一个数，下下一个数)
#             if k + 2 < len(idx):
#                 nxt2 = idx[k + 2]
#                 if nums[nxt] > nums[nxt2]:  # 旧数据
#                     dec -= 1
#                 if s > nums[nxt2]:  # 新数据（当前元素，下下一个数）
#                     dec += 1
#                 sl.remove((nums[nxt] + nums[nxt2], nxt))
#                 sl.add((s + nums[nxt2], i))

#             nums[i] = s  # 把 nums[nxt] 加到 nums[i] 中
#             idx.remove(nxt)  # 删除 nxt

#         return ans

a = Solution()
print(a.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))