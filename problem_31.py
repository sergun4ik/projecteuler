''' Solves problem #31 on https://projecteuler.net
Sergey Lisitsin. Jan 2020'''



combs = []
for pence in range(201):
    for twopence in range(101):
        for fivepence in range(41):
            for tenpence in range(21):
                for twentypence in range(11):
                    for fiftypence in range(5):
                        for pound in range(3):
                            #print(pence)
                            if pence + (twopence*2) \
                                + (fivepence * 5) \
                                + (tenpence * 10) \
                                + (twentypence * 20) \
                                + (fiftypence * 50) \
                                + (pound * 100) == 200:
                                  combs.append((pence,twopence,fivepence,tenpence, \
                                                twentypence, fiftypence, pound))
                                  print(len(combs))

print(len(combs)+1)
