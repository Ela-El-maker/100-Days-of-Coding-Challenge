def linearSearch(array,n,x):
  for i in range(0,n):
    if array[i] == x:
      return i
    return -1
  

array =[11,22,33,44,55,66]
x = 44
n = len(array)
result = linearSearch(array,n,x)
if result == -1:
  print("Element not found")
else:
  print("Element found at index : ",result)