class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        ans = [-1]
        arr.reverse()
        for i in arr[:-1]:
            ans.append(max(ans[-1], i))
        ans.reverse()
        return ans