''' Solves problem #17 on https://projecteuler.net
Sergey Lisitsin. June 2019'''

one = len(list('one'))
two = len(list('two'))
three = len(list('three'))
four = len(list('four'))
five = len(list('five'))
six = len(list('six'))
seven = len(list('seven'))
eight = len(list('eight'))
nine = len(list('nine'))
ten = len(list('ten'))
eleven = len(list('eleven'))
twelve = len(list('twelve'))
thirteen = len(list('thirteen'))
fourteen = len(list('fourteen'))
fifteen = len(list('fifteen'))
sixteen = len(list('sixteen'))
seventeen = len(list('seventeen'))
eighteen = len(list('eighteen'))
nineteen = len(list('nineteen'))
twenty = len(list('twenty'))
thirty = len(list('thirty'))
fourty = len(list('forty'))
fifty = len(list('fifty'))
sixty = len(list('sixty'))
seventy = len(list('seventy'))
eighty = len(list('eighty'))
ninety = len(list('ninety'))

hundredcount = 999 - 99
andcount = 999 - 99 - 9
onecount = 100 + 99*9
twocount = 100 + 99*10
threecount = 100 + 99*10
fourcount = 100 + 99*10
fivecount = 100 + 99*10
sixcount = 100 + 99*10
sevencount = 100 +99*10
eightcount = 100 + 99*10
ninecount = 100+99*10
tencount = 10
elevencount = 10
twelvecount = 10
thirteencount = 10
fourteencount = 10
fifteencount = 10
sixteencount = 10
seventeencount = 10
eighteencount = 10
nineteencount = 10
twentycount = 10*10
thirtycount = 10*10
fourtycount = 10*10
fiftycount = 10*10
sixtycount = 10*10
seventycount = 10*10
eightycount = 10*10
ninetycount = 10*10


result = onecount*one+twocount*two+threecount*three+fourcount*four+fivecount*five+sixcount*six+sevencount\
    +sevencount*seven+eightcount*eight+ninecount*nine+tencount*ten+elevencount*eleven+twelvecount*twelve\
    +thirteencount*thirteen+fourteencount*fourteen+fifteencount*fifteen+sixteencount*sixteen+seventeencount*seventeen\
    +eighteencount*eighteen+nineteencount*nineteen+twentycount*twenty+thirtycount*thirty+fourtycount*fourty\
    +fiftycount*fifty+sixtycount*sixty+seventycount*seventy+eightycount*eighty+ninetycount*ninety
andcount = 999-99-9
print(result+andcount+11)