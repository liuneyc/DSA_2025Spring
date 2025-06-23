import bisect
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        return bisect.bisect_left(nums, target)
            
            
a = Solution()
print(a.searchInsert([1, 3], 0))