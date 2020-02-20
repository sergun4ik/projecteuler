''' Solves problem # 179 on https://projecteuler.net
Sergey Lisitsin. Feb 2020
'''

def bump(l,step):
    sub = [x+1 for x in l[::step]]
    l[::step] = sub

a = [0] * ((10**7)+1)
counter = 0
for x in range(1,10**7+1):
    bump(a,x)
for x in range(len(a)-1):
    if a[x]==a[x+1]:
        counter+=1

print(counter)