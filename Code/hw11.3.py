f = sorted(list(map(float, input().split())), reverse=True)

n = len(f)

def ch(x, b):
    a = b / 1000000000
    return a*x+1.1**(a*x)

def check(b):
    cnt = 0
    for i in range(int(n*0.6)+1):
        if ch(f[i], b) >= 85: cnt += 1
        else: break
    return cnt*5 >= n*3

l, r = 1, 1000000000
ans = 1000000000
while l < r:
    m = (l + r) // 2
    if check(m):
        ans = min(ans, m)
        r = m
    else:
        l = m + 1
print(ans)