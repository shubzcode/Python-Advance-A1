# A python program that inserts an element into a binary search tree.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    root = None
    keys = [15, 10, 20, 8, 12, 17, 25]

    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of the binary search tree:")
    inorder_traversal(root)
