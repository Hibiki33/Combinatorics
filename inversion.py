import random
n = 8

# inversion = []
# for i in range(1, n + 1):
# 	 inversion.append(random.randint(0, n - i))

inversion = [1, 3, 5, 4, 3, 2, 1, 0]

print(inversion)

permutaion = [0 for i in range(n)]
for i in range(n):
	move = inversion[i] + 1
	for j in range(n):
		if permutaion[j] == 0:
			move -= 1
		if move == 0:
			permutaion[j] = i + 1
			break

print(permutaion)
