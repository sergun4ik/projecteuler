''' Solves problem # 52 on https://projecteuler.net
Sergey Lisitsin. Jan 2020
'''
def numtoset(num):
    result = set()
    for x in str(num):
        result.add(x)
    return result

for x in range(1000,10000000):
    single = numtoset(x)
    double = numtoset(x*2)
    triple = numtoset(x*3)
    quad = numtoset(x*4)
    quant = numtoset(x*5)
    sext = numtoset(x*6)
    if single==double==triple==quad==quant==sext:
        print(x)
        break