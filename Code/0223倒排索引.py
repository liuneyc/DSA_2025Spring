a = []
d = {}
n = int(input())
for i in range(n):
    tmp = input().split()
    for j in tmp[1:]:
        if j in d and i+1 not in d[j]:
            d[j].append(i+1)
        if j not in d:
            d[j] = [i+1]

for _ in range(int(input())):
    word = input()
    if word not in d:
        print("NOT FOUND")
    else:
        print(*d[word])