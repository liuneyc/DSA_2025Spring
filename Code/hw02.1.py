class matrix:
    def __init__(self, a):
        self.a = a          #matrix
        self.x = len(a)     #行
        self.y = len(a[0])  #列

    def multiplication(self, b):
        '''乘法'''
        if self.y != b.x:
            return -1
        ans = [[0] * b.y for _ in range(self.x)]
        for i in range(self.x):
            for j in range(b.y):
                for k in range(self.y):
                    ans[i][j] += self.a[i][k] * b.a[k][j]
        return matrix(ans)
    
    def add(self, b):
        '''加法'''
        if self.x != b.x or self.y != b.y:
            return -1
        ans = [[0] * self.y for _ in range(self.x)]
        for i in range(self.x):
            for j in range(self.y):
                ans[i][j] = self.a[i][j] + b.a[i][j]
        return matrix(ans)
    
    def print_matrix(self):
        '''打印矩阵'''
        for i in self.a:
            print(*i)

if __name__ == "__main__":
    x1, y1 = map(int, input().split())
    m1 = matrix([list(map(int, input().split())) for _ in range(x1)])

    x2, y2 = map(int, input().split())
    m2 = matrix([list(map(int, input().split())) for _ in range(x2)])

    x3, y3 = map(int, input().split())
    m3 = matrix([list(map(int, input().split())) for _ in range(x3)])

    ans = m1.multiplication(m2)
    if ans == -1:
        print("Error!")
        exit()
        
    ans = ans.add(m3)
    if ans == -1:
        print("Error!")
        exit()
    ans.print_matrix()