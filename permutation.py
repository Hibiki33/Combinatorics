'''
Generate a recyclable permutation
'''

n = 8

perm = [[i, -1] for i in range(n)]

for i in range(n):
	print(perm[i][0] + 1, end=' ')
print()

while True:
	move = -1
	for i in range(n):
		nearby = i + perm[i][1]
		if nearby in range(0, n) and perm[nearby][0] < perm[i][0]:
			if move == -1:
				move = i
			else:
				move = i if perm[i][0] > perm[move][0] else move

	if move == -1:
		break
	else:
		cur = perm[move][0]
		temp = perm[move + perm[move][1]]
		perm[move + perm[move][1]] = perm[move]
		perm[move] = temp
		for i in range(n):
			print(perm[i][0] + 1, end=' ')
			perm[i][1] = (0 - perm[i][1]) if perm[i][0] > cur else perm[i][1]
		print()
