"""
Test cases for the sum of natural numbers function.
"""
from sum_of_natural_numbers import sum_of_natural_numbers
import pytest   
print("Test cases for the sum of natural numbers function.")
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (10, 55),
    (100, 5050),
    (0, 0),  # Edge case: sum of first 0 natural numbers
])
def test_sum_of_natural_numbers(n, expected):
    """
    Test the sum_of_natural_numbers function with various inputs.
    
    :param n: The input number for which the sum is calculated.
    :param expected: The expected result of the sum.
    """
    assert sum_of_natural_numbers(n) == expected