"""String utility functions."""


def reverse_string(s):
    """Return the reverse of the string s."""
    return s[::-1]


def count_vowels(s):
    """Return the number of vowels in string s."""
    return sum(1 for c in s if c in "aeiou")


def find_word(text, word):
    """Check if word exists in text. Returns True/False."""
    return word in text


def capitalize_words(s):
    """Return a string with each word in s capitalized."""
    return " ".join(w.capitalize() for w in s.split())


def truncate(s, max_length):
    """Truncate s to at most max_length characters."""
    if len(s) <= max_length:
        return s
    return s[:max_length]
