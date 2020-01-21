''' Solves problem #47 on https://projecteuler.net
Sergey Lisitsin. January 2020'''

def isprime(num):
    for x in range(2,(num//2)+1):
        if num%x == 0:
            return False
    return True

def checkfactors(num,*factors):
    o = 1
    for p in factors:
        o = o * p
    if o == num:
        return  True
    return False

def primefactors(num):
  factors =[]
  for x in range(2,num//2):
      if num%x==0:
          factors.append(x)
  return list(filter(lambda x: isprime(x), factors))


start = 1000
while(True):
    one = start - 1
    two = start
    three = start + 1
    four = start + 2
    #print(one)
    if len(primefactors(one)) != 4:
       start +=1
       continue
    if len(primefactors(two)) != 4:
       start +=2
       continue
    if len(primefactors(three)) != 4:
       start +=3
       continue
    if len(primefactors(four)) !=4:
       start += 4
       continue
    else:
        print(start-1)
        break
    start += 1
print(start)


