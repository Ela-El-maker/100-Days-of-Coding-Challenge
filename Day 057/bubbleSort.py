## Sorting Algorithm
## Bubble Sort
# for(index = 0 to input.length -1){
#   for(j = 0 to j < input.length -1 - index){
#     if(input[j] > input[j+1])
#       swap input[j+1] & input[j]
#   }
# }
# begin
# bubbleSort(array)
# for all the elements of the array 
# if(array[i] array[i+1])
# switch(array[i], array[i+1])
# end if
# end for 
# return array 
# end bubbleSort

def bubbleSort(array):
  n = len(array)
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        swapped = True
      if swapped == False:
        break

if __name__ == "__main__":
  array = [64,12,34,54,33,66,87,54]
  bubbleSort(array)
  print("Sorted array: ")
  for i in range(len(array)):
    print("%d" % array[i], end = "")