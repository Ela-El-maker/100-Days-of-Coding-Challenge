def counting_sort_for_radix(arr, exp):
  n = len(arr)
  output = [0] * n
  count = [0] * 10  # Since the base is 10

  # Count occurrences of each digit
  for i in range(n):
      index = arr[i] // exp
      count[index % 10] += 1

  # Update count[i] so that it contains the actual position of this digit in output[]
  for i in range(1, 10):
      count[i] += count[i - 1]

  # Build the output array
  i = n - 1
  while i >= 0:
      index = arr[i] // exp
      output[count[index % 10] - 1] = arr[i]
      count[index % 10] -= 1
      i -= 1

  # Copy the output array to arr[], so that arr now contains sorted numbers
  for i in range(n):
      arr[i] = output[i]

def radix_sort(arr):
  # Find the maximum number to know the number of digits
  max_num = max(arr)

  # Apply counting sort to sort elements based on place value
  exp = 1
  while max_num // exp > 0:
      counting_sort_for_radix(arr, exp)
      exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array is:", arr)
