class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        used = [[0] * n for _ in range(m)]
        wl = len(word)
        ans = 0

        def check(x, y, l):
            if 0 <= x < m and 0 <= y < n:
                if board[x][y] == word[l] and used[x][y] == 0:
                    return 1
            return 0
        
        def dfs(x, y, l):
            nonlocal ans
            # print(x, y, l, ans)
            if l == wl-1:
                ans = 1
                return
            if board[x][y] != word[l]:
                return
            for i in range(4):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if check(x1, y1, l+1):
                    used[x1][y1] = 1
                    dfs(x1, y1, l+1)
                    used[x1][y1] = 0
        
        for i in range(m):
            for j in range(n):
                if ans == 1:return True
                if board[i][j] == word[0]:
                    used[i][j] = 1
                    dfs(i, j, 0)
                    used[i][j] = 0
        
        return False if ans == 0 else True
    


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# a = Solution()
# print(a.exist(board, word))