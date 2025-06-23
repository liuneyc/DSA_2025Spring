class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        a = [[1] * m for _ in range(n)]
        tmp = 1
        for i in range(n):
            for j in range(m):
                a[i][j] = tmp
                tmp = tmp * grid[i][j] % 12345
        tmp = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                a[i][j] = a[i][j] * tmp % 12345
                tmp = tmp * grid[i][j] % 12345
        
        return a