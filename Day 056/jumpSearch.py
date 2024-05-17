## Jump Search algorithm
# jumpSearch(input,searchValue){
# n = input.length
# jumpBy = Math.floor(Math.sqrt(n))
# blockStart = 0
# blockEnd jumpBy

# # Look for the correct block
# while(input[blockEnd] <= searchValue){
# blockStart = blockEnd
# blockEnd += jumpBy
# if(blockEnd > = n)
# blockend = n-1
# # No block suitable, hence not found
# if(blockStart >= n)
# return False
# }
# # Now do a linear search inside the block
# for(i = blockStart to  i = blockEnd){
#   if (input[i] == searchValue)
# return True

# }
# return False
# }
import Math

def jumpSearch(input, searchValue):
  n = len(input)
  jumpBy = Math.floor(Math.sqrt(n))

  blockStart = 0
  blockEnd = jumpBy

  # Look for the correct block

  while(input[blockEnd] <= searchValue):
    blockStart = blockEnd
    blockEnd += jumpBy

    if blockEnd >= n:
      blockEnd = n -1

#  No block suitable ,hence not found
    if(blockStart >= n):
      return False

  for i in range(blockStart, min(blockEnd,n)):
    if(input[i]==searchValue):
      return True
  return False