'''
A script that solves problem #26 on Project Euler
https://projecteuler.net/problem=26
Sergey Lisitsin. May 2019
'''

def flattenlist(str):
    ''' This function takes a list of string elements and returns
    a single concatenated string'''

    result = ""
    for x in str:
        result=result+x
    return result

def periodpattern(div, num):
    '''This function implements the division algorithm
    it takes the divisor and numerator as arguments and
    returns a string with a string of digits, that
    represent the period of the result'''
    result = []
    remainders = []                     # A list of remainders to keep track of
    ind = 0                             # An index, representing a position in results
                                        # array from which the period starts
    divresult = None
    remainder = None
    while remainder is not 0:
        while (div * 10) < num:         # increasing the numerator to be able to divide
            div = div * 10
            result.append(str(0))
        while div < num:
            div = div * 10
        divresult = div // num
        remainder = div % num
        if remainder == 0:
            return(0)
        div = remainder
        if remainder in remainders:             # Checking if we had similar remainder previously
            ind = remainders.index(remainder)
            break
        result.append(str(divresult))
        remainders.append(remainder)
    return flattenlist(result[ind::])


results = {}
for x in range(1,1000):
    results[x]=periodpattern(1,x)

for x in range(1, 1000):
    print("{:10}, {:30}".format(x, results[x]))
