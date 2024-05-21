# for (i = 0 to i = input.length -1){
#   int temp = input[i]
#   boolean hasMoved = False
#   boolean notPlaced = True

#   for(j =i to j = 0){
#     if(input[j] > temp){
#       // Shift numbers till you find          // it's right location
#       input[j+1] = input[j]
#       hasMoved = True
      
#     }else{
#       input[j+1]= temp
#       notPlaced = False 
#       break;
#     }
#   }

#   // Edge case
#   if(hasMoved  && notPlaced)
#   input[0] = temp
# }
### insertion sort algorithm

# def insertionSort(array):
#   for i in range(len(array)):
#     temp = array[i]
#     hasMoved = False
#     notPlaced = True 
#     j = i - 1

#     while j>= 0 and temp < array[j]:
#       array[j+1] = array[j]
#       hasMoved = True
#       j -= 1

#     array[j+1] = temp 

# array = [90,2,3,32,57,2122,767,43323,799]
# print(insertionSort(array))


def insertionSort(arr):
  for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key

# Test the insertionSort function
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array:", arr)
  