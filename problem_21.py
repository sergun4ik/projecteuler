def factorsum(num):
    ''' Returns a list of factors '''
    factors = [1]
    half = (num // 2) + 1
    for x in range(2, half):
        if num % x == 0:
            factors.append(x)
    # factors.append(num)
    return (sum(factors))


dict = list(range(10000))
for x in range(10000):
    dict[x] = factorsum(x)

result = []
for x in dict:
    if x < 10000 and dict[x] < 10000:
        print("x is {}".format(x))
        if dict.index(dict[x]) == dict[dict[x]] and dict[x] != dict[dict[x]]:
            print("current pair is {} {}".format(dict[x], dict[dict[x]]))
            result.append(dict[dict[x]])
            result.append(dict[x])

sum(set(result))