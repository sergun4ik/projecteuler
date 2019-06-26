''' Solves problem #27 on https://projecteuler.net
Sergey Lisitsin. May 2019'''


def sequence(a,b):
    n = 0
    seq = 0
    while seq == n:
 #       print ((n*(n+a))+b)
        if isprime(n*(n+a)+b):
           seq +=1
        n += 1
    return(seq)


def isprime(num):
    for x in range(2,(abs(num)//2)+1):
        if abs(num) % x == 0:
            return False
    return True



a = [x for x in range(-999,1000)]
b = [x for x in range(-1000,1001)]

champseq = 0
champs = [0,0]
for x in a:
    for y in b:
        if sequence(x,y) > champseq:
            champseq = sequence(x,y)
            champs[0] = x
            champs[1] = y

print("{}".format(champs[0]*champs[1]))




