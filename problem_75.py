''' Solves problem # 75 on https://projecteuler.net
Sergey Lisitsin. Feb 2020
'''

from math import sqrt

# squares = []
# # for x in range(1,750000):
# #     squares.append(x**2)
# #
# # triangles = []
# # for x in squares:
# #     for y in squares:
# #         if x + y > 1500000:
# #             break
# #         if x+y in squares:
# #             triangles.append((x,y,sqrt(x**2+y**2)))
# #
# #
# # len(triangles)

def findwholehyp(n1,n2):
    res = sqrt(n1**2+n2**2)
    #print(res)
    if res.is_integer():
        return res
    else:
        return False

def find_common(n1,n2):


x = 1
triangles = [0,0,0]
while triangles[-1]+triangles[-2]+triangles[-3] < 1500000:
    triangles.append(x*3+x*4+x*5)
    triangles.append(x*5+x*12+x*13)
    triangles.append(x*8+x*15+x*17)
    x+=1

print(len(triangles))
counter = 0
for x in triangles:
    if triangles.count(x)==1:
        counter+=1
print(counter)