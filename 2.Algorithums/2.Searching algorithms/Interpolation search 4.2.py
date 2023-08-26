# Interpolation search: A searching algorithm that estimates the position of the target value in
# the array and then searches around that position.
# Method 2
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + int(
            ((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        )

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Example usage
sorted_numbers = [11, 25, 34, 50, 67, 72, 88]
target_number = 67

index = interpolation_search(sorted_numbers, target_number)

if index != -1:
    print(f"Element {target_number} found at index {index}.")
else:
    print(f"Element {target_number} not found.")
