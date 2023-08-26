# Quicksort: A sorting algorithm that chooses a pivot element and 
# partitions the array around the pivot element.
# method 2 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

sorted_array = quick_sort(numbers)
print("Sorted array using QuickSort:", sorted_array)
