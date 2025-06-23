t = input()
lt = len(t)
num = "0123456789"
def f(l: int, r: int) -> str:
    # print(l, r, t[l:r+1])
    if l > r:
        return ""
    if l == r:
        return t[l]
    if t[l] in num:
        for i in range(l+1, r+1):
            if t[i] not in num:
                return int(t[l:i]) * f(i, r)
    if t[l] == "[":
        cnt = 1
        for i in range(l+1, r+1):
            if t[i] == "[":
                cnt += 1
            elif t[i] == "]":
                cnt -= 1
            if cnt == 0:
                return f(l+1, i-1) + f(i+1, r)
    return t[l] + f(l+1, r)

print(f(0, lt-1))