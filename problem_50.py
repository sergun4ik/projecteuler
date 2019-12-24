''' Solves problem #50 on https://projecteuler.net
Sergey Lisitsin. December 2019'''


def findprimes(count):
    ''' This function returns first count
    number of primes'''
    primes = [2,3,5,7]
    start = 9
    for x in range(start, count):
        isprime = True
        for p in primes:
            if x % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(x)
    return primes

primes = findprimes(10000)

