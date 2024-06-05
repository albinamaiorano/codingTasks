def binary_search(arr, target):
    """
    Searches for the target element in the given sorted array using binary search algorithm.

    Parameters:
    arr (list): The sorted list to search in.
    target (int): The target element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    # Initialize left and right pointers for the binary search
    left, right = 0, len(arr) - 1

    # Loop until the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the mid index
        mid = (left + right) // 2
        
        # Check if the mid element is the target
        if arr[mid] == target:
            return mid
        # If the mid element is less than the target, update the left pointer
        elif arr[mid] < target:
            left = mid + 1
        # If the mid element is greater than the target, update the right pointer
        else:
            right = mid - 1
    
    # If the target is not found, return -1
    return -1

if __name__ == "__main__":
    # Test binary_search function with sample input
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print("Array:", arr)
    print("Target:", target)
    print("Index of target:", binary_search(arr, target))
