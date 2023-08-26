# A python program that finds the maximum element in a queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)

    def find_max(self):
        max_element = self.queue[0]
        for element in self.queue:
            if element > max_element:
                max_element = element
        return max_element


def main():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(8)
    queue.enqueue(4)
    queue.enqueue(5)

    print("The maximum element in the queue is:", queue.find_max())


if __name__ == "__main__":
    main()
