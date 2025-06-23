class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        m, ans = prices[0], 0
        for i in range(1, n):
            m = min(m, prices[i])
            ans = max(ans, prices[i] - m)
        return ans
