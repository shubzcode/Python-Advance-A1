# A python program that sorts a queue using a queue.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def sort_queue(queue):
    sorted_queue = Queue()
    
    while not queue.is_empty():
        min_element = float('inf')
        min_index = -1
        size = queue.size()

        for i in range(size):
            current_element = queue.dequeue()
            if current_element < min_element:
                min_element = current_element
                min_index = i
            queue.enqueue(current_element)

        for i in range(size):
            current_element = queue.dequeue()
            if i != min_index:
                queue.enqueue(current_element)
            else:
                sorted_queue.enqueue(min_element)

    return sorted_queue


# Create a queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(30)
queue.enqueue(10)
queue.enqueue(50)
queue.enqueue(20)
queue.enqueue(40)

# Sort the queue
sorted_queue = sort_queue(queue)

# Print the sorted queue
print("Sorted queue:")
while not sorted_queue.is_empty():
    print(sorted_queue.dequeue())