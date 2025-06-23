class heap:
    def __init__(self):
        self.a = []

    def swap(self, a, b):
        self.a[a], self.a[b] = self.a[b], self.a[a]

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    
    def size(self):
        return len(self.a)
    
    def fa(self, i):
        return (i - 1) // 2
    
    def up(self, i):
        if i == 0: return
        if self.a[self.fa(i)] > self.a[i]:
            self.swap(i, self.fa(i))
            self.up(self.fa(i))
    
    def down(self, i):
        l, r = self.left(i), self.right(i)
        if l >= self.size(): return
        if r >= self.size():
            if self.a[l] < self.a[i]:
                self.swap(i, l)
                self.down(l)
            return
        if self.a[i] <= self.a[r] and self.a[i] <= self.a[l]: return
        elif self.a[l] < self.a[r]:
            self.swap(i, l)
            self.down(l)
        else:
            self.swap(i, r)
            self.down(r)

    def insert(self, num):
        if self.size() == 0:
            self.a.append(num)
            return
        self.a.append(num)
        self.up(self.size()-1)
    
    def pop(self):
        ans = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()
        self.down(0)
        return ans

h = heap()
for _ in range(int(input())):
    l = list(input().split())
    if len(l) == 1: print(h.pop())
    else: h.insert(int(l[1]))