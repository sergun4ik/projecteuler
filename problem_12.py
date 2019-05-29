def factors(num):
    ''' Returns a list of factors '''
    factors = [1]
    half = (num // 2) + 1
    for x in range(2, half):
        if num % x == 0:
            factors.append(x)
    factors.append(num)
    return (factors)


def halve(list):
    ''' halves every even number in a list '''
    result = []
    for x in list:
        if x % 2 == 0:
            result.append(x / 2)
        else:
            result.append(x)
    return result


def jointfactors(num1, num2):
    ''' Returns a list of factors of two given numbers
    divided by 2 '''
    result = []
    if num1 % 2 == 0:
        num1factors = halve(factors(num1))
        num2factors = factors(num2)
    else:
        num2factors = halve(factors(num2))
        num1factors = factors(num1)
    for x in num1factors:
        for y in num2factors:
            result.append(x * y)
    return (set(result))


winner = 0
counter = 1
while winner < 501:
    number = counter
    next = counter + 1
    if len(jointfactors(number, next)) < 501:
        counter = counter + 1
    else:
        winner = counter

print(winner * (winner + 1) / 2)