''' Solves problem #31 on https://projecteuler.net
Sergey Lisitsin. May 2019'''

p = 1
p2 = 2
p5 = 5
p10 = 10
p20 = 20
p50 = 50
pound = 100
pound2 = 200

coins = [p, p2, p5, p10, p20, p50, pound, pound2]

ways = 0

for coin in coins:
    for subcoin in coins.remove(coin):