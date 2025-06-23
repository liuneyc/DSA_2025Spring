while 1:
    try:
        a = input()
        l = len(a)
        cnt = 0
        for i in range(l):
            if a[i] == '@':cnt += 1
        if cnt != 1:
            print("NO")
            continue
        if a[0] in ["@", "."] or a[-1] in ["@", "."]:
            print("NO")
            continue
        if a.find("@.") != -1 or a.find(".@") != -1:
            print("NO")
            continue
        cnt = 0
        if a.find("@") > a.find(".",a.find("@")) or a.find(".",a.find("@")) == -1:
            print("NO")
            continue
        print("YES")
    except:
        break