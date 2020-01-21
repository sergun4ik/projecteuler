''' Solves problem #92 on https://projecteuler.net
Sergey Lisitsin. Jan 2020'''


def chain(num):
    sqsumm = 0
    for x in str(num):
        sqsumm = sqsumm + int(x) ** 2
    if sqsumm == 89:
        return 89
    if sqsumm == 1:
        return 1
    else:
        return chain(sqsumm)

res = 0

for x in range(1,10000000):
    if chain(x) == 89:
        res+=1

print(res)