# The 3 Largest values in a list

def printLargest3(array):
  arrSize = len(array)
  # There should be at-least 3 elements
  if arrSize < 3:
    print("Invalid Input")

    return
  third = first = second = float('-inf')
  for i in range(arrSize):
    # If current element is greater than first
    if array[i] > first:
      third = second
      second = first
      first = array[i]
    elif array[i] > second and array[i] != first:
      third = second
      second = array[i]

    elif array[i] > third  and array[i] != second and array[i] != first:
      third = array[i]
      print("Three largest elements are : ",first,second,third)


array = [11,22,33,44,55,66,77,88,99]


printLargest3(array)