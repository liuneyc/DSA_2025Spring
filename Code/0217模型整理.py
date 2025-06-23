def siz(s: str) -> int:
    if s[-1] == "B":
        return float(s[:-1]) * 1000
    else:
        return float(s[:-1])

if __name__ == "__main__":
    n = int(input())
    a = {}
    for _ in range(n):
        name, size = input().split(sep="-")
        if name in a.keys():
            a[name].append(size)
        else:
            a[name] = [size]

    for i in a.values():
        i.sort(key=siz)

    ans = {i : a[i] for i in sorted(a)}
    for k, v in ans.items():
        print(k, end=": ")
        b = ", ".join(v)
        print(b)
        