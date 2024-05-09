def bubbleSort(array):

  # We create 2 loops:
  # 1. One loop is for iterating throughout the array.
  # 2. Second loop is for comparing the elements in the array.
  for  i in range(len(array)):
    for j in range(0, len(array) - i -1):
      # To sort in descending order:
      # You change > to < .
      if(array[j] > array[j+1]):
        # Then we swap 
        (array[j],array[j+1])=  (array[j+1],array[j])

data = [11,21,-1,-33,99]
bubbleSort(data)
print("Sorted array : ")
print(data)