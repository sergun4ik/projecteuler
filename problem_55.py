''' Solves problem #55 on https://projecteuler.net
Sergey Lisitsin. January 2020'''

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_lychrell(num):
    current = num
    for x in range(50):
        current = current+int(str(current)[::-1])
        if is_palindrome(current):
            return False
    return True

lycs = []

for a in range (10000):
    if is_lychrell(a):
        lycs.append(a)
print(len(lycs))