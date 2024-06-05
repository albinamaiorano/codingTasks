class Node:
    def __init__(self, data=None):
        # Initialize a new node with data and next pointer
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with no head
        self.head = None

    def insert(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Set the new node's next pointer to the current head
        new_node.next = self.head
        # Set the head to the new node, making it the new head
        self.head = new_node

    def display(self):
        # Start from the head of the linked list
        current = self.head
        # Traverse the linked list until reaching the end (current is None)
        while current:
            # Print the data of the current node
            print(current.data, end=" -> ")
            # Move to the next node
            current = current.next
        # Print "None" to indicate the end of the linked list
        print("None")

def main():
    # Create a new linked list object
    ll = LinkedList()
    # Insert some elements into the linked list
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    # Display the contents of the linked list
    ll.display()

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
