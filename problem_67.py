'''
This is a script that solves problem #18 on Project Euler
https://projecteuler.net/problem=67
Sergey Lisitsin. Jan 2020.
'''


def dataset():
    """
    this is a function's docstring
    """
    rows = []
    file = open('p067_triangle.txt','r')
    lines = file.readlines()
    for x in lines:
        p = x.replace('\n','').split()
        rows.append(p)
    return rows


def emptymatrix(h,w):
    """
    this function creates an empty matrix the
    same size as input one
    """
    emptyset = []
    for x in range(h):
        emptyset.append([0]*w)
    return emptyset


def extend(row, maximum):
    '''
    this is an extend function's doc string
    '''
    for _ in range(maximum - len(row)):
        row.append(0)


def expand(matrix):
    """
    this function expands matrix to square
    """
    for count in range(len(matrix)):
        matrix[count].append(0)
    return matrix


def mybest(myrow, mycolumn):
    """
    this function defines the best path to the
    row above current cell
    """
    if mycolumn > 0:
        above = emptyset[myrow - 1][mycolumn]
        aboveleft = emptyset[myrow - 1][mycolumn - 1]
    else:
        aboveleft = 0
        above = int(emptyset[myrow - 1][mycolumn])
    if int(above) > int(aboveleft):
        return int(myrows[myrow][mycolumn]) + int(above)
    else:
        return int(myrows[myrow][mycolumn]) + int(aboveleft)


if __name__ == '__main__':
    myrows = dataset()
    emptyset = emptymatrix(len(myrows),len(myrows[-1]))
    #print (emptyset)
    for row in myrows:
        extend(row, len(myrows[-1]))

    emptyset[0][0] = myrows[0][0]
    for x in range(1, len(myrows[-1])):
        for y in range(len(myrows)):
            #print(x,y)
            emptyset[x][y] = (mybest(x, y))
    for x in emptyset:
        print(x)
    u = emptyset[-1]
    u.sort()
    print ('The answer is {}'.format(u[-1]))
