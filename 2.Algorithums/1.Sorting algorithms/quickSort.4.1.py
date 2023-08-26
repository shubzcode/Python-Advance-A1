# Quicksort: A sorting algorithm that chooses a pivot element
# and partitions the array around the pivot element.
# Method 1
def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    quicksort(array, 0, len(array) - 1)

    print("The sorted array is", array)


if __name__ == "__main__":
    main()
