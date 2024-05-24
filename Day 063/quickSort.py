# quickSort(int [] input, int left,int right){
#   if(right - left <= 0){
#     return 0
#   }
#   int pivot = input[(left+right) / 2];
#   int i = left, j = right,
#   while(i<=j){
#     while(input[i] < pivot)
#        i++
#     while(input[j] > pivot)
#        j--

#     if(i<=j){
#          swap input[i] & input[j]
#          i++
#          j--
#     }
#   }
#          //Recursive calls
#          quickSort(input,left,i-1)
#          quickSort(input,i,right)
# }



# Quick Sort in Python

# Function to partition the array on the  basis of pivot element
def partition (array,low,high):

  # Select the pivot element
  pivot = array[high]
  i = low -1

  # Put the elements smaller than pivot on the left and greater
  # than pivot on the right of pivot
  for j in range(low,high):
    if array[j] <= pivot:
      i = i + 1
      (array[i] ,array[j]) = (array[j], array[i])


  (array[i+1],array[high]) = (array[high],array[i+1])
  return i+1


def quickSort(array,low,high):
  if low= high:

  # Select pivot position and put all the elements smaller than the pivot on left and greater than the pivot in the right
  pi = partition(array,low,high)

  # Sort the elements on the left of the pivot
  quickSort(array,low,pi-1)
  # sort the elements on the right of the pivot
  quickSort(array,pi-1,high)


data = [1,2,9,7,2,4,76,4,8,43,8,3]
size =len(data)
quickSort(data,0,size -1)
print("Sorted Array : ")
print(data)