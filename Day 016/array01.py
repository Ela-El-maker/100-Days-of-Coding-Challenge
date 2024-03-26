print("How many elements do you want to stroe : - ", end="")

num = input()

arr =[]

print('\n Enter :- ',num,'Element:- ',end='')

num = int(num)

for i in range(num):
    element= input()
    arr.append(element)
print("\nThe array elements are :- ")
for i in range(num):
    print(arr[i],end='')