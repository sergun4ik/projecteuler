''' Solves problem #19 on https://projecteuler.net
Sergey Lisitsin. May 2019'''

const = ''

for x in range(1,1000000):
    const+=str(x)

a = (int(const[0]))
b = (int(const[9]))
c = (int(const[99]))
d = (int(const[999]))
e = (int(const[9999]))
f = (int(const[99999]))
g = (int(const[999999]))

print(a*b*c*d*e*f*g)
