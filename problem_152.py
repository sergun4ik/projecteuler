''' Solves problem # 152 on https://projecteuler.net
Sergey Lisitsin. Apr 2020
'''


inverse_squares = [ 1/x**8 for x in range(2,80) ]

print(inverse_squares[-1])

