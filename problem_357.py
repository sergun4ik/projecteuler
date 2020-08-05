''' Solves problem # 357 on https://projecteuler.net
Sergey Lisitsin. June 2020
'''
from math import sqrt

def findprimes(count):
    ''' This function returns first count
    number of primes'''
    primes = [2, 3, 5, 7]
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

def is_prime(num):
    ''' finds if a number is prime '''
    if num==1:
        return False
    for x in range(2,int(sqrt(num)+1)):
        if num%x==0:
            return False
    return True

def propdivs(num):
    ''' Returns all the number's proper divisors'''
    result = [(1,num)]
    for x in range(2,int(sqrt(num)+1)):
        if num % x == 0:
            result.append((x,num//x))
    return result

primes = findprimes(10000)

start = list(range(2, 100000000,4))
start = [x for x in start if (x+1) % 3 !=0 ]
#print(len(start))
start = [x for x in start if str(x)[::-1][:2:] != '05']
start = [x for x in start if str(x)[-1] != '4']
start = [x for x in start if str(x)[-1] != '6']


numbers = {1,2,6}
for x in start:
    eligible = True
    for y in propdivs(x):
        if not is_prime(y[0]+y[1]):
            eligible = False
    if eligible:
        numbers.add(x)
        #print(x)

print(sum(numbers))
