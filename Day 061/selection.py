## Selection Sort Algorithm


# Adds sorted numbers to the right end of the array
# for(i = input.length-1 to i > 0){
#   int maxIndex = 0;
#   for (j = i to j <= i){
#     if(input[j] > input[maxIndex]){
#       # Set index for largest element found till now
#       maxIndex = j;
      
#     }
#   }
#   if(maxIndex != i){
#     swap input[i] & input[maxIndex]
#   }
# }

def selectionSort(array,size):
  for step in range(size):
    minIndex = step 

    for i in range(step + 1, size):
      # select the minimum element in each loop
      if array[i] < array[minIndex]:
        minIndex = i 

    (array[step],array[minIndex]) = (array[minIndex], array[step])


data = [-2,45,0,11,44,22,33,9]
size = len(data)
selectionSort(data,size)

print("Sorted Array : ")
print(data)
      