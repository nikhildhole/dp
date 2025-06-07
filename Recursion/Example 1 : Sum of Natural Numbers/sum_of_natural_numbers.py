"""
Find the sum of first n natural numbers using recursion.
"""

def sum_of_natural_numbers(n: int) -> int:
    """
    Calculate the sum of first n natural numbers using recursion.

    :param n: The number up to which the sum is to be calculated.
    :return: The sum of first n natural numbers.
    """
    if n == 0:
        return 0
    
    return sum_of_natural_numbers(n - 1) + n