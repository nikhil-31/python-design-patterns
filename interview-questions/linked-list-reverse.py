"""
Python interview question

- Reverse a singly linked list

"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


linked_list = LinkedList()
linked_list.push(20)
linked_list.push(4)
linked_list.push(15)
linked_list.push(85)

print("Linked list ")
linked_list.print_list()

linked_list.reverse()

print("Reversed list")
linked_list.print_list()