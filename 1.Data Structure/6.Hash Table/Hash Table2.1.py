# A program that checks if a string is a palindrome using a hash table.
def is_palindrome(string):
    hash_table = {}

    for i in range(len(string)):
        hash_table[string[i]] = i

    for i in range(len(string) // 2):
        if string[i] not in hash_table or hash_table[string[i]] != len(string) - i - 1:
            return False

    return True


def main():
    string = input("Enter a string: ")

    if is_palindrome(string):
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


if __name__ == "__main__":
    main()
