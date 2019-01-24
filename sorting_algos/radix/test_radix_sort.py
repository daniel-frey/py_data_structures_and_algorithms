import pytest
from radix_sort import radix_sort


def test_list_gets_sorted():
    """Test the sorting method on the list."""
    unsorted = [3, 2, 1, 4]
    assert radix_sort(unsorted) == [1, 2, 3, 4]


def test_incorrect_input():
    """Test incorrect input throws an error."""
    unsorted = 'a,b,c,d'
    with pytest.raises(TypeError):
        radix_sort(unsorted)


def test_sorted_list_remains():
    """Test a previously sorted list."""
    unsorted = [num for num in range(20)]
    list_sorted = radix_sort(unsorted)
    assert unsorted == list_sorted


def test_duplicate_value_list():
    """Test duplicate values in a list to make sure they are sorted correctly."""
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    list_sorted = radix_sort(unsorted)
    assert expected == list_sorted
