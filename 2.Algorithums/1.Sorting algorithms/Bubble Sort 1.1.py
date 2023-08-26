# a Python program Bubble sort: A simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    bubble_sort(array)

    print("The sorted array is", array)


if __name__ == "__main__":
    main()
