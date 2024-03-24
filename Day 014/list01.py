def getSmaller(listValues, target):
    return [
        e 
        for e in listValues if e < target
    ]

listValues = [9,15,14,22,11,33,44,55]

target = 20

print(getSmaller(listValues, target))