# Selection sort: A sorting algorithm that repeatedly selects the smallest
# element from the unsorted part of the array and moves it to the sorted part.
# Method 2
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

selection_sort(numbers)
print("Sorted array using Selection Sort:", numbers)