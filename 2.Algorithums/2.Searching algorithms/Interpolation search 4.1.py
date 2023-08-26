# Interpolation search: A searching algorithm that estimates the position of the target value in 
# the array and then searches around that position.
# Method 1
def interpolation_search(array, target):
    n = len(array)
    
    low = 0
    high = n - 1

    while low <= high:
        mid = low + int((high - low) * (target - array[low]) / (array[high] - array[low]))

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

    index = interpolation_search(array, target)

    if index != -1:
        print("The target value is at index", index)
    else:
        print("The target value is not found")


if __name__ == "__main__":
    main()
