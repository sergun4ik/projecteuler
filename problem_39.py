''' Solves problem #39 on https://projecteuler.net
Sergey Lisitsin. May 2019'''

from math import pow

squares = [x**2 for x in range(1,1000)]

results = {}
for x in range(1,1001):
    results[x]=0
for x in squares:
    for y in squares:
        if x+y in squares and (pow(x,1/2) + pow(y,1/2) + pow(x+y,1/2) < 1000):
            name = (pow(x,1/2) + pow(y,1/2) + pow(x+y,1/2))
            results[name] += 1

champ = 0

for x in results:
    if results[x] > champ:
        champ = x
        print("{} {}".format(x,results[x]))

print (champ)


