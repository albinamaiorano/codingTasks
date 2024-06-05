class Queue:
    def __init__(self):
        # Initialize the queue as an empty list
        self.items = []

    def enqueue(self, item):
        # Add the new item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Check if the queue is not empty
        if not self.is_empty():
            # Remove and return the first item from the queue
            return self.items.pop(0)
        else:
            # Return None if the queue is empty
            return None

    def peek(self):
        # Check if the queue is not empty
        if not self.is_empty():
            # Return the first item from the queue without removing it
            return self.items[0]
        else:
            # Return None if the queue is empty
            return None

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)

if __name__ == "__main__":
    # Test queue operations
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:", queue.items)
    print("Dequeue item:", queue.dequeue())
    print("Queue after dequeue:", queue.items)
    print("Peek item:", queue.peek())
    print("Is queue empty?", queue.is_empty())
    print("Queue size:", queue.size())
