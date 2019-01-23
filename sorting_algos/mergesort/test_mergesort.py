import pytest
from mergesort import mergesort


def test_gets_sorted():
    """Test that an unsorted list gets sorted."""
    unsorted_list = [3, 2, 1, 4]
    assert mergesort(unsorted_list) == [1, 2, 3, 4]


def test_doesnt_mess_up_already_sorted():
    """ Tests to make sure an already sorted list remains the same
    """
    unsorted_list = [num for num in range(20)]
    sorted_list = mergesort(unsorted_list)
    assert unsorted_list == sorted_list


def test_sorts_list_of_duplicates():
    """Test that duplicate items still gets sorted."""
    unsorted_list = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    sorted_list = mergesort(unsorted_list)
    assert expected == sorted_list
