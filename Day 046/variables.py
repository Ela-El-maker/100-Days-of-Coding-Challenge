# Binary Search in Python
# Recursive Binary Search
def binarySearch(array, x, low, high):
  if high >= low:
    mid = low + (high - low) // 2

    #  if found at mid , then return it
    if array[mid] == x:
      return mid
    # Search the left half
    elif array[mid] > x:
      return binarySearch(array,x,low,mid-1)


    # Search the right half
    else:
      return binarySearch(array,x,mid+1,high)

  else:
    return -1

array = [1,2,3,4,5,6,7,8,9,0]
x=5

result = binarySearch(array,x,0,len(array) -1)


if result != -1:
  print("Element fount at index : "+ str(result))

else:
  print("Not found")