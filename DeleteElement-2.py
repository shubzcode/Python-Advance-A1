# Take user input for creating an array of numbers
input_numbers = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_numbers.split()]

# Take user input for the element to delete
delete_element = int(input("Enter the element to delete: "))

# Deletion from an array
def delete_from_array(arr, element):
    if element in arr:
        arr.remove(element)

# Perform deletion
delete_from_array(numbers, delete_element)

print("Array after deletion:", numbers)