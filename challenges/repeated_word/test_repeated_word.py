from repeated_word import repeated_word
import pytest


def test_word_appears_twice():
    assert repeated_word('The quick brown fox jumped over the lazy dog') == 'the'


def test_word_appears_three_times():
    assert repeated_word('The quick quick brown fox jumped over the lazy dog') == 'quick'


def test_all_words_once():
    assert repeated_word('The quick brown fox jumped over lazy dog') == []


def test_repeated_word():
    assert repeated_word('The the quick brown fox jumped over lazy dog') == 'the'


def test_repeated_last_word():
    assert repeated_word('The quick brown fox jumped over lazy cat cat') == 'cat'


def test_empty_string():
    assert repeated_word('') == []