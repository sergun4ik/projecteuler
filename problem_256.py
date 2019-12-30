import re

def compiletree(length):
  treelength = 2**length
  tree = []
  modifier = len(str(bin(treelength))[2::])
  modstring = '0' + str(modifier) + 'b'
  for x in range(treelength):
    line = str(format(x, modstring))
    #print(line)
    if not line[1::].startswith('111'):
      if not line[1::].endswith('111'):
        tree.append(line[1::])
  return (tree)
  

def deletes(cases):
  dup = cases
  dels = []
  for x in cases:
    for y in dup:
      if x == y:
        continue
      if x == y[::-1]:
        #print("comparing {} to {}".format(x,y))
        cases.remove(y)
  return (cases)
  
 
def buildtape(case, side1, side2):
  tape = [0]*(side1*side2)
  tat = 1
  for x in case:
    index = tape.index(0)
    if x == '0':
      step = 1
    else:
      step = side1
    if tape[index] == 0:
      tape[index] = tat
    if index+step > len(tape)-1:
      return('Invalid case')
    if tape[index+step] != 0:
      return('Invalid case')
    tape[index+step] = tat
    tat = tat + 1
  return(tape)
 
 
 
def isunique(subset):
  subset.sort()
  for x in range(3):
    if subset[x]==subset[x+1]:
      return ('True')
  return ('False')


def verifytape(tape,side1,side2):
  step = side1
  for x in range(len(tape)-step-1):
    subset = list((tape[x],tape[x+1],tape[x+step],tape[x+step+1]))
    if not isunique(subset):
      return ("invalid room")
  return ("valid room")



def returnmask(num):
  mask = (len(bin(num))-2)
  return (2**mask)-1



room = 4
tatfree = 0
while tatfree < 1:
  tats = int(room/2)
  configs = factors(room)
  for x in configs:
    print ("checking room size {} sides {} by {}".format(room,x[0],x[1]))
    tree = compiletree(tats)
    tree = deletes(tree)
    #print(tree)
    for p in tree:
      tape = buildtape(p,*x)
      if verifytape(tape,*x) == 'invalid room':
        tatfree = tatfree +1
        print ('tatfree count is {}'.format(tatfree))
  room = room + 2
          

def clearcases(length):
  cases = []
  subcases = []
  for x in range(4,2**length):
    l = length - len(str(bin(x))[2::])
    cases.append('0'*l + (str(bin(x)))[2::])
  for x in cases:
    cur = x.split('1')
    for z in cur:
      if len(z) % 2 != 0:
        subcases.append(x)
  for x in cases:
    if '111' in x:
      subcases.append(x)
  return(list(set(cases)-set(subcases)))
  

def validfirst(line):
  if line.startswith('111') or line.endswith('10'):
    return False
    

def arecompatible(line1,line2):
  compstep = len(line1)
  for x in line1:
    if x == '1' and line2[line1.index(x)] == '0':
      return False
  return True
  
def isstackable(line1,line2):
  for x in range(len(line1)):
    if line1[x] == '1' and line2[x] == '0':
      return False
  return True
  
def numberise(cases):
  numcases = []
  for x in cases:
    curstring = []
    for p in range(len(x)):
      curstring.append(int(x[p]))
    numcases.append(curstring)
  return numcases

def mutuallyexclusive(line1,line2):
  if not isstackable(line1,line2) \
  and not isstackable(line2,line1):
    return True
  return False

def goodpairs(nums):
  pairs = []
  for x in nums:
    for y in nums:
      if not mutuallyexclusive(x,y) and not x == y:
        pairs.append(list((x,y)))
  return pairs
  
    
def filtercases(cases):
  subcases = []
  for x in cases:
    current = False
    curset = set(cases)
    curset.remove(x)
    print("current subset is {}".format(curset))
    for y in curset:
      if not mutuallyexclusive(x,y):
        current = True
    if not current:
      subcases.append(x)
  return list(set(cases)-set(subcases))
   

def creatematrix(side1,side2):
  result = []
  for x in range(side1):
    result.append([])
  for y in result:
    for p in range(side2):
       y.append(0)
  return result


  
def rotate(matrix):
  result = []
  for x in range((len(matrix[0]))-1,-1,-1):
    subresult = []
    for y in matrix:
      subresult.append(y[x])
    result.append(subresult)
  return result



def haszero(matrix):
  for x in matrix:
    if 0 in x:
      return True
  return False

 

def findgaprow(matrix):
  for x in matrix:
    if 0 in x:
      return matrix.index(x)
  return -1




def rowfill(matrix,starttat):
  row = findgaprow(matrix)         # Index of the row in matrix 
  start = matrix[row].index(0)
  split = matrix[row].count(0)
  if split % 2 != 0:
    end = start+split-1
  else:
    end = start+split
  for x in range(start,end,2):
    matrix[row][x] = starttat
    matrix[row][x+1] = starttat
    starttat = starttat + 1  
  return matrix,starttat



 
def spiralfill(matrix):
  multiplier = len(str(len(matrix)*len(matrix[0])))
  tat = 1*(10**(multiplier-2))
  while haszero(matrix):
    matrix,tat = rowfill(matrix,tat)
    matrix = rotate(matrix)
  return matrix




def verifyroom(room):
  side1 = len(room)
  side2 = len(room[0])
  for x in range(side1-1):
    for y in range(side2-1):
      x1 = x
      x2 = x + 1
      y1 = y
      y2 = y + 1
      subarr = [room[x1][y1],room[x1][y2],room[x2][y1],room[x2][y2]]
      subarr.sort()
      if subarr[0] != subarr[1] != subarr[2] != subarr[3] :
        print("Room size {} by {} fails check with result {},{},{},{}".format( \
        side1,side2,subarr[0],subarr[1],subarr[2],subarr[3]))
        return True
  return False



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



def countfree(area):
  rooms = factors(area)
  freecount = 0
  for x in rooms:
    if 2 in x:
      continue
    if 3 in x:
      continue
    current = creatematrix(x[0],x[1])
    currentfill = spiralfill(current)
    print("Current room size is {} by {}".format(x[0],x[1]))
    slicesx = slicex(*x)
    slicesy = slicey(*x)
    #print("X slices are: {}".format(slicesx))
    #print("Y slices are: {}".format(slicesy))
    kusok = False
    if (len(slicesx)) > 1:
      for y in slicesx:
        kusok = False
        if 2 in y or 3 in y:
          continue
        if y[0] % 2 != 0 and y[1] % 2 != 0:
          continue
        sliceroom = creatematrix(y[0],y[1])
        fillslice = spiralfill(sliceroom)
        print("Current subroom size is {} by {}".format(y[0],y[1]))
        if not verifyroom(fillslice):
          kusok = True
          break
    if not kusok and (len(slicesy)) > 1:
      for y in slicesy:
        kusok = False
        if 2 in y or 3 in y:
          continue
        if y[0] % 2 != 0 and y[1] % 2 != 0:
          continue
        sliceroom = creatematrix(y[0],y[1])
        fillslice = spiralfill(sliceroom)
        print("Current subroom size is {} by {}".format(y[0],y[1]))
        if not verifyroom(fillslice):
          kusok = True
          break
    if verifyroom(currentfill) and not kusok:
      print("the tatami-free room is {} by {}".format(x[0], x[1]))
      freecount = freecount + 1
  return freecount



def slicex(x1, x2):
  slicerooms = []
  pieces = factors(x1)
  for x in pieces:
    slicerooms.append([x[0],x2])
    slicerooms.append([x[1],x2])
  return slicerooms

def slicey(x1, x2):
  slicerooms = []
  pieces = factors(x2)
  for x in pieces:
    slicerooms.append([x[0],x1])
    slicerooms.append([x[1],x1])
  return slicerooms

  
