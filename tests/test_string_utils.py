from app.string_utils import reverse_string, count_vowels, find_word, capitalize_words, truncate


def test_reverse():
    assert reverse_string("hello") == "olleh"


def test_count_vowels():
    assert count_vowels("hello") == 2


def test_find_word():
    assert find_word("hello world", "world") is True
    assert find_word("hello world", "World") is True  # BUG: this will fail


def test_capitalize():
    assert capitalize_words("hello world") == "Hello World"


def test_truncate():
    assert truncate("hello world", 5) == "hello"
