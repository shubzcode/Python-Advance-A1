# A Python program that checks if a string is a palindrome using a stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to the stack")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty, cannot pop")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Create a stack
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Pop elements from the stack
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())  # Trying to pop from an empty stack

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())
