''' Solves problem # 24 on https://projecteuler.net
Sergey Lisitsin. May 2019
'''

def perms(num):
    result = set()
    for x in permutations((num)):
        result.add((''.join(x)))
    return list(result)

t = perms('0123456789')
t.sort()
t[999999]

