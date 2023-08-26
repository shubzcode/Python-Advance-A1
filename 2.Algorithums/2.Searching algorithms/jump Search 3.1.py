# Jump search: A searching algorithm that jumps over a fixed 
# number of elements in the array and then compares the target value with the next element.
# Method 1
def jump_search(array, target):
    n = len(array)
    step = int(n ** 0.5)

    prev = 0
    curr = step

    while curr < n:
        if array[curr] <= target:
            prev = curr
            curr += step
        else:
            break

    if curr < n and array[curr] == target:
        return curr
    else:
        return -1


def main():
    array = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    target = 4

    index = jump_search(array, target)

    if index != -1:
        print("The target value is at index", index)
    else:
        print("The target value is not found")


if __name__ == "__main__":
    main()
