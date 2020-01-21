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

list = findprimes(2000000)
sum(list)
