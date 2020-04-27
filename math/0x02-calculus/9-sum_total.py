#!/usr/bin/env python3
"""Module to calculate sums of i*i.
"""


def summation_i_squared(n):
    """Compute the summation of i squared (i²)
    by using the Faulhaber's formula.
    Arguments:
        n (int): the index or the limit of the summation.

    Returns:
        int: the summattion if the limit is valid, else None.
    """
    if not isinstance(n, (int, float)) or n < 1:
        return None
    a = 2 * (n ** 3)
    b = 3 * (n ** 2)
    return int((a + b + n) / 6)
