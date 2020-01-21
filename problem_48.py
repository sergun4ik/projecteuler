''' Solves problem #48 on https://projecteuler.net
Sergey Lisitsin. December 2019'''

start = 1
result = 0

while start < 1000:
    result = result + start**start
    start += 1

print (str(result)[-10::])

