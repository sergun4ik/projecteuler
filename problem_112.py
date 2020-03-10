''' Solves problem # 112 on https://projecteuler.net
Sergey Lisitsin. Mar 2020
'''

def num_type(num):
    decreasing = True
    increasing = True
    bouncy = True
    strnum = str(num)
    for x in range(len(strnum)-1):
        if strnum[x]>strnum[x+1]:
            increasing = False
        if strnum[x]<strnum[x+1]:
            decreasing = False
    if increasing:
        return ("increasing")
    if decreasing:
        return ("decreasing")
    else:
        return ("bouncy")

numbers = 101
bouncy = 1

while bouncy/numbers < 0.99:
    numbers+=1
    if num_type(numbers) == 'bouncy':
        bouncy += 1

print(numbers)