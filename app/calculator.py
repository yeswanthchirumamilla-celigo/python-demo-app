"""Basic calculator operations."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide_numbers(a, b):
    """Divide a by b and return the result. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    return base ** exponent
