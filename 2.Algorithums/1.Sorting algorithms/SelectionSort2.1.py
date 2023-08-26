    # * Selection sort: A sorting algorithm that repeatedly selects the smallest
    # element from the unsorted part of the array and moves it to the sorted part.

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    selection_sort(array)

    print("The sorted array is", array)


if __name__ == "__main__":
    main()
