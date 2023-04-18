'''
Generate Combination-Number C(n, m)

Modular Multiplicative Inverse
if (a and p are coprime integers) and ((a * b) % p == 1):
    b is named to be the Inverse of (a % p)
then let c become the Inverse of (b % p):
    (a / b) % p = (a / b) * 1 % p
                = (a / b) * (b * c % p) % p
                = a * c % p
                = (a % p) * (c % p) % p

Fermat's Little Theorem
if (p is prime number) and ((a % p) != 0):
    (a**(p - 1)) % p == 1
    a**(p - 1) == (a**(p - 2)) * a
then:
    (a**(p - 2)) is the Inverse of a

assuming that p is a large prime number,
now we want to figure out (C(n, m) % p):
    (as equivalence operation of mod can't apply to division)
    C(n, m) = (n! / (m! * (n - m)!)) % p
            = ((n! % p) * (((m!)**(p - 2)) % p) * ((((n - m)!)**(p - 2)) % p)) % p
'''

import math

n, m = map(int, input().split())
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
