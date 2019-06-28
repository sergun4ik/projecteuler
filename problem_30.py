''' Solves problem # 30 on https://projecteuler.net
Sergey Lisitsin. May 2019
'''

powers = [x**5 for x in range(10)]
numbers = [x for x in range(1000,999999)]

result = 0
for x in numbers:
  digits = list(str(x))
  sum = 0
  for y in digits:
    sum += powers[int(y)]
  if sum == x:
    result += x

print(result)