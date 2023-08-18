def delete_element(array, index):
    if index < 0 or index >= len(array):
        raise ValueError("Index is out of bounds")

    for i in range(index, len(array) - 1):
        array[i] = array[i + 1]

    array.pop()


array = [1, 2, 3, 4, 5]
index = 2

delete_element(array, index)

print(array)