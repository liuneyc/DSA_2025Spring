if __name__ == "__main__":
    while 1:
        try:
            a = input()
            n = len(a)
            place = []
            ans = [" "] * n
            for i in range(n):
                if a[i] == "(":
                    place.append(i)
                    ans[i] = "$"
                    pass
                if a[i] == ")":
                    if len(place) == 0:
                        ans[i] = "?"
                    else:
                        ans[place[-1]] = " "
                        place.pop()
                    pass
            print(a)
            print("".join(ans))
        except EOFError:
            break