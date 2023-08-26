# A program that deletes an element from a binary search tree.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    
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

    print("Binary search tree before deletion:")
    inorder_traversal(root)
    
    key_to_delete = 15
    root = deleteNode(root, key_to_delete)
    
    print("\nBinary search tree after deleting", key_to_delete, ":")
    inorder_traversal(root)
