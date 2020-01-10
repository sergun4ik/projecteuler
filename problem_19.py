''' Solves problem #19 on https://projecteuler.net
Sergey Lisitsin. Dec 2019'''
def weekday(day):
  while True:
    yield wikdays[day%7]
    day +=1

months = [31,28,31,30,31,30,31,31,30,31,30,31]
mths = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
wikdays = ['mon','tue','wed','thu','fri','sat','sun']
#wday = weekday(0)
sundays = 0

lmonth = 0
daycount = 0
wday = 0

for year in range(1900,2001):
    if year%4==0 and year != 1900:
        leap = 1
    else:
        leap = 0
    for month in mths:
        if month == 'feb':
            lmonth = months[mths.index(month)] + leap
        else:
            lmonth = months[mths.index(month)]
        for d in range(1, lmonth+1):
            day = next(weekday(daycount))
            if day == 'sun' and d == 1 and year > 1900:
                sundays += 1
            daycount+=1


print(sundays)