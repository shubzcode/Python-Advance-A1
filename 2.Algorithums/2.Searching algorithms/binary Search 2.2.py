# Binary search: A searching algorithm that divides the array in half and recursively
# searches the half that contains the target value.
# Method 2
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Example usage
sorted_numbers = [11, 25, 34, 50, 67, 72, 88]
target_number = 67

index = binary_search(sorted_numbers, target_number)

if index != -1:
    print(f"Element {target_number} found at index {index}.")
else:
    print(f"Element {target_number} not found.")
