# A python program that prints the first n elements of a queue.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.pop(0)

    def print_first_n(self, n):
        for i in range(n):
            print(self.queue[i])


def main():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.print_first_n(4)


if __name__ == "__main__":
    main()