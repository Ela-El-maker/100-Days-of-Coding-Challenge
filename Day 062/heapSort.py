# # Heap Sort Algorithm
# # sort(){
# int size = input.length
# for(int i = size/2-1 to 0){
#   heapify(size,i)
#   for (int i = size -1 to 0){
#     swap input[i] & input[0]
#        heapify(i,0)
#   }
# }

#     heapify(int n int i){
#     int largest = i
#     int left = 2i + 1
#       int right = 2i +2
#          // If left child is larger than root
#          if(left < n && input[largest] < input[left])
#          largest = left

#         // If right child is largest than largest found 
#         if(right < n && input[largest] < input[right])
#         largest = right 

#         // If the largest element is not root
#         if(largest != i){
#           swap input[i] & input[largest]
#           heapify(n,largest)
        
#     }
# }


# Heap Sort algorithm in Python
def heapify(array, n ,i):
  # Find the largest among root and children
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and array[i] < array[1]:
    largest = 1

  if r < n and array[largest] < array[r]:
    largest = r 

  # Root is not largest, Swap with largest and continue heapifying
  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    heapify(array, n ,i)


def heapSort(array):
  n = len(array)

  # Build max heap
  for i in range(n//2, -1, -1):
    heapify(array,n ,i)

  for i in range(n-1,0,-1):
    # Swap

    array[i], array[0] = array[0],array[i]

    # Heapify root element
    heapify(array,i,0)

array = [1,12,9,5,3,20]
heapSort(array)

n = len(array)
print("Sorted Array: ")
for i in range(n):
  print("%d", % array[i],end="")