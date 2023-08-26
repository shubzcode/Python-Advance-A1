# A python program that sorts a queue using a queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)

    def sort(self):
        # Create a temporary queue to store the sorted elements.
        temp_queue = Queue()

        # While the original queue is not empty,
        # remove the first element from the original queue,
        # and add it to the temporary queue.
        while len(self.queue) > 0:
            temp_queue.enqueue(self.dequeue())

        # Transfer all the elements from the temporary queue to the original queue.
        for element in temp_queue.queue:
            self.enqueue(element)


def main():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.sort()

    print("The sorted queue is:")
    for element in queue.queue:
        print(element)


if __name__ == "__main__":
    main()
