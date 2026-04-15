"""Basic calculator operations."""


def add(a, b):
    """Return the sum of a and b.
    
    Args:
        a (float or int): First number.
        b (float or int): Second number.
    Returns:
        float or int: The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """Return the result of subtracting b from a.
    
    Args:
        a (float or int): Minuend.
        b (float or int): Subtrahend.
    Returns:
        float or int: The difference (a - b).
    """
    return a - b


def multiply(a, b):
    """Return the product of a and b.
    
    Args:
        a (float or int): First number.
        b (float or int): Second number.
    Returns:
        float or int: The product.
    """
    return a * b


def divide_numbers(a, b):
    """Divide a by b and return the result.
    
    Args:
        a (float or int): Numerator.
        b (float or int): Denominator.
    Returns:
        float: Division result.
    Raises:
        ValueError: If division by zero is attempted.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Return base raised to the power of exponent.
    
    Args:
        base (float or int): The base number.
        exponent (float or int): The exponent.
    Returns:
        float or int: Result of base ** exponent.
    """
    return base ** exponent
