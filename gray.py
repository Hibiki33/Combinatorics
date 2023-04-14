n = 4


def bit_xor(num):
	res = 0

	while num != 0:
		res = res ^ (num & 1)
		num = num >> 1

	return True if res == 1 else False


def above_bit_xor(nums, i):
	res = 0

	while i < n:
		res = res ^ nums[i]
		i += 1

	return res


def gray2dictionary(gray):
	res = [0] * n

	for i in range(n):
		res[i] = above_bit_xor(gray, i)

	return res[::-1]


def sequence2gray(num):
	res = []

	for i in range(n):
		res.append(num & 1)
		num = num >> 1

	return res[::-1]


def print_sequence(sequence):
	# print gray
	nums_gray = sequence2gray(sequence)
	for i in range(n):
		print(nums_gray[i], end='')
	print(' ', end='')

	# print dictionary
	nums_dict = gray2dictionary(nums_gray[::-1])
	for i in range(n):
		print(nums_dict[i], end='')
	print()


sequence = 0
print_sequence(sequence)

while True:
	if bit_xor(sequence):
		i = 0
		while (sequence >> i) & 1 == 0: 
			i += 1
		sequence = sequence ^ (1 << (i + 1))		
	else:
		sequence = sequence ^ 1

	print_sequence(sequence)

	if sequence == 2**(n - 1):
		break
