''' Solves problem #39 on https://projecteuler.net
Sergey Lisitsin. May 2019'''


def isright(a,b,c):
    sides = [a,b,c]
    sides.sort()
    if sides[-1]**2 == (sides[0]**2+sides[1]**2):
        return True
    return False

def champ(list):
    champion = 0
    for x in list:
        if list.count(x) > champion:
            champion = x
    return champion

sides1 = sides2 = sides3 = list(range(1,998))

results = []
for x in sides1:
    for y in sides2:
        for z in sides3:
            if x+y+z>1000:
                continue
            if x == y and x ==z:
                continue
            if isright(x,y,z):
                results.append(x+y+z)


print(champ(results))
