''' Solves problem #62 on https://projecteuler.net
Sergey Lisitsin. June 2019'''

def myhash(num):
    l = len(str(num))
    counts = {}
    for x in range(10):
        counts[x]=0
    for x in str(num):
        counts[int(x)]+=1
    return(l,counts)

def sibcount(num):
    sibs = 0
    for x in cubes:
        if len(str(x)) == len(str(num)) and myhash(num) == myhash(x):
            sibs += 1
    return sibs

cubes = [x**3 for x in range(346,10000)]

for x in cubes:
    if sibcount(x)==5:
        print(x)
        break
        

