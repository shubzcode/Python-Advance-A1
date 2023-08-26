def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2

index = binary_search(array, target)

if index != -1:
    print("The element is found at index", index)
else:
    print("The element is not found")
