''' Solves problem #17 on https://projecteuler.net
Sergey Lisitsin. July 2019'''

from itertools import permutations

def isprime(num):
    if str(num)[-1] in '0 2 4 5 6 8'.split():
        return False
    for x in range(2,(abs(int(num))//2)+1):
        if abs(int(num)) % x == 0:
            return False
    return True

def ispan(num):
    pan = '123456789'
    l = len(str(num))
    a = str(num)
    b = list(a)
    b.sort()
    a = ''.join(b)
    if a == pan[:l:]:
        return True
    return False

digits = '123456789'
for x in range(1,10):
    currentlist = permutations(digits[:x:])
    for x in currentlist:
        string = ''.join(x)
        #print(string)
        if ispan(string):
            if isprime(string):
                print(string)
