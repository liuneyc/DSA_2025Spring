n = int(input())
a = list(input())
l = len(a)
b = []

for i in range(l//n):
    if i % 2 == 1:
        b.append(a[i*n+n-1:i*n-1:-1])
    else:
        b.append(a[i*n:i*n+n])
        
for i in range(n):
    for j in range(l//n):
        print(b[j][i], end="")
print()