# Data Structures - Queue

## Description
This task involves implementing a Queue data structure in Python. A queue is a collection of elements that follows the First In, First Out (FIFO) principle. It supports operations such as enqueue (adding an element to the rear of the queue), dequeue (removing the front element from the queue), peek (viewing the front element without removing it), checking if the queue is empty, and getting the size of the queue.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

## Usage
1. Clone the repository or download the `queue.py` file.
2. Import the `Queue` class into your Python script.
3. Create a `Queue` object and use its methods to perform queue operations.
4. Example usage:
    ```python
    from queue import Queue

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
    ```


