### Linear Search Algorithm

# linearSearch(input, searchValue){
#   from typing import TypeVarTuple


# for(i = 0 to input.length -1){
#     if(input[i] == searchValue)
#       return True
#   }
#   return False
# }


## In Python
def linearSearch(input,searchValue):
  for i in range(0,len(input)):
    if input[i] == searchValue:
      return True
  return False

target = 88
array = [11,22,33,44,55,66,77,88,99]
print(linearSearch(array,target))



