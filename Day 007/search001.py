def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1
    found = False
    
    while start <= end:
        mid = int((start + end) / 2)
        
        if numbers[mid] == target:
            found = True
            break
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    if found:
        print("Found")
    else:
        print("Not found")

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
binary_search(numbers, target)

