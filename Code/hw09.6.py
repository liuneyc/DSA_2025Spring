from heapq import *
from collections import defaultdict, deque
class node:
    def __init__(self, val = None, left = None, right = None, char = None, fa = None):
        self.val = val
        self.left = left
        self.right = right
        self.char = char
        self.fa = fa

    def __lt__(self, other):
        if self.val != other.val:
            return self.val < other.val
        return self.char < other.char



h = []
heapify(h)
way = defaultdict(str)
def ad(root, s):
    if root.left == None and root.right == None: way[root.char] = s + way[root.char]
    else:
        ad(root.left, s)
        ad(root.right, s)
for _ in range(int(input())):
    tmp = input().split()
    heappush(h, node(val=int(tmp[1]),char=tmp[0]))
while len(h) > 1:
    n1, n2 = heappop(h), heappop(h)
    # print(n1.val, n2.val)
    new = node(val=n1.val+n2.val)
    new.char = n1.char
    new.left = n1
    new.right = n2
    ad(n1, "0")
    ad(n2, "1")
    heappush(h, new)
    # print(new.val, way)
root = h[0]
def transfer(s: str):
    ans = ""
    for i in s: ans += way[i]
    return ans

def restore(s: str):
    ans = ""
    s = list(s)
    tmp = root
    p = 0
    while p < len(s):
        if s[p] == '0': tmp = tmp.left
        if s[p] == '1': tmp = tmp.right
        if tmp.left == None and tmp.right == None:
            ans += tmp.char
            tmp = root
        p += 1
    return ans

while 1:
    try:
        t = input()
        if t[0] in "01":
            print(restore(t))
        else: print(transfer(t))
    except EOFError:
        break