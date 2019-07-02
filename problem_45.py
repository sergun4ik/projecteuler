''' Solves problem #45 on https://projecteuler.net
Sergey Lisitsin. July 2019'''

def pents(count):
    result = [1]
    s = 2
    while len(result) < count:
        next = s*(s*3 - 1)/2
        result.append(int(next))
        s+=1
    return result

def triangulars(count):
    result = [1]
    s = 2
    for x in range(1,count):
        result.append(s*(s+1)/2)
        s+=1
    return result

def hexagonals(count):
    result = [1]
    s = 2
    for x in range(1,count):
        result.append(s*((s*2) -1))
        s+=1
    return result

t = triangulars(99999)
p = pents(99999)
h = hexagonals(99999)

sub = set(t) & set(p) & set(h)
print(sub)