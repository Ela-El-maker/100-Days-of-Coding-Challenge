def swap():
  value1 = 3
  value2 =4
  value3 = 5
  tempValue = 0
  tempValue = value1
  value1 = value2
  value2 = tempValue
  print(value1)
  print(value2)
def letSwap(array):
  newArray = []
  for i in range(len(array)):
    # print(f"First element {array[i]}")
    # print(f"Second element {array[i+1]}")
    if (array[i] < array[i+1]):
      temp = array[i]
      array[i] = array[i+1]
      array[i+1] = temp
    newArray.append(array[i])
    
  for i in range(len(newArray)):
    print(newArray[i])

array = [11,33,66,77,4,33,22,55,73]
letSwap(array)
  