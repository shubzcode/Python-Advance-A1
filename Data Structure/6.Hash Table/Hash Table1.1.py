class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash(self, key):
        return key % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        node = self.table[index]

        if node is None:
            self.table[index] = node(key, value)
        else:
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    break
                node = node.next

            if node.key != key:
                node.next = node(key, value)

    def get(self, key):
        index = self.hash(key)
        node = self.table[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None

# Example usage
if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert("John", 100)
    hash_table.insert("Jane", 200)
    hash_table.insert("Peter", 300)

    print("The value of John is", hash_table.get("John"))
    print("The value of Jane is", hash_table.get("Jane"))
    print("The value of Peter is", hash_table.get("Peter"))
