def quick_sort(arr):
    """
    Sorts the given array using the Quick Sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        None: The sorting is done in-place, so the original array is modified.
    """
    if len(arr) <= 1:  # Base case: If the array has 0 or 1 element, it is already sorted
        return arr
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        lesser_than_pivot = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to the pivot
        greater_than_pivot = [x for x in arr[1:] if x > pivot]  # Elements greater than the pivot
        # Recursively apply quick sort to the sub-arrays, then concatenate them with the pivot
        return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

if __name__ == "__main__":
    # Test quick_sort function with sample input
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    quick_sort(arr)
    print("Sorted array:", arr)
