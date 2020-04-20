#!/usr/bin/env python3
"""Module to compute the shape of a NumPy ndarray"""


def np_shape(matrix):
    """Calculates the shape of a NumPy ndarray using its default field.

    Arguments:
        matrix (numpy.ndarray): a NumPy array (a representation of a square
                                matrix in most cases).

    Returns:
        tuple:  a tuple of integers with the size of every dimension
                in the matrix.
    """
    return matrix.shape
