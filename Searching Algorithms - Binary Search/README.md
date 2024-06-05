# Searching Algorithm - Binary Search

## Description
This task involves implementing the binary search algorithm in Python. Binary search is an efficient search algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array and continues narrowing down the search until the target is found or the subarray is empty.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

## Usage
1. Clone the repository or download the `binary_search.py` file.
2. Import the `binary_search` function into your Python script.
3. Create a sorted list to search in and specify the target element.
4. Call the `binary_search` function with the list and target element as arguments.
5. Example usage:
    ```python
    from binary_search import binary_search

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print("Array:", arr)
    print("Target:", target)
    print("Index of target:", binary_search(arr, target))
    ```

