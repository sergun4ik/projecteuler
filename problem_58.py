''' Solves problem # 58 on https://projecteuler.net
Sergey Lisitsin. Nov 2020
'''


def is_prime(num):
    ''' finds if a number is prime '''
    if num==1:
        return False
    for x in range(2,int(num**0.5)+1):
        if num%x==0:
            return False
    return True

diagonals = [1]
primes = set([3])

counter = 3
while len(primes)/len(diagonals) > 0.1:
    current = counter**2
    step = counter - 1
    for x in range(3,-1,-1):
        diagonals.append(current - x*step)
        if is_prime(diagonals[-1]):
            primes.add(diagonals[-1])
    #print(len(diagonals), len(primes), len(primes)/len(diagonals))
    counter += 2

print(diagonals[-1]**0.5)
