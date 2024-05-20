#Creating Singly Linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#to also support insertion, deletion and transversal 
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

#test

# Create a singly linked list
sll = SinglyLinkedList()

# Insert some elements
sll.insert_at_beginning(101)
sll.insert_at_end(202)
sll.insert_at_end(303)

# Display the list
print("Singly Linked List:")
sll.display() 
# Delete an element
sll.delete_node(374)

# Display the updated list
print("\nSingly Linked List after deletion:")
sll.display()  
