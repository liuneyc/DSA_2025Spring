

## Cheatsheet

刘祚宏

这个Cheatsheet是我带到考场上的，其中包含了一些基本的bfs, dfs, 迪杰斯特拉，并查集，欧拉筛，哈夫曼，KMP等算法。

其实在考试过程中一个都没有用到，只是起到了心理安慰的作用。

**# OOP：**

 | `__eq__(self, other)` | `==` | 判断相等 |

 | `__ne__(self, other)` | `!=` | 判断不相等 |

 | `__lt__(self, other)` | `<` | 判断是否小于 |

 | `__le__(self, other)` | `<=` | 判断是否小于等于 |

 | `__gt__(self, other)` | `>` | 判断是否大于 |

 | `__ge__(self, other)` | `>=` | 判断是否大于等于 |

**Lake Counting bfs，dfs**

```python
# bfs
from collections import deque
n, m = map(int, input().split())
a = []
cnt = 0
for _ in range(n):
    a.append(list(input()))
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def check(x, y):
    return 0 <= x < n and 0 <= y < m and a[x][y] == "W"

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    while q:
        x0, y0 = q.popleft()
        for i in range(8):
            x1 = x0 + dx[i]
            y1 = y0 + dy[i]
            if check(x1, y1):
                q.append((x1, y1))
                a[x1][y1] = "."

for i in range(n):
    for j in range(m):
        if a[i][j] == "W":
            cnt += 1
            bfs(i,j)
print(cnt)

# dfs
import sys
sys.setrecursionlimit(20000)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
n, m = map(int, input().split())
a = []
cnt = 0
for _ in range(n):
    a.append(list(input()))

def check(x, y):
    return 0 <= x < n and 0 <= y < m and a[x][y] == "W"

def dfs(x, y):
    for i in range(8):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if check(x1, y1):
            a[x1][y1] = "."
            dfs(x1, y1)

for i in range(n):
    for j in range(m):
        if a[i][j] == "W":
            cnt += 1
            dfs(i, j)
print(cnt)
```

**bfs**

```python
from collections import defaultdict, deque
g = defaultdict(list)

n = int(input())
for _ in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

p = set(map(int, input().split()))
vis = set()
q = deque([])
q.append(0)
while q:
    x0 = q.popleft()
    vis.add(x0)
    for x1 in g[x0]:
        if x1 in p: continue
        if x1 in vis: continue
        q.append(x1)

print(len(vis))
```

**走山路 迪杰斯特拉**

```python
from heapq import *

m, n, p = map(int, input().split())

a = [[0] * n for _ in range(m)]
step = [[10**9] * n for  _ in range(m)]
vis = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    return 0 <= x < m and 0 <= y < n and a[x][y] != -1

for i in range(m):
    tmp = input().split()
    for j in range(n):
        if tmp[j] == "#":
            a[i][j] = -1
        else:
            a[i][j] = int(tmp[j])

for _ in range(p):
    step = [[10**9] * n for  _ in range(m)]
    flag = 0
    vis = set()
    sx, sy, ex, ey = map(int ,input().split())
    if a[sx][sy] == -1 or a[ex][ey] == -1:
        print("NO")
        continue
    h = [(0, sx, sy)]
    while h:
        s0, x0, y0 = heappop(h)
        if (x0, y0) in vis: continue
        vis.add((x0, y0))
        # print(x0, y0)
        if x0 == ex and y0 == ey:
            print(s0)
            flag = 1
            break
        for i in range(4):
            x1 = x0 + dx[i]
            y1 = y0 + dy[i]
            if check(x1, y1):
                s1 = abs(a[x1][y1] - a[x0][y0]) + s0
                if s1 < step[x1][y1]:
                    step[x1][y1] = s1
                    heappush(h, (s1, x1, y1))
    
    if flag == 0:
        if step[ex][ey] == 10**9: print("NO")
        else: print(step[ex][ey])
```

**并查集**

```python
f = [i for i in range(n)]
def find(x):
    if f[x] == x: return x
    else:
        f[x] = find(f[x])
        return f[x]
      
if find(i) != find(j):
    f[find(i)] = find(j)
```

**欧拉筛**

```python
prime = []
primecnt = 0
isprime = [1]*10001
isprime[1] = 0
for i in range(1, 10001):
    if isprime[i] == 1:
        primecnt += 1
        prime.append(i)
    for j in range(primecnt):
        if prime[j]*i > 10000: break
        isprime[prime[j]*i] = 0
        if i%prime[j] == 0: break
```

**迪杰斯特拉**

```python
from collections import deque, defaultdict
from heapq import *

g = defaultdict(dict)
n, m, s = map(int, input().split())

for _ in range(m):
    u, v, w = map(int, input().split())
    if v in g[u]: g[u][v] = min(w, g[u][v])
    else: g[u][v] = w

mindir = [10**9] * (n + 1)
mindir[s] = 0

h = [[0, s]]
vis = set()

while h:
    dir, t0 = heappop(h)
    if t0 in vis: continue
    vis.add(t0)

    for i in g[t0]:
        if mindir[i] > mindir[t0] + g[t0][i]:
            mindir[i] = mindir[t0] + g[t0][i]
            heappush(h, [mindir[i], i])

print(*mindir[1:])
```



**完全二叉树：**

0是根节点

儿子 `2*i+1`, `2*i+2`

父亲 `(i-1)//2`



2i, 2i+1

i/2



计算：`eval()`



**迪杰斯特拉2**

```python
from collections import defaultdict
from heapq import *
n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    x, y, d = map(int, input().split())
    g[x].append((y, d))
vis = set()
d = [float('inf')] * (n + 1)
h = [(0, 1)]
while h:
    dis, p = heappop(h)
    if p in vis: continue
    vis.add(p)
    d[p] = min(d[p], dis)
    for p1, d1 in g[p]:
        if d[p1] > dis + d1:
            heappush(h, (dis + d1, p1))
            d[p1] = min(d[p1], dis+d1)


print(d[n])
```

```python
distance=[float('inf')]*n
distance[s]=0
visied=[False]*n
q=[]
heapq.heappush((0,s))
while q:
    u=heappop(q)
    if visited[u]:
        continue
    visited[u]=True
    for v,w in e[u]:
		if visited[v] and distance[u]+w<distance[v]:
            diatance[v]=distance[u]+w
            heapq.heappush(q,(distance[u]+w,v))
```

Huffman

<img src="https://raw.githubusercontent.com/liuneyc/PICTURES/main/img/20250618002941418.png" alt="image-20250603130545311" style="zoom: 33%;" />



共同祖先 lca

```python
def lowestCommonAncestor(root,p,q):
    if root is None or p is None or q is None:
        return root
    l=lowestCommonAncestor(root.left,p,q)
    r=lowestCommonAncestor(root.right,p,q)
    if l is not None and r is not None:
        return root
    if l is None and r is None:
        return None
    return l if l is not None else r
```

```
heapq
sys setrecursionlimit
bisect insort
collections deque defaultdict

```



![image-20250603154948666](https://raw.githubusercontent.com/liuneyc/PICTURES/main/img/20250618002953004.png)

拓扑排序判断环

```python
from collections import defaultdict, deque

for __ in range(int(input())):
    g = defaultdict(list)
    n, m = map(int, input().split())
    into = [0] * (n+1)
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        into[y] += 1
    
    q = deque([])
    for i in range(1, n+1):
        if into[i] == 0: q.append(i)
    vis = 0
    while q:
        t = q.popleft()
        vis += 1
        for i in g[t]:
            into[i] -= 1
            if into[i] == 0:
                q.append(i)
    if vis == n: print("No")
    else: print("Yes")
```

哈夫曼

```python
from heapq import *
from collections import defaultdict
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
```

KMP

```python
""""
compute_lps 函数用于计算模式字符串的LPS表。LPS表是一个数组，
其中的每个元素表示模式字符串中当前位置之前的子串的最长前缀后缀的长度。
该函数使用了两个指针 length 和 i，从模式字符串的第二个字符开始遍历。
"""
def compute_lps(pattern):
    """
    计算pattern字符串的最长前缀后缀（Longest Proper Prefix which is also Suffix）表
    :param pattern: 模式字符串
    :return: lps表
    """

    m = len(pattern)
    lps = [0] * m  # 初始化lps数组
    length = 0  # 当前最长前后缀长度
    for i in range(1, m):  # 注意i从1开始，lps[0]永远是0
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]  # 回退到上一个有效前后缀长度
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    lps = compute_lps(pattern)
    matches = []

    # 在 text 中查找 pattern
    j = 0  # 模式串指针
    for i in range(n):  # 主串指针
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]  # 模式串回退
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - j + 1)  # 匹配成功
            j = lps[j - 1]  # 查找下一个匹配

    return matches


text = "ABABABABCABABABABCABABABABC"
pattern = "ABABCABAB"
index = kmp_search(text, pattern)
print("pos matched：", index)
# pos matched： [4, 13]

```

重复

```python
def kmp_next(s):
  	# kmp算法计算最长相等前后缀
    next = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j] and j > 0:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next


def main():
    case = 0
    while True:
        n = int(input().strip())
        if n == 0:
            break
        s = input().strip()
        case += 1
        print("Test case #{}".format(case))
        next = kmp_next(s)
        for i in range(2, len(s) + 1):
            k = i - next[i - 1]		# 可能的重复子串的长度
            if (i % k == 0) and i // k > 1:
                print(i, i // k)
        print()


```

f"{ans:.2f}"

