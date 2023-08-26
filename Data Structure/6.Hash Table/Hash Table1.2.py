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

# Example usage
if __name__ == "__main__":
    hash_table = HashTable(size=10)

    # Inserting elements into the hash table
    hash_table.insert("apple", 5)
    hash_table.insert("banana", 8)
    hash_table.insert("cherry", 12)
    # hash_table.insert("grape", 55)

    # Retrieving elements from the hash table
    print("Value for 'apple':", hash_table.retrieve("apple"))
    print("Value for 'banana':", hash_table.retrieve("banana"))
    print("Value for 'cherry':", hash_table.retrieve("cherry"))
    print("Value for 'grape':", hash_table.retrieve("grape"))
