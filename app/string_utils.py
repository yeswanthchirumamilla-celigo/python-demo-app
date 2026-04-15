"""String utility functions."""

def reverse_string(s):
    """
    Reverse the input string.
    Args:
        s (str): The input string.
    Returns:
        str: The reversed string.
    """
    return s[::-1]

def count_vowels(s):
    """
    Count the number of vowels in the input string.
    Args:
        s (str): The input string.
    Returns:
        int: The number of vowels in s.
    """
    return sum(1 for c in s if c in "aeiou")

def find_word(text, word):
    """
    Check if word exists in text.
    Args:
        text (str): The main string to search in.
        word (str): The word to search for.
    Returns:
        bool: True if word is found, False otherwise.
    """
    return word in text

def capitalize_words(s):
    """
    Capitalize the first letter of each word in the string.
    Args:
        s (str): The input string.
    Returns:
        str: The string with each word capitalized.
    """
    return " ".join(w.capitalize() for w in s.split())

def truncate(s, max_length):
    """
    Truncate the string to a maximum length if necessary.
    Args:
        s (str): Input string.
        max_length (int): Maximum length to truncate.
    Returns:
        str: The truncated string.
    """
    if len(s) <= max_length:
        return s
    return s[:max_length]
