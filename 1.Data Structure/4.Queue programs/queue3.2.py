# A python program that finds the maximum element in a queue.
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


def find_max_in_queue(queue):
    if queue.is_empty():
        return None

    max_element = queue.dequeue()
    while not queue.is_empty():
        current_element = queue.dequeue()
        if current_element > max_element:
            max_element = current_element

    return max_element


# Create a queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(30)
queue.enqueue(90)
queue.enqueue(50)
queue.enqueue(40)

# Find and print the maximum element in the queue
max_element = find_max_in_queue(queue)
if max_element is not None:
    print("Maximum element in the queue:", max_element)
else:
    print("Queue is empty.")
