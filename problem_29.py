''' Solves problem #29 on https://projecteuler.net
Sergey Lisitsin. May 2019'''

a = b =list(range(2,101))
result = set()
for x in a:
    for y in b:
        result.add(x**y)

print(len(list(result)))

