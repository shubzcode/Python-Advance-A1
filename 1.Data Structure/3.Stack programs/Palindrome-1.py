# A  python program that checks if a string is a palindrome using a stack.
def is_palindrome(string):
    stack = []

    for char in string:
        stack.append(char)

    while len(stack) > 1:
        top_element = stack.pop()
        bottom_element = stack.pop(0)

        if top_element != bottom_element:
            return False

    return True


def main():
    string = input("Enter a string: ")

    if is_palindrome(string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()
