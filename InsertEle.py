def insert_element(array, element, index):
    if index < 0 or index > len(array):
        raise ValueError("Index is out of bounds")

    array.insert(index, element)


array = [1, 2, 3, 4, 5]
element = 6  #element 
index = 2   #insert element position

insert_element(array, element, index)

print(array)