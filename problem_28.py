''' Solves problem # 28 on https://projecteuler.net
Sergey Lisitsin. May 2019
'''

def matrix(side):
	list = side*side
	decrement = side-1
	candidates = []
	while list > 1:
		for x in range(4):
			candidates.append(list)
			list = list - decrement
		decrement = decrement - 2
	candidates.append(1)
	return sum(candidates)

print(matrix(1001))
