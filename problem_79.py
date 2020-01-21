''' Solves problem #79 on https://projecteuler.net
Sergey Lisitsin. January 2020'''

data = open('p079_keylog.txt','r')
lines = data.readlines()
data.close()

sixes = []
print(lines)
for x in lines:
    for y in lines:
        p = x.replace('\n', '')
        q = y.replace('\n', '')
        if p[-2::] == q[:2:]:
            sixes.append(p+q[-1])
print(set(sixes))

