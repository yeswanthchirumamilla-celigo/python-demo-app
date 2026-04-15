"""String utility functions."""

def reverse_string(s):
    """
    Reverse a given string.

    Args:
        s (str): Input string.

    Returns:
        str: Reversed version of the input string.
    """
    return s[::-1]

def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
        s (str): Input string.

    Returns:
        int: Number of vowels in s.
    """
    return sum(1 for c in s if c in "aeiou")

def find_word(text, word):
    """
    Check if word exists in text. Returns True/False.

    Args:
        text (str): The string to search within.
        word (str): Substring (word) to search for.

    Returns:
        bool: True if word is present, False otherwise.
    """
    return word in text

def capitalize_words(s):
    """
    Capitalize every word in the string.

    Args:
        s (str): Input string.

    Returns:
        str: String with each word capitalized.
    """
    return " ".join(w.capitalize() for w in s.split())

def truncate(s, max_length):
    """
    Truncate the string to a maximum length.

    Args:
        s (str): Input string.
        max_length (int): Maximum allowed length.

    Returns:
        str: Truncated string if needed, else original string.
    """
    if len(s) <= max_length:
        return s
    return s[:max_length]
