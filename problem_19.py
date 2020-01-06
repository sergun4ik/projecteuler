''' Solves problem #19 on https://projecteuler.net
Sergey Lisitsin. Dec 2019'''

years=list(range(1901,2001))
months=[1,2,3,4,5,6,7,8,9,10,11,12]
normaldaycount = [31,28,31,30,31,30,31,31,30,31,30,31]
leapdaycount =  [31,29,31,30,31,30,31,31,30,31,30,31]
weekdays = [1,2,3,4,5,6,7]

day = 1
result = 0
while day < 36500:
