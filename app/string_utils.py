"""String utility functions."""


def reverse_string(s):
    """Return the reversed version of the given string.
    
    Args:
        s (str): String to reverse.
    Returns:
        str: Reversed string.
    """
    return s[::-1]


def count_vowels(s):
    """Count the number of vowels in a string.
    
    Args:
        s (str): String to analyze.
    Returns:
        int: Number of vowels.
    """
    return sum(1 for c in s if c in "aeiou")


def find_word(text, word):
    """Check if word exists in text. Returns True/False.
    
    Args:
        text (str): Full text to search.
        word (str): Word to find.
    Returns:
        bool: True if word exists, otherwise False.
    """
    return word in text


def capitalize_words(s):
    """Capitalize the first character of each word in the string.
    
    Args:
        s (str): String to capitalize.
    Returns:
        str: Capitalized string.
    """
    return " ".join(w.capitalize() for w in s.split())


def truncate(s, max_length):
    """Truncate the string to at most max_length characters.
    
    Args:
        s (str): String to truncate.
        max_length (int): Maximum allowed length.
    Returns:
        str: Truncated string.
    """
    if len(s) <= max_length:
        return s
    return s[:max_length]
