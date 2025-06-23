from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        a = [[1] * n for _ in range(n)]
        for j in range(n):
            for i in range(j):
                a[i][j] = (s[i] == s[j]) and a[i+1][j-1]
        # print(a)
        ans = []
        tmp = []

        def dfs(x):
            if x == n:
                ans.append(tmp[:])
            for i in range(x, n):
                if a[x][i] == 1:
                    tmp.append(s[x:i+1])
                    dfs(i+1)
                    tmp.pop()

        dfs(0)
        return ans
    
