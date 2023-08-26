# A program that evaluates a postfix expression using a stack.
def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = do_operation(token, operand1, operand2)
            stack.append(result)

    return stack.pop()


def do_operation(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


def main():
    expression = input("Enter a postfix expression: ")

    result = evaluate_postfix(expression)

    print("The result of the expression is:", result)


if __name__ == "__main__":
    main()