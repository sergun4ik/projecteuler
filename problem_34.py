''' Solves problem # 34 on https://projecteuler.net
Sergey Lisitsin. July 2019
'''
def factorial(num):
    result = 1
    for x in range(1,num+1):
        result = result * x
    return result

def factorialsum(num):
    sum = 0
    for x in str(num):
        sum += factorial(int(x))
    return sum
result = 0

for x in range(99999):
    if factorialsum(x) == x:
        result+=x
print(result-3)
