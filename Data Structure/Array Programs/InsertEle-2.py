# Take user input for creating an array of numbers
input_numbers = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_numbers.split()]

# Take user input for the element to insert
insert_element = int(input("Enter the element to insert: "))

# Take user input for the index to insert the element
insert_index = int(input("Enter the index to insert the element: "))

# Insertion into an array
def insert_into_array(arr, element, index):
    arr.insert(index, element)

# Perform insertion
insert_into_array(numbers, insert_element, insert_index)

print("Array after insertion:", numbers)