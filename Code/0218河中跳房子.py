def check(x: int) -> bool:
    cnt = 0
    tmp = 0
    for i in a:
        tmp += i
        if tmp < x:
            cnt += 1
        else:
            tmp = 0
    # print(f"{x} {cnt <= m}")
    return cnt <= m
    pass

if __name__ == '__main__':
    l, n, m = map(int, input().split())
    tmp = [0]
    for i in range(n):
        tmp.append(int(input()))
    tmp.append(l)
    a = [tmp[i+1] - tmp[i] for i in range(n + 1)]
    left, right = 1, l
    ans = 0
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid
    
    print(ans)



# #include <iostream>
# using namespace std;
# int l, m, n, ans;
# int a[50005];
# int max(int a, int b)
# {
#     return a > b ? a : b;
# }
# int check(int x)
# {
#     int now = 0, cnt = 0;
#     for (int i = 1; i <= n + 1; i++)
#     {
#         if (a[i] - a[now] < x)
#             cnt++;
#         else
#             now = i;
#     }
#     return cnt <= m;
# }

# int main()
# {
#     cin >> l >> n >> m;
#     for (int i = 1; i <= n; i++)
#         cin >> a[i];
#     a[n + 1] = l;
#     int left = 0, right = l;
#     while (left < right)
#     {
#         int mid = (left + right) / 2;
#         if (check(mid))
#         {
#             ans = max(ans, mid);
#             left = mid + 1;
#         }
#         else
#             right = mid;
#     }
#     cout << ans << endl;
#     return 0;
# }