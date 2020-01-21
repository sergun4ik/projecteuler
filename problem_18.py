'''
This is a script that solves problem #18 on Project Euler
https://projecteuler.net/problem=18
Sergey Lisitsin. 2017.
'''


def dataset():
    """
    this is a function's docstring
    """
    row0 = [75]
    row1 = [95, 64]
    row2 = [17, 47, 82]
    row3 = [18, 35, 87, 10]
    row4 = [20, 4, 82, 47, 65]
    row5 = [19, 1, 23, 75, 3, 34]
    row6 = [88, 2, 77, 73, 7, 63, 67]
    row7 = [99, 65, 4, 28, 6, 16, 70, 92]
    row8 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
    row9 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
    row10 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
    row11 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
    row12 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
    row13 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
    row14 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    rows = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,\
           row12,row13,row14]
    return rows


def emptymatrix(size):
    """
    this function creates an empty matrix the
    same size as input one
    """
    emptyset = []
    for x in range(size):
        emptyset.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
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
        above = emptyset[myrow-1][mycolumn]
        aboveleft = emptyset[myrow-1][mycolumn - 1]
    else:
        aboveleft = 0
        above = emptyset[myrow-1][mycolumn]
    if above > aboveleft:
        return myrows[myrow][mycolumn] + above
    else:
        return myrows[myrow][mycolumn] + aboveleft

if __name__ == '__main__':
    myrows = dataset()
    emptyset = emptymatrix(15)
    for row in myrows:
        extend(row, 15)
   
    emptyset[0][0] = myrows[0][0]
    for x in range(1, 15):
        for y in range(15):
            emptyset[x][y] = ( mybest(x,y) )
    for x in emptyset:
        print(x)
