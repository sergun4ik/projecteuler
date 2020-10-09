'''
Project Euler Problem 138
'''
from math import sqrt

def is_correct_plus(base):
    result = 0
    height = base * 2 + 1
    hyp = sqrt(height ** 2 + base ** 2)
    if (hyp).is_integer():
        print(hyp)
        result += hyp
        print('{:30}{:30}{:30}'.format(int(base*2), int(height), int(hyp)))
    return (result)

def is_correct_minus(base):
    result = 0
    height = base * 2 - 1
    hyp = sqrt(height ** 2 + base ** 2)
    if (hyp).is_integer():
        print(hyp)
        result += hyp
        print('{:30}{:30}{:30}'.format(int(base*2), int(height), int(hyp)))
    return (result)

total = 0
count = 0
start = 1.0
while count < 12:
    #print(start)
    curplus = is_correct_plus(start)
    curminus = is_correct_minus(start)
    if curplus > 0:
        #print(curplus)
        total+=curplus
        count+=1
        #print(total)
    if curminus > 0:
        #print(curminus)
        total+=curminus
        count+=1
        #print(total)
    start += 0.5

print(total)