from math import *

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def out(self):
        print(f"{self.a}/{self.b}")

    def __add__(self, fra2):
        a1 = self.a * fra2.b + self.b * fra2.a
        b1 = self.b * fra2.b
        n = gcd(a1, b1)
        return Fraction(a1//n, b1//n)
    
if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    x = Fraction(a, b)
    y = Fraction(c, d)
    z = x + y
    z.out()