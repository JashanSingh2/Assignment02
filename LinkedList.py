#Made By: Jashan Singh

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete_node(self, n):
        if not self.head:
            raise ValueError("Cannot delete node from an empty list")

        if n < 1:
            raise ValueError("Index out of range")

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        current_index = 1

        while current and current.next:
            if current_index + 1 == n:
                current.next = current.next.next
                return
            current = current.next
            current_index += 1

        raise ValueError("Index out of range")

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Linked List:")
linked_list.print_list()

linked_list.delete_node(3)

print("Linked List after deletion:")
linked_list.print_list()

try:
    linked_list.delete_node(10)
except ValueError as e:
    print(e)

try:
    empty_list = LinkedList()
    empty_list.delete_node(1)
except ValueError as e:
    print(e)
