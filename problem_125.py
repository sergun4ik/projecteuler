''' Solves problem # 125 on https://projecteuler.net
Sergey Lisitsin. Feb 2020
'''

from math import sqrt

def is_palindrome(num):
    return str(num)==str(num)[::-1]

def generate_squares(num):
  while True:
    yield num**2
    num+=1


def find_largest_square(num):
    x = 0
    while x**2 < num:
        s = x**2
        x+=1
    maximumsquare = (x**2)
    return int(maximumsquare)


def find_sub_squares(num):
    biggest = int(sqrt(find_largest_square(num)))
    squares = [x**2 for x in range(1,biggest+1)]
    return squares

def get_squares_list(num):
    limit =  list(range(1,find_largest_square(num)+1))
    return [x**2 for x in limit if x**2 < num]

def find_sum(num):
    straight = get_squares_list(num)
    inverse = straight[::-1]
    while len(inverse) > 1:
        for x in range(len(inverse)+1):
            #print(x)
            if sum(inverse[:x:])==num:
                return True
            if sum(inverse[:x:])>num:
                break
        inverse.pop(0)
    return False

mylist = list(range(1,10**8+1))
slist = [x**2 for x in mylist if x**2 < 10**8+1]
winlist = []

while len(slist) > 1:
    x = len(slist)
    #print(x)
    for p in range(x):
        cursum = sum(slist[:p:])
        if cursum > 10**8:
            break
        if is_palindrome(cursum):
            if find_sum(cursum):
                winlist.append(cursum)
    slist.pop(0)


winset = set(winlist)

newlist = list(winset)
print(sum(newlist))
