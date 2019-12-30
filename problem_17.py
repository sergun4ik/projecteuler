''' Solves problem #17 on https://projecteuler.net
Sergey Lisitsin. June 2019'''

def get_tail(num):
    output = 'and'
    startlist = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
    tenslist = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
    tail = str(num)[-2::]
    if tail == '00':
        return ''
    if len(str(num)) < 2:
        return startlist[(int(num))]
    if len(str(num)) == 2:
        output = ''
    if tail[-1] == '0':
        output = output + str(tenslist[(int(tail[0]))])
        return output
    if tail[0] == '0':
        output = output + str(startlist[(int(tail[1]))])
        return output
    if tail[0] == '1':
        output = output + str(startlist[int(tail)])
        return output
    if '0' not in tail:
        output = output + str(tenslist[(int(tail[0]))]) + str(startlist[(int(tail[1]))])
    return output

def get_hund(num):
    startlist = 'zero one two three four five six seven eight nine'.split()
    if len(str(num)) > 2:
        return startlist[int(str(num)[0])] + 'hundred'


def wordise(num):
    if get_hund(num):
        return get_hund(num)+get_tail(num)
    else:
        return get_tail(num)


master = ''
for x in range(1,1000):
    print(wordise(x))
    master = master + wordise(x)
master = master + 'onethousand'
print(len(master))
