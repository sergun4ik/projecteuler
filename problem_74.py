''' Solves problem # 74 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

from math import factorial


def factsum(nums):
    res = 0
    for x in nums:
        res += factorial(x)
    return res

def chain_length(num):
    digs = [int(x) for x in str(num)]
    chain = [num]
    result = 0
    while result not in chain:
        if result != 0:
            chain.append(result)
        result = factsum(digs)
        digs = [int(x) for x in str(result)]
    return len(chain)


start = 1
counter = 0
while start < 1000000:
    if chain_length(start) == 60:
        counter += 1
    start += 1

print(counter)