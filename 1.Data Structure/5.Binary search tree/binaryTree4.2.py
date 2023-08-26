# A python program that finds the minimum and maximum elements in a binary search tree.
# Method 2
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.val

def find_max(root):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Example usage
if __name__ == "__main__":
    root = TreeNode(15)
    root.left = TreeNode(10)
    root.right = TreeNode(20)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(12)
    root.right.left = TreeNode(17)
    root.right.right = TreeNode(25)

    min_value = find_min(root)
    max_value = find_max(root)

    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
