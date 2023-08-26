# A python program that sorts a list of elements using a hash table.
# Method 2
def hash_sort(arr):
    # Find the range of elements in the array
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    # Create empty buckets
    buckets = [[] for _ in range(range_val)]

    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)

    # Sort elements within each bucket
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


# Example usage
if __name__ == "__main__":
    unsorted_list = [42, 10, 7, 23, 32, 16, 5, 19]
    sorted_list = hash_sort(unsorted_list)

    print("Unsorted list:", unsorted_list)
    print("Sorted list:", sorted_list)
