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