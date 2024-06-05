class Stack:
    def __init__(self):
        # Initialize the stack as an empty list
        self.items = []

    def push(self, item):
        # Add the new item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Check if the stack is not empty
        if not self.is_empty():
            # Remove and return the top item from the stack
            return self.items.pop()
        else:
            # Print a message if the stack is empty and return None
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        # Check if the stack is not empty
        if not self.is_empty():
            # Return the top item from the stack without removing it
            return self.items[-1]
        else:
            # Print a message if the stack is empty and return None
            print("Stack is empty. Cannot peek.")
            return None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

if __name__ == "__main__":
    # Test stack operations
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack.items)
    print("Pop item:", stack.pop())
    print("Stack after pop:", stack.items)
    print("Peek item:", stack.peek())
    print("Is stack empty?", stack.is_empty())
    print("Stack size:", stack.size())
