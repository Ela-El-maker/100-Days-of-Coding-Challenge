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

def insertionSort(array):
  