'''
Generate a n * n magic square
'''

n = eval(input())

t = [[None] * n for _ in range(n)]

t[0][int(n / 2)] = 1
row = 0
col = int(n / 2)
i = 2

while i <= n * n:
    if row == 0 and col != n - 1:
        t[n - 1][col + 1] = i
        row = n - 1
        col = col + 1
    elif row != 0 and col == n - 1:
        t[row -1][0] = i
        row = row - 1
        col = 0
    elif row == 0 and col == n - 1:
        t[row + 1][col] = i
        row = row + 1
        col = col
    elif row != 0 and col != n - 1:
        if t[row - 1][col + 1] == None:
            t[row - 1][col + 1] = i
            row = row - 1
            col = col + 1
        else:
            t[(row + 1) % n][col] = i
            row = (row + 1) % n
            col = col
    i += 1

for x in range(n):
    for y in range(n):
        print(t[x][y], end=' ')
    print()