""" Solves problem # 75 on https://projecteuler.net
Sergey Lisitsin. Oct 2020
"""
from numpy import matrix, matmul


a = matrix([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
b = matrix([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
c = matrix([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])

origin = [3, 4, 5]

undone = []
sums = []


def hatch(l):
  if sum(l) in sums:
  sums.append(sum(l))
  undone.append((matmul(a,l)).tolist())
  undone.append((matmul(b,l)).tolist())
  undone.append((matmul(c,l)).tolist())

hatch(origin)
limit = 1500000


sums.sort()
while sum(undone[0][0]) < limit or sum(undone[1][0]) < limit \
        or sum(undone[2][0]) < limit:
    hatch(undone[0][0])
    undone.pop(0)
    hatch(undone[0][0])
    undone.pop(0)
    hatch(undone[0][0])
    undone.pop(0)
    undone.sort(key=lambda x: sum(x[0]))

undone.sort(key=lambda x: sum(x[0]))

sums = [x for x in sums if x <= limit]
sums = [x for x in sums if sums.count(x) == 1]


sums.sort()
results = []

for x in range(2, limit+1,2):
    for y in sums:
        if y > x:
            break
        if x % y == 0:
          results.append(x)


result = [x for x in results if results.count(x) == 1]
result.sort()

print(result)
#print(result[-100:-1:])
print (len(result))

