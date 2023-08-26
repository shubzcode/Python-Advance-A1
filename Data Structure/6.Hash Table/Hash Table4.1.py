# A python program that sorts a list of elements using a hash table.
def sort_list(list):
    hash_table = {}

    for i in range(len(list)):
        hash_table[list[i]] = i

    sorted_list = []

    for key in hash_table.keys():
        sorted_list.append(key)

    return sorted_list


def main():
    list = [10, 2, 5, 3, 1, 9, 8, 7, 6, 4]

    sorted_list = sort_list(list)

    print("The sorted list is", sorted_list)


if __name__ == "__main__":
    main()
