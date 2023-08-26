# A python program that finds the minimum and maximum elements in a binary search tree.
# Method 1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right
    return current

def findMinMax(root):
    if root is None:
        return (None, None)

    minNode = minValueNode(root)
    maxNode = maxValueNode(root)

    return (minNode.data, maxNode.data)

# Example usage
if __name__ == "__main__":
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.right = Node(25)

    (minValue, maxValue) = findMinMax(root)
    print("The minimum value in the tree is", minValue)
    print("The maximum value in the tree is", maxValue)
