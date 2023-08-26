# A program that checks if a string is a palindrome using a hash table.
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def retrieve(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for stored_key, value in self.table[index]:
                if stored_key == key:
                    return value
        return None


def is_palindrome(s):
    hash_table = HashTable(size=len(s))

    for char in s:
        if char.isalnum():
            char_lower = char.lower()
            if hash_table.retrieve(char_lower) is None:
                hash_table.insert(char_lower, 1)
            else:
                hash_table.insert(char_lower, hash_table.retrieve(char_lower) + 1)

    odd_count = 0
    for key in hash_table.table:
        if key is not None:
            for _, value in key:
                if value % 2 == 1:
                    odd_count += 1

    return odd_count <= 1


# Example usage
if __name__ == "__main__":
    test_strings = [
        "racecar",
        "hello",
        "A man, a plan, a canal, Panama",
        "not a palindrome",
    ]

    for s in test_strings:
        is_pal = is_palindrome(s)
        print(f"'{s}' is a palindrome:", is_pal)
