# Linear search: A searching algorithm that compares each element of the array with
# the target value and returns the index of the first occurrence of the target value.
# Method 1
def linear_search(array, target):
    index = 0

    while index < len(array):
        if array[index] == target:
            return index

        index += 1

    return -1


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    target = 8

    index = linear_search(array, target)

    if index != -1:
        print("The target value is at index", index)
    else:
        print("The target value is not found")


if __name__ == "__main__":
    main()
