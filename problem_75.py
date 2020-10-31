""" Solves problem # 75 on https://projecteuler.net
Sergey Lisitsin. Oct 2020
"""
from numpy import matrix, matmul


a = matrix([[1, -2, 2], [2, -1, 2], [2, -2, 3]])  # These are 3 "Magic matrices" that when multiplied
b = matrix([[1, 2, 2], [2, 1, 2], [2, 2, 3]])     # by a column of a Pythagorean triplet produce
c = matrix([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])  # new Pythagorean triple

origin = [3, 4, 5]                                # We start with the first triple

undone = []                                       # This is a storage for unprocessed triples
sums = []                                         # This is a storage for triple sums


def hatch(l):
""" The hatch function takes in a list with a Pythagorean triplet
and places the sum of the triplet into sums. Then it multiplies it
by each of the Magic matrices, thus generating 3 new triplets.
Then these are appended to undone. """
  sums.append(sum(l))
  undone.append((matmul(a,l)).tolist())
  undone.append((matmul(b,l)).tolist())
  undone.append((matmul(c,l)).tolist())

hatch(origin)                                     # Processing the first Triplet
limit = 1500000                                   # Setting the limit


sums.sort()                                       # Sorting the sums list is very important to make sure
                                                  # they are processed consecutively later on

while sum(undone[0][0]) < limit or sum(undone[1][0]) < limit \  # This block keeps generating new triplets until
        or sum(undone[2][0]) < limit:                           # all 3 of triplets generated from a single 'parent'
    hatch(undone[0][0])                                         # are greater than the limit. The new tiplets are
    undone.pop(0)                                               # added to undone and sorted after each iteration
    hatch(undone[0][0])
    undone.pop(0)
    hatch(undone[0][0])
    undone.pop(0)
    undone.sort(key=lambda x: sum(x[0]))

undone.sort(key=lambda x: sum(x[0]))                            # additional sort

sums = [x for x in sums if x <= limit]                          # Now filtering out the sums that are greater than
                                                                # the limit
sums = [x for x in sums if sums.count(x) == 1]                  # Selecting only the unique sums


sums.sort()                                                     # Last sort of sums after filtering
results = []                                                    # This is the storage for candidate L values

for x in range(2, limit+1,2):                                   # Main loop runs through even numbers from 2 to limit
    for y in sums:                                              # and if it is evenly divisible by any of the sums,
        if y > x:                                               # adding it to results list.
            break
        if x % y == 0:
          results.append(x)


result = [x for x in results if results.count(x) == 1]          # filtering the result to only chose numbers that appear
                                                                # in the list once
print(result)                                                   # Printing the resulting list

print (len(result))                                             # The length of this list is our final value of all
                                                                # the numbers that satisfy problem criteria.

