def getEvenOdd(list):
    even = [x for x in list if x % 2 == 0]
    odd = [x for x in list if x % 2 != 0]

    return even,odd


list = [11,22,33,44,55,66,77,88]

even,odd = getEvenOdd(list)

print('Even : {}'.format(even))

print('Odd : {}'.format(odd))