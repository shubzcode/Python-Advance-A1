class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def delete_node(linked_list, data):
    if linked_list.head is None:
        return

    current_node = linked_list.head
    previous_node = None

    while current_node is not None:
        if current_node.data == data:
            if previous_node is None:
                linked_list.head = current_node.next
            else:
                previous_node.next = current_node.next
            break

        previous_node = current_node
        current_node = current_node.next


linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
linked_list.head.next = second_node
third_node = Node(3)
second_node.next = third_node

delete_node(linked_list, 2)

print(linked_list.head.data)
print(linked_list.head.next.data)
