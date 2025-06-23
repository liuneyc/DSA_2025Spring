from heapq import *
class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        n = len(nums2)
        a = [[nums1[i], nums2[i], i] for i in range(n)]
        a.sort()
        ans = [0] * n
        h = []
        # print(a)
        i = 0
        s = 0
        while i < n:
            # print(h)
            p = i
            ans[a[i][2]] = s
            t = a[i][0]
            while i < n and a[i][0] == t:
                ans[a[i][2]] = s
                i += 1
            for j in range(p, i):
                y = a[j][1]
                s += y
                heappush(h, y)
                if len(h) > k:
                    s -= heappop(h)

        return ans

nums1 =[18,11,24,9,10,11,7,29,16]
nums2 =[28,26,27,4,2,19,23,1,2]
k =1
# nums1 =[2,2,2,2]
# nums2 =[3,1,2,3]
# k =1


print(Solution.findMaxSum(0, nums1, nums2, k))