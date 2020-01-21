''' Solves problem #53 on https://projecteuler.net
Sergey Lisitsin. Jan 2020'''

from math import factorial

results = 0
for n in range(1,101):
    for r in range(1,101):
        if n <= r:
            continue
        if factorial(n)/(factorial(r)*factorial(n-r)) > 1000000:
            results += 1

print(results)