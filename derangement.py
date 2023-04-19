'''
Figure the n'th derangement number
when n beq 1:
D(n) = n!(1 - 1/(1!) + 1/(2!) - 1/(3!) + ... + (-1)**n/(n!))
thus:
D(n) = (n - 1)(D(n - 2) + D(n - 1))
D(n) = nD(n - 1) + (-1)**n 
'''

n = int(input())
d = 1

for i in range(1, n + 1):
    if i & 1 == 1:
        d = i * d - 1
    else:
        d = i * d + 1

print(d)
