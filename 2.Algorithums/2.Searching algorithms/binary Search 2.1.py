# Binary search: A searching algorithm that divides the array in half and recursively 
# searches the half that contains the target value.
#Method 1 
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


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    target = 5

    index = binary_search(array, target)

    if index != -1:
        print("The target value is at index", index)
    else:
        print("The target value is not found")


if __name__ == "__main__":
    main()
