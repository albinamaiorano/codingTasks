def insertion_sort(arr):
    """
    Sorts the given array using the insertion sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None. The original list is sorted in-place.
    """
    for i in range(1, len(arr)):  # Iterate over the array, starting from the second element
        key = arr[i]  # Store the current element to be compared
        j = i - 1  # Initialize the index to the left of the current element
        while j >= 0 and key < arr[j]:  # Move elements greater than the key to the right
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1  # Move to the left
        arr[j + 1] = key  # Place the key in its correct position

if __name__ == "__main__":
    # Test insertion_sort function with sample input
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
