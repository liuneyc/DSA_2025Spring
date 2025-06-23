n = 0; a = []; b = []
ans = 0

def ms(l, r):
    global ans
    if l == r: return
    m = (l + r) // 2
    ms(l, m)
    ms(m+1, r)
    i = l; j = m+1; cnt = l
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[cnt] = a[j]
            cnt += 1
            j += 1
            ans += m - i + 1
        else:
            b[cnt] = a[i]
            cnt += 1
            i += 1
    while i <= m:
        b[cnt] = a[i]
        i += 1
        cnt += 1
    
    while j <= r:
        b[cnt] = a[j]
        j += 1
        cnt += 1
    for i in range(l, r+1):a[i] = b[i]
    # print(l, r, ans)
    pass


if __name__ == '__main__':
    n = int(input())
    a = [int(input()) for _ in range(n)]
    b = [0] * n
    ms(0, n-1)
    # print(a)
    print(ans)