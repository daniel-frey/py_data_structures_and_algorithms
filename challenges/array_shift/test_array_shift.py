from .array_shift import insert_shift_list
import pytest

def test_with_an_even_amount_of_numbers():
    actual_list = [1, 3, 7, 9]
    actual_value_to_add = 5
    expected = [1, 3, 5, 7, 9]
    assert insert_shift_list(actual_list, actual_value_to_add) == expected

def test_with_and_odd_amount_of_numbers():
    actual_list = [3,5,90,21,78]
    actual_value_to_add = 54
    expected = [3,5,90,54,21,78]
    assert insert_shift_list(actual_list, actual_value_to_add) == expected

def test_the_list_is_empty():
    actual_list = []
    actual_value_to_add = 4
    expected = [4]
    assert insert_shift_list(actual_list, actual_value_to_add) == expected

def test_the_input_is_not_a_list():
    actual_list = {}
    actual_value_to_add = 0

    with pytest.raises(TypeError):
        insert_shift_list(actual_list, actual_value_to_add)
