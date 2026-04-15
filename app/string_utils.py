"""String utility functions.

This module provides utility functions for string manipulation, such as reversing, counting vowels, finding words, capitalizing, and truncating strings.
"""

def reverse_string(s):
    """Return the reverse of the input string s."""
    return s[::-1]

def count_vowels(s):
    """Return the number of vowels in the input string s."""
    return sum(1 for c in s if c in "aeiou")

def find_word(text, word):
    """Check if word exists in text. Returns True if found, False otherwise."""
    return word in text

def capitalize_words(s):
    """Return the input string s with each word capitalized."""
    return " ".join(w.capitalize() for w in s.split())

def truncate(s, max_length):
    """Truncate the string s to max_length characters. If s is shorter, return s unchanged."""
    if len(s) <= max_length:
        return s
    return s[:max_length]
