# A python program that finds the most frequent word in a text file using a hash table.
import string

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

def most_frequent_word(filename):
    hash_table = HashTable(size=1000)

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                cleaned_word = word.strip(string.punctuation).lower()
                if cleaned_word:
                    if hash_table.retrieve(cleaned_word) is None:
                        hash_table.insert(cleaned_word, 1)
                    else:
                        hash_table.insert(cleaned_word, hash_table.retrieve(cleaned_word) + 1)

    max_word = None
    max_frequency = 0
    for key in hash_table.table:
        if key is not None:
            for stored_key, value in key:
                if value > max_frequency:
                    max_frequency = value
                    max_word = stored_key

    return max_word, max_frequency

# Example usage
if __name__ == "__main__":
    filename = "sample.txt"  # Replace with the path to your text file
    most_frequent, frequency = most_frequent_word(filename)
    
    if most_frequent:
        print("Most frequent word:", most_frequent)
        print("Frequency:", frequency)
    else:
        print("No words found in the file.")
