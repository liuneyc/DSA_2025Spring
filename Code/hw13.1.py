import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]

l = [0.5] * m
for t in num_list:
    d = t % m
    cnt = 1
    while 1:
        if cnt % 2 == 0: tmp = d + (cnt//2)**2
        else: tmp = d - (cnt//2)**2
        tmp = tmp % m
        if l[tmp] == 0.5 or l[tmp] == t:
            l[tmp] = t
            print(f"{tmp} ", end="")
            break
        cnt += 1

