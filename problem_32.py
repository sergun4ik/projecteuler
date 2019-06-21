''' Solves problem #32 on https://projecteuler.net
Sergey Lisitsin. May 2019'''

pans = set()
digits = '123456789'
for x in range(1000):
    for y in range(10000):
        interim = str(x) + str(y) + str(x*y)
        interim = ''.join(sorted(interim))
        print (interim)
        if interim == digits:
            pans.add(x*y)

thelist = list(pans)
result = 0
for x in thelist:
    result += x

print(result)
