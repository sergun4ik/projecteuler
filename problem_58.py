''' Solves problem # 58 on https://projecteuler.net
Sergey Lisitsin. Jan 2020
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
	return candidates


def isprime(num):
    if num == 1:
        return False
    for x in range(2,(num//2)):
        if num%x == 0:
            return False
    return True


def countprimes(list):
    counter = 0
    for x in list:
        if isprime(x):
            counter +=1
    return counter


for x in range(7,2000,2):
    m = matrix(x)
    print (len(m))
    if countprimes(m)/len(m) < 0.1:
        print(x)
        break


def rotate(matrix):
  result = []
  for x in range((len(matrix[0]))-1,-1,-1):
    subresult = []
    for y in matrix:
      subresult.append(y[x])
    result.append(subresult)
  return result

def expand_matrix(matrix):
    width = len(matrix)
    height = len(matrix[0])


diagonals = []
step = 2
allnumbers = 2
while len(diagonals) / allnumbers > 0.1:



side = x*x
step = 1



