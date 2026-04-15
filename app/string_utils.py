"""String utility functions."""


def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    return sum(1 for c in s if c in "aeiou")


def find_word(text, word):
    """Check if word exists in text. Returns True/False."""
    return word.lower() in text.lower()


def capitalize_words(s):
    return " ".join(w.capitalize() for w in s.split())


def truncate(s, max_length):
    if len(s) <= max_length:
        return s
    return s[:max_length]
