''' Solves problem #46 on https://projecteuler.net
Sergey Lisitsin. January 2020'''

def isprime(num):
    for x in range(2,(num//2)+1):
        if num%x == 0:
            return False
    return True

def goldbach(num):
    smallerprimes = []
    for x in range(1,num):
