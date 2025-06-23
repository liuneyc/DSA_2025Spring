# while 1:
#     try:
#         a = list(input())
#         n = len(a); flag = 1
#         for i in range(n // 2):
#             if a[i] != a[n - 1 - i]:
#                 print("NO")
#                 flag = 0
#                 break
#         if flag:print("YES")
#     except EOFError:
#         break


while 1:
    try:
        a=input();print('YES'if a==a[::-1]else'NO')
    except:break