def selection_sort(unsorted):
    """Implement the selection sort method."""
    if type(unsorted) is not list:
        raise TypeError('Your input must be a list.')
    for i in range(0, len(unsorted)):
        minimum = i
        for j in range(i+1, len(unsorted)):
            # check current minimum number to the current number
            if unsorted[minimum] > unsorted[j]:
                minimum = j
        # swap the minimum and the current numbers
        unsorted[i], unsorted[minimum] = unsorted[minimum], unsorted[i]
    return unsorted
