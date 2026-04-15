"""Basic calculator operations."""

def add(a, b):
    """
    Add two numbers.

    Args:
        a (float/int): First number.
        b (float/int): Second number.

    Returns:
        float/int: Sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract b from a.

    Args:
        a (float/int): First number.
        b (float/int): Second number to subtract from a.

    Returns:
        float/int: Result of a - b.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (float/int): First number.
        b (float/int): Second number.

    Returns:
        float/int: Product of a and b.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divide a by b and return the result. Raises ValueError on division by zero.

    Args:
        a (float/int): Dividend.
        b (float/int): Divisor.

    Returns:
        float/int: Result of a / b.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """
    Raise a number to a power.

    Args:
        base (float/int): The base number.
        exponent (float/int): The exponent.

    Returns:
        float/int: Result of base ** exponent.
    """
    return base ** exponent
