"""
Calculator Module
=================
This module provides basic arithmetic operations such as addition,
subtraction, multiplication, and division.

The functions include NumPy-style docstrings written manually as required.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Number to subtract.

    Returns
    -------
    float
        The result of a - b.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divide a by b.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.

    Returns
    -------
    float
        Result of division.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    return a / b


# Example function calls (optional)
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
