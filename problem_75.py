''' Solves problem # 75 on https://projecteuler.net
Sergey Lisitsin. Feb 2020
'''

from math import sqrt

squares = [x**2 for x in range(750000)]

triangles = []
for x in squares:
    for y in squares:
        if x + y > 1500000:
            break
        if x+y in squares:
            triangles.append((x,y,sqrt(x**2+y**2)))


len(triangles)

def findwholehyp(n1,n2):
    res = sqrt(n1**2+n2**2)
    #print(res)
    if res.is_integer():

        return res
    else:
        return False
