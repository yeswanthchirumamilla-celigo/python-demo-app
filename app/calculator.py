"""Basic calculator operations."""

def add(a, b):
    """
    Add two numbers and return the result.
    Args:
        a (numeric): The first operand.
        b (numeric): The second operand.
    Returns:
        numeric: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract b from a and return the result.
    Args:
        a (numeric): The value to subtract from.
        b (numeric): The value to subtract.
    Returns:
        numeric: The result of a - b.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers and return the product.
    Args:
        a (numeric): The first operand.
        b (numeric): The second operand.
    Returns:
        numeric: The product of a and b.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divide a by b and return the result.
    Args:
        a (numeric): Numerator.
        b (numeric): Denominator; must not be zero.
    Returns:
        float: The division result.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """
    Raise base to the exponent power.
    Args:
        base (numeric): The number to be raised.
        exponent (numeric): The power.
    Returns:
        numeric: The result of base ** exponent.
    """
    return base ** exponent
