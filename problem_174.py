''' Solves problem # 174 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

# def generate_squares(limit):
#     squares = [ x**2 for x in range(1,limit+1)]
#     return squares
#
#
# squares = generate_squares(100000)

# evens = [x for x in squares if not (x%2) ]
# odds = [x for x in squares if (x%2)]

#
# def distinct_laminae(tiles):
#     laminae = 0
#     #print(mysquares)
#     for x in squares:
#         for y in squares:
#             #print (abs(x-y))
#             if abs(x-y)==tiles:
#                 laminae+=1
#     return laminae//2



# def distinct_laminae(tiles):
#     tiles_used = 0
#     starthole = 1
#     laminae = 0
#     while starthole <= (tiles//2) - 1:
#         side = starthole
#         while tiles_used <= tiles:
#             #print(starthole, tiles_used)
#             tiles_used = tiles_used + (side + 2) * 2 + side * 2
#             if tiles_used == tiles:
#                 laminae += 1
#                 #print(starthole,tiles_used)
#             side += 2
#         starthole += 1
#         tiles_used = 0
#         #print(starthole)
#     return laminae

def find_smaller_squares(num):
    return [x**2 for x in range(1,num//2) if x**2 < num]

squares = find_smaller_squares(1000000)
squares.pop(0)

def find_distinct_laminae(num):
  result = 0
  subsquares = [x for x in squares if x < num ]
  for x in range(len(subsquares)):
    multiplier = 2
    while not(subsquares[x] * multiplier > num):
      if subsquares[x] * multiplier == num:
        result +=1
      multiplier += 1
  return (result)

# def distinct_laminae(tiles):
#     start_side = (tiles//4)+1
#     laminae = 0
#     for x in range(start_side,1,-1):
#         for y in range((x-1),0,-1):
#             if x**2 - y**2 == tiles:
#                 laminae += 1
#                 if laminae > 10:
#                     return laminae
#     return laminae

#print(distinct_laminae(100000))
counter = 0
for x in range(2,1000000):
    #print(x)
    p = find_distinct_laminae(x)
    #print(p)
    if p > 0 and p <=10:
        counter += 1
    print(x)

print(counter)



#
# squares = find_smaller_squares(1000000)
# def find_distinct_laminae(num):
#   result = []
#   subsquares = [x for x in squares if x < num ]
#   for x in range(len(subsquares)):
#     multiplier = 2
#     while subsquares[x] * multiplier < num:
#       if subsquares[x] * multiplier == num:
#         result.append(1)
#       multiplier += 1
#   return len(result)