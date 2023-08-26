# A python program that creates a binary search tree of elements and then searches for an element in the tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def search(self, data):
        current_node = self.root

        while current_node is not None:
            if data == current_node.data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False


def main():
    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(19)


    print("Is 10 in the tree?:", bst.search(10))
    print("Is 15 in the tree?:", bst.search(15))
    print("Is 20 in the tree?:", bst.search(20))


if __name__ == "__main__":
    main()
