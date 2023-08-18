# Take user input for creating an array of numbers
input_numbers = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_numbers.split()]

# Take user input for the element to search
search_element = int(input("Enter the element to search: "))

# Linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # Element not found

# Perform linear search
index = linear_search(numbers, search_element)

if index != -1:
    print(f"Element {search_element} found at index {index}.")
else:
    print(f"Element {search_element} not found in the array.")
