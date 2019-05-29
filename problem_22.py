''' Solves problem # 22 on https://projecteuler.net
Sergey Lisitsin. May 2019
'''


def nametosum(name):
    name = name.lower()
    alf = 'abcdefghijklmnopqrstuvwxyz'
    result = 0
    for x in name:
        result = result + (alf.index(x) + 1)
    return result


with open('./names.txt') as file:
    content = file.read()
    content = content.replace('"', '')
    content = content.split(',')
    content.sort()
    newcontent = []
    result = 0
    for x in content:
        result = result + nametosum(x) * (content.index(x) + 1)

print(result)


