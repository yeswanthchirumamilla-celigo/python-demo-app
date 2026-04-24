"""String utility functions."""

def reverse_string(s):
    """Return the reverse of the given string s."""
    return s[::-1]

def count_vowels(s):
    """Return the count of vowels in the string s."""
    return sum(1 for c in s if c in "aeiou")

def find_word(text, word):
    """Check if word exists in text. Returns True/False."""
    return word in text

def capitalize_words(s):
    """Capitalize the first character of each word in the string s."""
    return " ".join(w.capitalize() for w in s.split())

def truncate(s, max_length):
    """Truncate string s to max_length characters. If shorter, return original."""
    if len(s) <= max_length:
        return s
    return s[:max_length]
