''' Solves problem # 42 on https://projecteuler.net
Sergey Lisitsin. May 2019
'''

def triangles(count):
    triang = [1]
    for x in range(2,count+1):
        summa = triang[-1]
        nex = summa + x
        triang.append(nex)
    return triang

counter = 0
tri = triangles(100)
file = open('c:\\users\\sergeyl\\Downloads\\Code\\euler\\p042_words.txt','r')
lines = file.read()
#lines = lines.split()
for x in lines.split(','):
    #print(x)
    value = 0
    for p in x[1:-1:]:
        value+=ord(p.lower())-96
    if value in tri:
        counter+=1
   #     print("{} {} ".format(x[1:-1:],value))

print(counter)