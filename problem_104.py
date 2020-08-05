''' Solves problem # 104 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

def generate_fibonacci(*pair):
    return (pair[1], pair[1]+pair[0])


a = generate_fibonacci(1, 1)
counter = 3
while len(str(a[1])) < 18:
    a = generate_fibonacci(*a)
    counter += 1

testset = ['1','2','3','4','5','6','7','8','9']

#beg = sorted(str(a[1])[:9:])
#end = sorted(str(a[1])[::-1][:9:])

#print(beg,end)

while True:
    #beg = sorted(str(a[1])[:9:])
    #end = sorted(str(a[1])[-1:-10:-1])
    #print(counter)
    #print(beg,end)
    if sorted(str(a[1])[:9:]) == testset:
        print('Fibonacci {} front is pandigital'.format(counter))
    if sorted(str(a[1])[-1:-10:-1]) == testset:
        print('Fibonacci {} end is pandigital'.format(counter))
    if sorted(str(a[1])[:9:]) == sorted(str(a[1])[-1:-10:-1]) == testset:
        break
    # print(counter)
    # if set(str(a[1])[:9:]) == testset:
    #     if set(str(a[1])[:9:]) == set(str(a[1])[::-1][:9:]):
    #         print(str(a[1])[::-1][:9:], str(a[1])[:9:])
    #         break
    a = generate_fibonacci(*a)
    counter += 1

print(str(a[1])[::-1][:9:], str(a[1])[:9:])
print(a[1])
print(counter)