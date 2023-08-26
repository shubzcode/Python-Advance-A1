# A program that deletes an element from a binary search tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        # The node to be deleted is found
        # Case 1: The node has no child
        if root.left is None and root.right is None:
            return None

        # Case 2: The node has only one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: The node has two children
        # Find the inorder successor of the node to be deleted
        successor = find_inorder_successor(root.right)

        # Copy the data of the inorder successor to the node to be deleted
        root.data = successor.data

        # Delete the inorder successor
        root.right = delete(root.right, successor.data)

    return root

def find_inorder_successor(root):
    if root.left is None:
        return root

    return find_inorder_successor(root.left)

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("Inorder traversal of the tree before deletion:")
    print_inorder(root)

    root = delete(root, 10)

    print("Inorder traversal of the tree after deletion:")
    print_inorder(root)

def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.data)
        print_inorder(root.right)

if __name__ == "__main__":
    main()
