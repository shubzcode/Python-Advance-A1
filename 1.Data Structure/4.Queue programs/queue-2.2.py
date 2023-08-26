# A python program that prints the first n elements of a queue.
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


def print_first_n_elements(queue, n):
    if n <= 0:
        return

    for _ in range(n):
        if not queue.is_empty():
            print(queue.dequeue())
        else:
            print("Queue is empty.")
            break


# Create a queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Print the first 3 elements
print("Printing the first 3 elements:")
print_first_n_elements(queue, 4)
