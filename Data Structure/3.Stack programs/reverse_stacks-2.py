# A python program that reverses a string using a stack.
def reverse_string(string):
    stack = []

    for char in string:
        stack.append(char)

    reversed_string = ""
    while len(stack) > 0:
        reversed_string += stack.pop()

    return reversed_string


def main():
    string = input("Enter a string: ")

    reversed_string = reverse_string(string)

    print("The reversed string is:", reversed_string)


if __name__ == "__main__":
    main()
