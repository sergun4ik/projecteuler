''' Solves problem # 174 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

def generate_squares(limit):
    squares = [ x**2 for x in range(1,limit+1)]
    return squares


squares = generate_squares(100000)

evens = [x for x in squares if not (x%2) ]
odds = [x for x in squares if (x%2)]


def distinct_laminae(tiles):
    laminae = 0
    #print(mysquares)
    for x in squares:
        for y in squares:
            #print (abs(x-y))
            if abs(x-y)==tiles:
                laminae+=1
    return laminae//2



def distinct_laminae(tiles):
    tiles_used = 0
    starthole = 1
    laminae = 0
    while starthole <= (tiles//2) - 1:
        side = starthole
        while tiles_used <= tiles:
            #print(starthole, tiles_used)
            tiles_used = tiles_used + (side + 2) * 2 + side * 2
            if tiles_used == tiles:
                laminae += 1
                #print(starthole,tiles_used)
            side += 2
        starthole += 1
        tiles_used = 0
        #print(starthole)
    return laminae

def distinct_laminae(tiles):
    start_side = tiles//4
    laminae = 0
    for x in range(start_side,1,-1):
        for y in range((x-1),1,-1):
            if x**2 - y**2 == tiles:
                laminae += 1
                if laminae > 10:
                    return laminae
    return laminae

#print(distinct_laminae(100000))
counter = 0
for x in range(1,1000000):
    print(x)
    if distinct_laminae(x) > 0 <=10:
        counter += 1

print(counter)


