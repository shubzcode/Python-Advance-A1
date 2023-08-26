# a Python program Bubble sort: A simple sorting algorithm that repeatedly compares 
# adjacent elements and swaps them if they are in the wrong order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers)

bubble_sort(numbers)
print("Sorted array using Bubble Sort:", numbers)
