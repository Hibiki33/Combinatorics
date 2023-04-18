'''
Generate a Chain of length n
'''

import copy

n = 5
chains = []
chains.append([[], [1]])

for i in range(2, n + 1):
	next_chains = []

	for chain in chains:
		k = len(chain)

		c1 = copy.deepcopy(chain)
		c2 = copy.deepcopy(chain)

		temp = copy.deepcopy(chain[k - 1])
		temp.append(i)
		c1.append(temp)
		next_chains.append(c1)

		if k != 1:
			for elm in c2:
				elm.append(i)
			c2.pop()
			next_chains.append(c2)

	chains = next_chains

for chain in chains:
	print(chain)
