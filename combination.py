import math

n, m = map(int,input().split())
p = 100000007

def power(x, y):  
    res = 1
    while y:
        if y % 2 != 0:
            res *= (x % p)
        y >>= 1
        x *= (x % p)
    return res

if n >= m:
    a = (math.factorial(n)) % p
    b = (power(math.factorial(m), (p - 2))) % p
    c = (power(math.factorial(n - m), (p - 2))) % p
    print(a * b * c % p)
else:
    print("0")

