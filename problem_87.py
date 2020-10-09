''' Solves problem # 87 on https://projecteuler.net
Sergey Lisitsin. Jan 2020
'''

def findprimes(count):
    ''' This function returns first count
    number of primes'''
    primes = [2,3,5,7]
    start = 9
    for x in range(start, count,2):
        isprime = True
        for p in primes:
            if x % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(x)
    return primes

primes = findprimes(10000)
sprimes = [x for x in primes if x**2 < 50000000]
tprimes = [x for x in primes if x**3 < 50000000]
fprimes = [x for x in primes if x**4 < 50000000]


resultnumbers = set()
for x in sprimes:
    for y in sprimes:
        for z in fprimes:
            if x**2+y**3+z**4 < 50000000:
                resultnumbers.add(x**2+y**3+z**4)

print(len(resultnumbers))