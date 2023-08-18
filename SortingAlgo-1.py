def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(array)
print(array)
