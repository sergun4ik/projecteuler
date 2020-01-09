''' Solves problem #46 on https://projecteuler.net
Sergey Lisitsin. January 2020'''

def isprime(num):
    for x in range(2,(num//2)+1):
        if num%x == 0:
            return False
    return True

def checkcubesum(prime,num):
    start = 1
    while prime + 2 * start**2 < num:
        start += 1
        if prime + 2 * start ** 2 == num:
            return True
    return False

def goldbach(num):
    smallerprimes = []
    for x in range(2,num):
        if isprime(x):
            smallerprimes.append(x)
    #print(smallerprimes)
    gold = False
    for x in smallerprimes:
        if checkcubesum(x,num):
            return True
    return False

p = 5001
while goldbach(p):
    p+=2
    if isprime(p):
        continue

print(p)


