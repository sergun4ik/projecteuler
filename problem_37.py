''' Solves problem #37 on https://projecteuler.net
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

def is_truncatable(prime):
    truncs = []
    truncatable = True
    for k in range(len(str(prime))):
        truncs.append(int(str(prime)[k::]))
    t = prime
    while t//10 > 0:
        truncs.append(t//10)
        t = t//10

   # for k in range(1,len(str(prime))-1):
   #     truncs.append(int(str(prime)[:k:]))
    for y in truncs:
        if y not in primes:
            truncatable = False
    return truncatable

primes = findprimes(1000000)
#print(primes)
tunks = []
for x in primes:
    if x > 7 and is_truncatable(x):
        tunks.append(x)
        #print(x)
print(sum(tunks))
