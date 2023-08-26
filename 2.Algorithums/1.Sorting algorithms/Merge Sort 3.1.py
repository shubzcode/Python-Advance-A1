# Merge sort: A sorting algorithm that divides the array into two
# halves and recursively sorts the two halves
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    sorted_array = merge_sort(array)

    print("The sorted array is", sorted_array)


if __name__ == "__main__":
    main()
