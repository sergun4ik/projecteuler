'''
Project Euler Problem 138
'''
from numpy import matrix,matmul


a = matrix([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
b = matrix([[1,2,2],[2,1,2],[2,2,3]])
c = matrix([[-1,2,2],[-2,1,2],[-2,2,3]])

origin = [3, 4, 5]

undone = []

def hatch(l):
  undone.append((matmul(a,l)).tolist())
  undone.append((matmul(b,l)).tolist())
  undone.append((matmul(c,l)).tolist())

hatch(origin)



counter = 0
sums = 0

while counter < 12:
    undone[0][0].sort()
    diff = undone[0][0][0]*2-undone[0][0][1]
    if abs(diff) == 1:
        counter += 1
        sums += undone[0][0][2]
        print(counter, undone[0][0][2], sums)
    hatch(undone[0][0])
    undone.pop(0)

print(sums)
