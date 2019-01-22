import pytest
from .quicksort import quicksort


def test_sorted():
    """Test the sorting algo."""
    unsorted = [3, 2, 1, 4]
    assert quicksort(unsorted, 0, 3) == [1, 2, 3, 4]


def test_wrong_type_throws_error():
    """ Test to make sure the incorrect input throws an error."""
    unsorted = 'a,b,c,d'
    with pytest.raises(TypeError):
        quicksort(unsorted, 0, 3)


def test_already_sorted():
    """Test a sorted list remains sorted."""
    unsorted = [num for num in range(20)]
    now_sorted = quicksort(unsorted, 0, 19)
    assert unsorted == now_sorted


def test_list_contains_dpulicates():
    """Test the sorting of a list that has duplicates."""
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = quicksort(unsorted, 0, 9)
    assert expected == now_sorted
