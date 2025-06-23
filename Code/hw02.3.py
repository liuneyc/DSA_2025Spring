def f(x: float) -> float:
    return x**3 - 5*x**2 + 10*x - 80

def d(x: float) -> float:
    return 3*x**2 - 10*x + 10

def l(x):
    return f(x) ** 2
def dl(x):
    return 2*f(x)*d(x)

# x0 = 6
# while 1:
#     k = d(x0)
#     x1 = x0 - f(x0) / d(x0)
#     if abs(x1 - x0) <= 1e-10:
#         print("%.9f" % x1)
#         exit()
#     x0 = x1

dx = 0.00001
x0 = 6
while 1:
    x1 = x0 - dx * dl(x0)
    # print(x1)
    if abs(x1 - x0) <= 0.00000000001:
        print("%.9f" % x1)
        # print()
        exit()
    x0 = x1