from .multi_bracket_validation import multi_bracket_validation
import pytest


def test_multi_bracket_validation():
    """Test that the method exist."""
    assert multi_bracket_validation


def test_balanced_nested_bracket_validation():
    """Test the completion of the stack method is empty and the string is balanced."""
    assert multi_bracket_validation('{([])}') is True


def test_balanced_with_words():
    """Test the completion of the stack method is empty regardless of characters and is balanced.."""
    assert multi_bracket_validation('{}{Code}[Fellows](())') is True


def test_balanced_validation():
    """Test the stack for correct validation"""
    assert multi_bracket_validation('{}[]()') is True


def test_unbalanced_bracket():
    """Test the stack for in-balanced input."""
    assert multi_bracket_validation('([]]]') is False


def test_unbalanced_bracket_one_more_time_because_why_not():
    """Test the stack for in-balanced input with bracket characters."""
    assert multi_bracket_validation('(](') is False


def test_unbalanced_incorrect_order_bracket():
    """Test edge case of incorrect bracket assertion."""
    assert multi_bracket_validation('([)]') is False


def test_unbalanced_with_one_character():
    """Test edge case of only one bracket"""
    assert multi_bracket_validation('[') is False

