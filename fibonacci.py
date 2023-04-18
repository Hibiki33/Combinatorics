'''
Quickly generate fibonacci number of n
'''

import numpy as np

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    res = quick_pow(n - 2)
    return res[0,0] + res[1,0]

def quick_pow(n):
    a = np.mat([[1, 1], [1, 0]], dtype=np.uint64)
    res = np.mat(np.eye(2, 2, dtype=np.uint64))

    while n != 0:
        if (n & 1) == 1:
            res = np.dot(res, a)
        a = np.dot(a, a)
        n >>= 1

    return res

n = int(input())
print(fibonacci(n))
