# Jump search: A searching algorithm that jumps over a fixed 
# number of elements in the array and then compares the target value with the next element.
# Method 2

#Jump Search 
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    return -1

# Example usage
sorted_numbers = [11, 25, 34, 50, 67, 72, 88]
target_number = 67

index = jump_search(sorted_numbers, target_number)

if index != -1:
    print(f"Element {target_number} found at index {index}.")
else:
    print(f"Element {target_number} not found.")

