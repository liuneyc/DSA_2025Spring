from collections import deque, defaultdict

class Solution:
    def minMoves(self, matrix: list[str]) -> int:
        if matrix[-1][-1] == "#": return -1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
        n = len(matrix)
        m = len(matrix[0])
        doors = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] in letters:
                    doors[matrix[i][j]].append((i, j))
        
        q = deque([])
        q.append((0, 0))

        step = [[1e9]*m for _ in range(n)]
        step[0][0] = 0
        while q:
            x0, y0 = q.popleft()
            if x0 == n-1 and y0 == m-1: return step[x0][y0]
            if matrix[x0][y0] in doors:
                tmp = doors[matrix[x0][y0]]
                for x1, y1 in tmp:
                    if (x1 != x0 or y1 != y0) and step[x1][y1] > step[x0][y0]:
                        step[x1][y1] = step[x0][y0]
                        q.appendleft((x1, y1))
                del doors[matrix[x1][y1]]
            for i in range(4):
                x1, y1 = x0+dx[i], y0+dy[i]
                if 0 <= x1 < n and 0 <= y1 < m and matrix[x1][y1] != "#" and step[x1][y1] > step[x0][y0] + 1:
                    step[x1][y1] = step[x0][y0] + 1
                    q.append((x1, y1))
        
        return -1
