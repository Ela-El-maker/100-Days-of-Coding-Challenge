string1 = 'geeksforgeeks'

list1 = []

for x in string1 :
    if x in 'aeiou':
        list1.append(x)
print('Vowels : {}'.format(list1))

list = ['geeks','ide','cowrier','gfg']

list2 = []

for x in list:
    if x.startswith('g'):
        list2.append(x)

print("Start with G : {}".format(list2))
      

list3 = [x * 2 for x in range(6)]
print(list3)