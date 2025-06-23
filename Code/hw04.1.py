class Solution(object):
    def singleNumber(self, nums):
        ans = nums.pop()
        for i in nums:
            ans ^= i
        return ans