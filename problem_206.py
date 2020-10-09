''' Solves problem # 206 on https://projecteuler.net
Sergey Lisitsin. Feb 2020
'''

x = 0
result = 0
while str(result)[::2] != '1234567890':
  x+=10
  result = x**2

print(x)