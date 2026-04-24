"""Basic calculator operations."""

def add(a, b):
    """
    Add two numbers.
    Args:
        a: First number.
        b: Second number.
    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract b from a.
    Args:
        a: First number.
        b: Second number.
    Returns:
        The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.
    Args:
        a: First number.
        b: Second number.
    Returns:
        The product of a and b.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divide a by b.
    Args:
        a: Numerator.
        b: Denominator.
    Returns:
        The result of division.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """
    Raise base to the given exponent.
    Args:
        base: The base number.
        exponent: The exponent value.
    Returns:
        base raised to the power of exponent.
    """
    return base ** exponent
