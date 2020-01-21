''' Solves problem #17 on https://projecteuler.net
Sergey Lisitsin. July 2019'''

def ispan(num):
    pan = '123456789'
    a = str(num)
    b = list(a)
    b.sort()
    a = ''.join(b)
    if a == pan:
        return True
    return False

multipliers = [1,2,3,4,5,6,7,8,9]
pan = '123456789'
numlist = []
for x in range(99999):
    mylist = ''
    for y in multipliers:
        mylist = mylist + str(x*y)
        if len(mylist) > 8:
            break
    if ispan(int(mylist)):
        numlist.append((x,mylist))


print(numlist[-1])