# A python program that inserts an element into a binary search tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def main():
    root = None
    root = insert(root, 10)
    root = insert(root, 5)
    root = insert(root, 15)
    root = insert(root, 2)
    root = insert(root, 7)

    print("Inorder traversal of the tree:")
    print_inorder(root)


def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.data)
        print_inorder(root.right)


if __name__ == "__main__":
    main()
