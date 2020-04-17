#!/usr/bin/env python3
"""Module to compute the addition of two arrays"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise if they're of the same shape.

    Arguments:
        arr1 (list): a list of ints/floats.
        arr2 (list): a list of ints/floats.

    Returns:
        list: a list of ints/float with the elements of arr1 and arr2.
    """
    if len(arr1) != len(arr2):
        return None
    else:
        return list(
            map(
                lambda num1, num2: num1 + num2,
                arr1, arr2
            )
        )
