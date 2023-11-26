class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List object"""

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """Add new element to the head of the data"""
        # Create a new node
        new_node = Node(new_data)
        # Move the head element of the list to next
        new_node.next = self.head
        # Setting a new node to the head of the list
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        """Append new element after exact element"""
        if prev_node is None:
            print("Node is not available")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        """Add new element to the end of the list"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        # Find the head of the list
        temp = self.head

        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None
