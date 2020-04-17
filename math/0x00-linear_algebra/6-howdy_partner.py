#!/usr/bin/env python3
"""Module to compute the concatenation of two arrays"""


def cat_arrays(arr1, arr2):
    """Concatenates two arrays of ints/floats.

    Arguments:
        arr1 (list) : an array of integer or floating numbers.
        arr2 (list) : an array of integer or floating numbers.

    Returns:
        list: a new list with the elements of arr1 and arr2.
    """
    return arr1[:] + arr2[:]
