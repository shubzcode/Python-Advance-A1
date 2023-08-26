# A program that creates a queue of elements and then enqueues and dequeues elements from the queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)


def main():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("The first element in the queue is:", queue.dequeue())
    print("The second element in the queue is:", queue.dequeue())
    print("The third element in the queue is:", queue.dequeue())


if __name__ == "__main__":
    main()
