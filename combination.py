import math

n,m = map(int,input().split())
p = 100000007
def power(x, y):     #求x的y次方
    p = 100000007
    res = 1
    while y:
        if y % 2 != 0:
            res *= (x % p)
        y >>= 1
        x *= (x % p)
    return res
a = (math.factorial(n))%p
b = (power(math.factorial(m),(p-2))) % p
c = (power(math.factorial(n-m),(p-2))) % p
print(a * b * c % p)

