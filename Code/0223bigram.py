class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        t = text.split()
        ans = []
        for i in range(len(t) - 2):
            if t[i] == first and t[i+1] == second:
                ans.append(t[i+2])
        return ans
        pass