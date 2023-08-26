# Linear search: A searching algorithm that compares each element of the array with
# the target value and returns the index of the first occurrence of the target value.
# Method 2
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [3, 7, 1, 9, 5]
target_number = 6 # target value

index = linear_search(numbers, target_number)

if index != -1:
    print(f"Element {target_number} found at index {index}.")
else:
    print(f"Element {target_number} not found.")
