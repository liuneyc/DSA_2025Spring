class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, 0, -1):
            for j in range(n - i + 1):
                tmp = s[j: j + i]
                if tmp == tmp[::-1]:
                    return tmp
                

a = Solution()

print(a.longestPalindrome("c"))