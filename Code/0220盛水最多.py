class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height) - 1
        l, r, ans = 0, n, 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans