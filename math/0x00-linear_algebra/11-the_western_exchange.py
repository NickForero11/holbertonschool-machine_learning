#!/usr/bin/env python3
"""Module to compute the transpose of a NumPy ndarray"""


def np_transpose(matrix):
    """Transpose a matrix and returns a new copy of it.

    Arguments:
        matrix (numpy.ndarray): a NumPy array (a representation of a square
                                matrix in most cases).

    Returns:
        numpy.ndarray: a NumPy array which is the transpose of @matrix.
    """
    return matrix.T.copy()
