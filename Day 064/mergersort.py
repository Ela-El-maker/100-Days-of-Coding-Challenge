## Merge Sort Algorithm
sort(input,left,right){
  if(left<right){
    int mid = (left+right)/2
    sort(input,left,mid)
    sort(input, mid+1,right)
    //Sort & merge the sorted halves
    merge(input,left,mid,right)
  }
}

merge(input,left,mid,right){
  int len1 = mid-left +1
  int len2 = right - mid

  L -> array of size len1 
  R -> array of size len2 

  // copy data to these arrays
  for (i=0 to i<len1)
  L[i] = input[left+i]

  for (i=0 to i<len2)
  R[i] = input[mid +i +1]

int i =0, j = 0, k = left
while (i<len1 && j<len2){
  if(L[i] <= R[j]){
    input[k] - L[i]
  i++
  
  }else{

  input[k] = R[j]
j++
  }
k++
}

// Fill the remaining numbers
  while(i<len1){
    input[k] = L[i]
i++
k++
  }
  while(j<len2){
    input[k]= R[j]
j++
k++
  }
}