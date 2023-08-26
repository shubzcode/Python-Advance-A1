# Create an array of numbers
numbers = [5, 2, 9, 1, 5, 6, 8] # list 

# Sorting using the built-in sorted() function
sorted_numbers_builtin = sorted(numbers)
print("Sorted using built-in sorted():", sorted_numbers_builtin)

# Bubble Sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Create a new array for Bubble Sort
numbers_bubble_sort = [5, 2, 9, 1, 5, 6, 7]
bubble_sort(numbers_bubble_sort)
print("Sorted using Bubble Sort:", numbers_bubble_sort)
