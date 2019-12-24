''' Solves problem #44 on https://projecteuler.net
Sergey Lisitsin. July 2019'''

def pents(count):
    result = [1]
    s = 2
    while len(result) < count:
        next = s*(s*3 - 1)/2
        result.append(int(next))
        s+=1
    return result

pens = pents(10000)
pairs = set()

for x in pens:
    for y in pens:
        if x == y:
            continue
        if x+y in pens and abs(x - y) in pens:
            print(abs(x-y))
            break
