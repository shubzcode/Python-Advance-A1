# A python program that evaluates a postfix expression using a stack.
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


def evaluate_postfix(expression):
    stack = Stack()
    operators = {"+", "-", "*", "/"}

    for token in expression:
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.push(result)

    return stack.pop()


def perform_operation(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


# Get input from the user
user_input = input("Enter a postfix expression (space-separated): ")
postfix_expression = user_input.split()

result = evaluate_postfix(postfix_expression)
print("Result:", result)
