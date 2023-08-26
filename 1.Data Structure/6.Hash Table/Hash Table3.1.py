# A python program that finds the most frequent word in a text file using a hash table.
def most_frequent_word(filename):
    hash_table = {}

    with open(filename, "r") as f:
        for line in f:
            words = line.split()

            for word in words:
                if word in hash_table:
                    hash_table[word] += 1
                else:
                    hash_table[word] = 1

    most_frequent_word = None
    most_frequent_count = 0

    for word, count in hash_table.items():
        if count > most_frequent_count:
            most_frequent_word = word
            most_frequent_count = count

    return most_frequent_word


def main():
    filename = input("Enter the name of the text file: ")

    most_frequent_word = most_frequent_word(filename)

    print("The most frequent word in the text file is", most_frequent_word)


if __name__ == "__main__":
    main()
