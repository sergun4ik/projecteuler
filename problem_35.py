''' Solves problem # 35 on https://projecteuler.net
Sergey Lisitsin. May 2019
'''


def findprimes(num):
    primes = [2, 3]
    for x in range(5, num, 2):
        third = x // 3
        prime = True
        for p in primes:
            if x % p == 0:
                prime = False
                break
        if prime:
            primes.append(x)
    return primes


def rotation(n):
    rotations = set()
    for i in range(len(str(n))):
        n = int(str(n)[1:] + str(n)[:1])
        rotations.add(n)
    return rotations


primes = findprimes(1000000)
circulars = []
for x in primes:
    permuts = []
    circular = True
    # print(str(x))
    for p in (rotation(x)):
        if p not in primes:
            circular = False
            break
    if circular:
        circulars.append(x)

len(circulars)
