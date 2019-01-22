def pivot_values(arr, low, high):
    """Helper function for the quicksort. It takes a value to pivot and
    places lower left and higher to the right.
    """
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quicksort(arr, low, high):
    """ Quicksort function uses the pivot_values helper function."""
    if low < high:
        pi = pivot_values(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
    return arr
