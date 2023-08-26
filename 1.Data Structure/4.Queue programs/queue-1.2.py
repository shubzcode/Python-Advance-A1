class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} to the queue")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty, cannot dequeue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Create a queue
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Dequeue elements from the queue
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())  # Trying to dequeue from an empty queue

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())
