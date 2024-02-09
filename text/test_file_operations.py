from src.file_operations import choose_word, display_word, get_word_length
import pytest 

def test_choose_word():
    word = choose_word()
    assert len(word.split()) == 1

def test_display_word():
    word = "python"
    guessed_letters = ["p", "y"]
    assert display_word(word, guessed_letters) == "py____"

def test_get_word_length():
    word = "python"
    assert get_word_length(word) == 6

