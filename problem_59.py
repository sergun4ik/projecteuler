''' Solves problem # 59 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

from itertools import permutations

keys = list(permutations('abcdefghijklmnopqrstuvwxyz',3))

with open('p059_cipher.txt','r') as file:
    cipherdict = [int(x) for x in file.read().split(',')]

def decrypt(data,key):
    result = ''
    counter = len(key)
    for x in range(len(data)):
        result += chr(data[x] ^ ord(key[x%counter]))
    return result

testword = 'Euler'

for x in keys:
    cleartext = decrypt(cipherdict,x)
    if testword in cleartext:
        mainsum = 0
        for x in cleartext:
            mainsum = mainsum+(ord(x))
        break

print(mainsum)

