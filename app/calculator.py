"""Basic calculator operations."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide_numbers(a, b):
    """Divide a by b and return the result. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent
