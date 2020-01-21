''' Solves problem # 43 on https://projecteuler.net
Sergey Lisitsin. July 2019
'''

from itertools import permutations

def check_property(num):
    primes = [2,3,5,7,11,13,17]
    #line = str(num)
    slices = []
    for x in range(1,8):
        slices.append(''.join(num[x:x+3]))
    for x in slices:
    for x,y in zip(slices,primes):
        if int(x)%y != 0:
            return False
    return True

seed = '0123456789'
base = list(permutations(seed))

counter = 0
for x in base:
    if check_property(x):
        counter+=int(''.join(x))
print(counter)

