''' Solves problem #49 on https://projecteuler.net
Sergey Lisitsin. July 2019'''

def findprimes(count):
    ''' This function returns first count
    number of primes'''
    primes = [2,3,5,7]
    start = 9
    for x in range(start, count, 2):
        isprime = True
        for p in primes:
            if x % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(x)
    return primes

primes = findprimes(10000)
for x in primes:
   # print(x)
    if len(str(x))==4:
        pup = list(str(x))
        pip = list(str(x+3330))
        pap = list(str(x+6660))
        pup.sort()
        pip.sort()
        pap.sort()

        if x+3330 in primes and x+6660 in primes and pup == pip and pip == pap:
            print(x,x+3330,x+6660)
