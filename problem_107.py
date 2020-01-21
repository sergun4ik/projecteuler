''' Solves problem #107 on https://projecteuler.net
Sergey Lisitsin. Jan 2020'''

import itertools

def creatematrix(side1, side2):
  result = []
  for x in range(side1):
    result.append([])
  for y in result:
    for p in range(side2):
       y.append(0)
  return result


def link(a, b, matrix, cost):
    matrix[a][b]=cost
    matrix[b][a]=cost

def get_links(m):
    links = []
    for x in m:
        mylinks = []
        for y in range(len(x)):
            if x[y] > 0:
                #print(x[y],y)
                mylinks.append(y)
        links.append((mylinks))
    return links


def check(l,m):
    for x in range(len(l)):
        if len(l[x]) == 1:
          return True
    return False

def reduce(l, m):
  for x in range(len(l)):
     if len(l[x]) == 1:
         addr = 0
         for y in l[x]:
             if y:
                 addr = l.index(l[y])
         m[x][addr] = 0
         m[addr][x] = 0
  l = get_links(m)


def del_expensive(m):
    most = 0
    i = ()
    for x in range(len(m)):
        for y in range(len(m[x])):
            if m[x][y] > most:
                most = m[x][y]
                i = (x,y)
    m[i[0]][i[1]] = 0
    m[i[1]][i[0]] = 0


def find_expensive(m):
    most = 0
    i = ()
    for x in range(len(m)):
        for y in range(len(m[x])):
            if m[x][y] > most:
                most = m[x][y]
    return most

def ssum(m):
    summ = 0
    for x in m:
        summ += sum(x)
    return summ

m = []
f = open('p107_network.txt','r')
matrix = f.read()
matrix2 = matrix.split('\n')
matrix2.pop(-1)
for x in matrix2:
    submat = []
    for y in x.split(','):
        if y == '-':
            submat.append(0)
        else:
            submat.append(int(y))
    m.append(submat)


counter = 0
while ssum(m):
    l = get_links(m)
    #print(l,m)
    if check(l,m):
        reduce(l,m)
    else:
        #print("loop found")
        counter += find_expensive(m)
        del_expensive(m)
print(counter)





