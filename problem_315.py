''' Solves problem # 315 on https://projecteuler.net
Sergey Lisitsin. Apr 2020
'''


digs =  [126, 12, 91, 31, 45, 55, 60, 28, 127, 63]

def digit_transition(dig1,dig2):
    if dig1 == '*':
        result = 0 ^ digs[dig2]
    elif dig2 == '*':
        result = digs[dig1] ^ 0
    else:
        result = digs[dig1] ^ digs[dig2]
    count = str(bin(result)).count('1')
    return count

def max_transition(n1, n2):
    if n1 == 0:
        string1 = ''
        string2 = str(n2)
    elif n2 == 0:
        string2 = ''
        string1 = str(n1)
    else:
        string1 = str(n1)
        string2 = str(n2)
    if len(string1) > len(string2):
        dif = len(string1)-len(string2)
        filler = '*'*dif
        string2 = filler+string2
    elif len(string2) > len(string1):
        dif = len(string2)-len(string1)
        filler = '*'*dif
        string1 = filler + string1
    counter = 0
    for x,y in zip(string1, string2):
        if x == '*':
            counter += digit_transition('*',int(y))
        elif y == '*':
            counter += digit_transition(int(x),'*')
        else:
            counter += digit_transition(int(x),int(y))
    return counter

def reduce_number(n):
    if len(str(n)) > 1:
        l = [int(x) for x in str(n)]
        count = 0
        for x in l:
            count += x
        return count
    else:
        return n


def root_chain(num):
    chain = [num]
    while len(str(num)) > 1:
        num = reduce_number(num)
        chain.append(num)
    chain.append(0)
    return chain

def max_transitions(num):
    counter = 0
    while num > 0:
        reduced = reduce_number(num)
        counter+= max_transition(num,reduced)
        num = reduced
    counter += max_transition(num,'*')
    return counter

def sam_transition(n1):
    counter = 0
    string = str(n1)
    for x in string:
        counter += digit_transition(int(x),'*')
    return counter*2

chain = root_chain(137)
count = 0
for x in range(len(root_chain)-1):
    pair = (chain[x],chain[x]+1)
    count +=
