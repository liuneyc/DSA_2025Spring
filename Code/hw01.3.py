n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

def check(x: int) -> bool:
    cnt, tmp = 1, 0
    for i in range(n):
        if a[i] > x:
            return 0
        tmp += a[i]
        if tmp > x:
            tmp = a[i]
            cnt += 1
    return cnt <= m

l, r, ans = 1, 2000000000, 2000000000
while l < r:
    mid = (l + r) // 2
    if check(mid):
        ans = min(ans, mid)
        r = mid
    else:
        l = mid + 1

print(ans)




# #include <iostream>
# using namespace std;
# int min(int a, int b)
# {
#     return a < b ? a : b;
# }

# int n, m, a[100005];
# int ans = 200000;

# int check(int x)
# {
#     int cnt = 0, tmp = 0;
#     for (int i = 1; i <= n; i++)
#     {
#         if (a[i] > x)
#             return 0;
#         tmp += a[i];
#         if (tmp > x)
#         {
#             tmp = a[i];
#             cnt++;
#         }
#     }
#     return cnt++ <= m;
# }

# int main()
# {
#     cin >> n >> m;
#     for (int i = 1; i <= n; i++)
#         cin >> a[i];
#     int l = 0, r = 200000;
#     while (l < r)
#     {
#         int m = (l + r) / 2;
#         if (check(m))
#         {
#             ans = min(ans, m);
#             r = m;
#         }
#         else
#             l = m + 1;
#     }
#     cout << ans << endl;
#     return 0;
# }