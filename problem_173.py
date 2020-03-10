''' Solves problem # 173 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

def hole_cover(side, limit):
    laminae = 0
    tiles =  (side + 2) * 2 + side * 2
    while tiles <= limit:
        laminae += 1
        tiles = tiles + (side + 2) * 2 + side * 2
    return laminae

counter = set()

lim = 1000000
for x in range(1,lim+1):
    a = hole_cover(x,lim)
    counter.add(a)

print(sum(list((counter))))



