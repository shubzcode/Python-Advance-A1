# A Python program that creates a stack of elements and then pushes and pops elements from the stack.
def push(stack, element):
    stack.append(element)


def pop(stack):
    return stack.pop()


def main():
    stack = []

    push(stack, 1)
    push(stack, 2)
    push(stack, 3)

    print("The top element of the stack is:", pop(stack))
    print("The stack now contains:", stack)


if __name__ == "__main__":
    main()
