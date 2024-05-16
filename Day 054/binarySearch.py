# Binary Search algorithm
# binarySearch(input, searchValue){
#   lower =0
#   upper = upper.length -1

#   while(upper >= lower){
#     mid = (upper + lower)/2

#     if(input[mid] == searchValue)
#       return True
#     else if(searchValue < input[mid])
#       upper == mid -1
#     else
#       lower = mid + 1
#   }
# return False
# }

# def binarySearch(input, searchValue):
#   lower = 0
#   upper = len(input)

#   while(upper >= lower):
#     mid = (upper + lower) //2

#     if(input[mid] == searchValue):
#       return True
#     elif(searchValue < input[mid]):
#       upper = mid -1
#     else:
#       lower = mid +1
#   return False


# value = 55
# array = [11,22,10,32,34,56,31,89]
# print(binarySearch(array,value))
def binarySearch(input, searchValue):
  lower = 0
  upper = len(input) - 1

  while upper >= lower:
    mid = (upper + lower) // 2

    if input[mid] == searchValue:
      return True
    elif searchValue < input[mid]:
      upper = mid - 1
    else:
      lower = mid + 1
  return False

value = 56
array = [11, 22, 10, 32, 34, 56, 31, 89]
print(binarySearch(array, value))
