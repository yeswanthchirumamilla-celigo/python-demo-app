"""String utility functions."""

def reverse_string(s):
    """
    Reverse the given string.
    Args:
        s: String to reverse.
    Returns:
        The reversed string.
    """
    return s[::-1]

def count_vowels(s):
    """
    Count the number of vowels in the string.
    Args:
        s: Input string.
    Returns:
        The count of vowels in s.
    """
    return sum(1 for c in s if c in "aeiou")

def find_word(text, word):
    """
    Check if a word exists in text.
    Args:
        text: Text to search in.
        word: Word to find.
    Returns:
        True if word is found in text, False otherwise.
    """
    return word in text

def capitalize_words(s):
    """
    Capitalize the first letter of each word in the string.
    Args:
        s: Input string.
    Returns:
        String with each word capitalized.
    """
    return " ".join(w.capitalize() for w in s.split())

def truncate(s, max_length):
    """
    Truncate the string up to max_length characters.
    Args:
        s: Input string.
        max_length: Maximum string length.
    Returns:
        Truncated string.
    """
    if len(s) <= max_length:
        return s
    return s[:max_length]
