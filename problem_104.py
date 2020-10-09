''' Solves problem # 104 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''
from decimal import getcontext as dc
from decimal import Decimal as D


# def generate_fibonacci(*pair):
#     return (pair[1], pair[1]+pair[0])


# a = generate_fibonacci(1, 1)
# counter = 3
# while len(str(a[1])) < 18:
#     a = generate_fibonacci(*a)
#     counter += 1

testset = set('123456789')
print(testset)
#beg = sorted(str(a[1])[:9:])
#end = sorted(str(a[1])[::-1][:9:])

#print(beg,end)

# while True:
#     #beg = sorted(str(a[1])[:9:])
#     #end = sorted(str(a[1])[-1:-10:-1])
#     #print(counter)
#     #print(beg,end)
#     if set(str(a[1])[:9:]) == testset:
#         print('Fibonacci {} front is pandigital'.format(counter))
#     if set(str(a[1])[-1:-10:-1]) == testset:
#         print('Fibonacci {} end is pandigital'.format(counter))
#     if set(str(a[1])[:9:]) == set(str(a[1])[-1:-10:-1]) == testset:
#         break
#     # print(counter)
#     # if set(str(a[1])[:9:]) == testset:
#     #     if set(str(a[1])[:9:]) == set(str(a[1])[::-1][:9:]):
#     #         print(str(a[1])[::-1][:9:], str(a[1])[:9:])
#     #         break
#     a = generate_fibonacci(*a)
#     counter += 1

# print(str(a[1])[::-1][:9:], str(a[1])[:9:])
# print(a[1])
# print(counter)

Phi = ((5**0.5)+1)/5**0.5
phi = (Phi-1)
def fib(n):
    num = D(n)
    return int(((Phi**n)-(-phi)**n)/(Phi-(-phi)))

found = False
counter = 1
while not found and counter < 700:
    current = D(fib(counter))
    print (counter)
    print (current)
    if set(str(current)[::-1][:9:]) == testset:
        print(f"Fibonacci {counter}\'s end is pandigital")
        if set(str(current)[:9:]) == testset:
            print(f"Fibonacci {counter}\'s start is pandigital")
            found = True
    if set(str(current)[:9:]) == testset:
        print(f"Fibonacci {counter}\'s start is pandigital")
    counter+=1


print (counter)
    