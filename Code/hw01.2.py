class Solution:

    def minimumSize(self, nums: list[int], maxOperations: int) -> int:

        def check(x: int) -> bool:
            cnt = 0
            for i in nums:
                cnt += (i - 1) // x
            return cnt <= maxOperations
        
        ans = 1000000000
        l, r = 1, 1000000000
        while l < r:
            m = (l + r) // 2
            if check(m):
                ans = min(ans, m)
                r = m
            else:
                l = m + 1
        return ans
