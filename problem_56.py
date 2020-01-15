''' Solves problem #56 on https://projecteuler.net
Sergey Lisitsin. Jan 2020'''

def numsum(num):
    summ = 0
    for x in str(num):
        summ = summ+int(x)
    return summ

best = 0
for x in range(1,100):
    for y in range(1,100):
       if numsum(x**y) > best:
           best = numsum(x**y)

print(best)