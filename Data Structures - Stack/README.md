# Data Structures - Stack

## Description
This task involves implementing a Stack data structure in Python. A stack is a collection of elements that follows the Last In, First Out (LIFO) principle. It supports operations such as push (adding an element to the top of the stack), pop (removing the top element from the stack), peek (viewing the top element without removing it), checking if the stack is empty, and getting the size of the stack.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

## Usage
1. Clone the repository or download the `stack.py` file.
2. Import the `Stack` class into your Python script.
3. Create a `Stack` object and use its methods to perform stack operations.
4. Example usage:
    ```python
    from stack import Stack

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
    ```


