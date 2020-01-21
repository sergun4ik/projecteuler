''' Solves problem #33 on https://projecteuler.net
Sergey Lisitsin. December 2019'''

def factors(num):
    ''' Returns a list of factors '''
    factor = []
    clear = []
    half = (num // 2) + 1
    for x in range(2, half):
        if num % x == 0:
            if list((int(num/x),x)) not in factor:
              factor.append(list((int(num/x),x)))
    for x in factor:
      x.sort()
    factor.sort()
    for x in range(len(factor)-1):
      if factor[x] == factor[x+1]:
        clear.append(factor[x])
    for x in clear:
      factor.remove(x)
    return (factor)


def cancelling(div, num):
    if len(str(div)) < 2 and len(str(num)) < 2:
        return False
    if div>num:
        return False
    if div == num:
        return False
    share = False
    for x in str(div):
        if x in str(num):
            share = True
            shared = x
            if shared == '0':
                return False

    #print (shared)
    if share:

        cd = str(div).replace(shared, '')
        cn = str(num).replace(shared, '')

        if cn == '' or cd == '':
          return False
        if int(cn) == 0 or int(cd) == 0:
          return False
        if int(cd) / int(cn) == div / num:
            return True
        else:
            return False

resd = 1
resn = 1
for d in range(10,100):
    for n in range(10,100):
        #print(d,n)
        if cancelling(d,n):
            resd = resd * d
            resn = resn * n
print(resd,resn)

factsd = factors(resd)
factsn = factors(resn)
#print (factsd)
#print (factsn)
flatd = [item for sublist in factsd for item in sublist]
flatn = [item for sublist in factsn for item in sublist]
print(flatd)
print(flatn)
divisors = set(flatd) & set(flatn)
print(divisors)
large = sorted(list(divisors))[-1]
print(large)
print(resd/large,resn/large)