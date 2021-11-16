''' Solves problem # 315 on https://projecteuler.net
Sergey Lisitsin. Apr 2020
'''


zero = [1,1,1,1,1,1,0]
one = [0,0,0,1,1,0,0]
two = [1,0,1,1,0,1,1]
three = [0,0,1,1,1,1,1]
four = [0,1,0,1,1,0,1]
five = [0,1,1,0,1,0,1]
six = [1,1,1,0,1,1,1]
seven = [0,1,1,1,1,0,0]
eight = [1,1,1,1,1,1,1]
nine = [0,1,1,1,1,1,1]
off = [0,0,0,0,0,0,0]
digits = [zero, one, two, three, four, five, six, seven, eight, nine, off]

def digit_switch(dig):
    return(dig.count(1))

def digit_transition(dig1,dig2):
    d1arr = digits[int(dig1)]
    d2arr = digits[int(dig2)]
    count = 0
    for x,y in zip(d1arr,d2arr):
        count += x ^ y
    return count


def max_transition(n1,n2):
    counter = 0
    n1arr = [int(x) for x in str(n1)]
    n2arr = [int(x) for x in str(n2)]
    n1len = len(n1arr)
    n2len = len(n2arr)
    dif = abs(n1len-n2len)
    while n2len < n1len:
        n2arr.insert(0,10)
        n2len = len(n2arr)
    while n1len < n2len:
        n1arr.insert(0,10)
        n1len = len(n1arr)
    print(n1arr,n2arr)
    for x,y in zip(n1arr,n2arr):
        counter += digit_transition(x,y)
    return counter


    def max_transition(n1, n2):
    n1arr = [digits[int(x)] for x in str(n1)]
    n2arr = [digits[int(x)] for x in str(n2)]
    n1diff = 3 - len(n1arr)
    n2diff = 3 - len(n2arr)
    for x in range(n1diff):
        n1arr.insert(0,off)
    for x in range(n2diff):
        n2arr.insert(0,off)
    for x,y in zip (n1arr,n2arr):
        print(digit_transition(x,y))

def sams_number(num):
    n1arr = [digits[int(x)] for x in str(num)]
    n2arr = [off] * len(n1arr)
    return digit_transition(n1arr, n2arr)

