#!/usr/bin/python3
import sys

"""
    Calculate the factorial of a non-negative integer.

    Parameters:
    - n (int): The integer for which factorial is to be calculated.

    Returns:
    - int: The factorial of the input integer n. Returns 1 if n is 0.

    Raises:
    - ValueError: If the input n is negative.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)