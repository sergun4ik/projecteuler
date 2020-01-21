''' Solves problem #15 on https://projecteuler.net
Sergey Lisitsin. May 2019'''

def propdivs(num):
    ''' Returns all the number's proper divisors'''
    result = [1]
    for x in range(2,(num//2)+1):
        if num % x == 0:
            result.append(x)
    return result

def isabundant(num):
    return sum(propdivs(num)) > num

abundants = set()

for x in range(12, 28124):
    if isabundant(x):
        abundants.add(x)

sums = set()
for x in abundants:
    for y in abundants:
        if x + y < 28124:
            sums.add(x+y)

allnums = set(range(23124))

targetset = allnums - sums
sum(targetset)
