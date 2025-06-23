n = int(input())
words = []
all_passage = set()
for i in range(n):
    tmp = list(map(int, input().split()))
    words.append(set(tmp[1:]))
    all_passage = all_passage | words[i]
    
m = int(input())
for _ in range(m):
    tmp = list(map(int, input().split()))
    ans = all_passage
    for i in range(n):
        if tmp[i] == 1:
            ans = ans & words[i]
        elif tmp[i] == -1:
            ans = ans - words[i]
    if not ans:
        print("NOT FOUND")
    else:
        print(*sorted(ans))