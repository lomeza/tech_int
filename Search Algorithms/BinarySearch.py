def binary_search(arr, target):
    """
    Performs binary search on a SORTED array to find the index of the target element.

    Returns:
        The index of the target element if found, -1 otherwise.
    """

    low, high = 0, len(arr) - 1

    while low <= high:
        # mid-declaration that changes each loop using int division
        mid = (low + high) // 2
        # return the answer if it is in the middle first
        if arr[mid] == target:
            return mid
        # if mid is less than target (top half) raise mid by 1
        elif arr[mid] < target:
            low = mid + 1
        # if target is lower than target (bottom half) lower mid by 1
        else:
            high = mid - 1
    # return -1 if target not in array
    return -1