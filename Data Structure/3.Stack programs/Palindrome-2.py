# A  python program that checks if a string is a palindrome using a stack.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_palindrome(input_string):
    input_string = (
        input_string.lower()
    )  # Convert the string to lowercase for case-insensitivity
    stack = Stack()

    for char in input_string:
        if char.isalnum():  # Ignore non-alphanumeric characters
            stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string == input_string


# Get input from the user
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
