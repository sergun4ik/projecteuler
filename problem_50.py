''' Solves problem #50 on https://projecteuler.net
Sergey Lisitsin. December 2019'''

def isprime(num):
    for x in range(2,(num//2)+1):
        if num%x == 0:
            return False
    return True

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

p = findprimes(5000)
champ = 0
champlist = []


while len(p)>3:
    summ = 0
    for x in range(len(p)):
        #if x < len(champlist):
        #    continue
        if x%2==0:
            continue
        sublist = p[x::]
        if len(sublist) < len(champlist):
            continue
        summ = sum(sublist)
        if summ > 1000000:
            continue
        if isprime(summ) and len(sublist)>len(champlist):
            champ = summ
            champlist = sublist
    p.pop(-1)


print("The winner is {} standing at {} primes long!".format(champ,len(champlist)))
