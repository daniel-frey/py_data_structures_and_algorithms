from .hash_table import HashTable
import pytest


def test_empty_table_set():
    """Test empty hash table set method"""
    ht = HashTable()
    ht.set('Football', 'Head')
    assert ht.get('Football') == 'Head'


def test_get_empty_table_hash():
    """Test get doesn't work if table empty"""
    ht = HashTable()
    assert ht.get('Football') == 'The value is not in the table'


def test_remove_the_happy_path():
    """Test remove on a small ht"""
    ht = HashTable()
    ht.set('Football', 'Head')
    assert ht.remove('Football') == 'True'


def test_remove_empty_hash_table():
    """Test remove on empty ht"""
    ht = HashTable()
    assert ht.remove('Football') == 'False'
