from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans = []
        t = [0] * n
        for i in range(1, n):
            t[i] = t[i-1]
            if nums[i] - nums[i-1] > maxDiff: t[i] += 1
        for x, y in queries:
            if t[x] == t[y]: ans.append(True)
            else: ans.append(False)
        return ans