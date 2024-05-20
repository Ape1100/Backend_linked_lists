class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            if current_node.next:
                current_node.next.prev = None
            self.head = current_node.next
            current_node = None
            return
        while current_node and current_node.data != key:
            current_node = current_node.next
        if current_node is None:
            return
        if current_node.next:
            current_node.next.prev = current_node.prev
        if current_node.prev:
            current_node.prev.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")
#testing 
# Create a doubly linked list
dll = DoublyLinkedList()

# elements
dll.insert_at_beginning(101)
dll.insert_at_end(202)
dll.insert_at_end(303)

# Display 

print("Doubly Linked List:")
dll.display()  

# Delete 

dll.delete_node(2)

# Display

print("\nDoubly Linked List after deletion:")
dll.display() 

