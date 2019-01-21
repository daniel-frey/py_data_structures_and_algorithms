import pytest
from .selection import selection_sort


def test_list_gets_sorted():
    """Test to make sure unsorted list gets sorted."""
    unsorted = [3, 2, 1, 4]
    assert selection_sort(unsorted) == [1, 2, 3, 4]


def test_non_list_throws_error():
    """Test to make tje incorrect input results in an error."""
    unsorted = 'a,b,c,d'
    with pytest.raises(TypeError):
        selection_sort(unsorted)


def test_doesnt_mess_up_already_sorted():
    """Test sorted list returns the same."""
    unsorted = [num for num in range(20)]
    now_sorted = selection_sort(unsorted)
    assert unsorted == now_sorted


def test_sorts_list_of_duplicates():
    """Test a list with duplicates values returns the correct sorted order."""
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted
