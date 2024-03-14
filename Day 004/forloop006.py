list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

found = False
for element in list1:
    if element in list2:
        found = True
        break

print(found)
