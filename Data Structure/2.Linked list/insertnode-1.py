class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def insert_node(linked_list, data, position):
    if position < 0:
        raise ValueError("Position is out of bounds")

    if linked_list.head is None:
        new_node = Node(data)
        linked_list.head = new_node
        return

    current_node = linked_list.head
    for i in range(position - 1):
        if current_node.next is None:
            raise ValueError("Position is out of bounds")
        current_node = current_node.next

    new_node = Node(data)
    new_node.next = current_node.next
    current_node.next = new_node


linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
linked_list.head.next = second_node

insert_node(linked_list, 3, 1)

print(linked_list.head.data)
print(linked_list.head.next.data)
print(linked_list.head.next.next.data)
