''' Solves problem # 345 on https://projecteuler.net
Sergey Lisitsin. Jan 2020
'''

matrix = '''7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805'''

nummatrix = []
for x in matrix.split('\n'):
    nummatrix.append(x.split())
result = 0

champs = []
champx = []
champy = []

current_biggest = 0
for x in nummatrix:
    print(x)

def is_unique(number):
    coordinatesx = []
    coordinatesy = []
    for x in range(len(nummatrix)):
        for y in range(len(nummatrix[x])):
            if nummatrix[x][y] == number:
                coordinatesx.append(x)
                coordinatesy.append(y)
    if len(coordinatesx) > len(set(coordinatesx)) or len(coordinatesy) > len(set(coordinatesy)):
        return False
    else:
        return True


def find_largest():
    largest = 0
    coordinates = 0,0
    for x in range(len(nummatrix)):
        for y in range(len(nummatrix[x])):
            if int(nummatrix[x][y]) >= largest:
                if is_unique(nummatrix[x][y]):
                    largest = int(nummatrix[x][y])
                    coordinates = x,y
    return(largest,*coordinates)

def zeroize(x,y):
    for a in range(len(nummatrix)):
        for b in range(len(nummatrix[a])):
           if a == x or b == y:
               nummatrix[a][b] = 0


def gain_loss(x,y):
    gain = int(nummatrix[x][y])
    loss =  0
    for a in range(len(nummatrix)):
        for b in range(len(nummatrix[a])):
            if a == x or b ==y:
                loss+=int(nummatrix[a][b])
    return gain, loss-gain, gain/loss


while find_largest()[0] > 0:
    k = find_largest()
    print(k)
    result += k[0]
    zeroize(k[1],k[2])

print(result)
