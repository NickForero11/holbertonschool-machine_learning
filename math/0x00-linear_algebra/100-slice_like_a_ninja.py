#!/usr/bin/env python3
"""Module to compute slices of a matrix along specific axes.
"""


def np_slice(matrix, axes={}):
    """Slices a NumPy Array along specific axes.

    Arguments:
        matrix (numpy.ndarray): a NumPy array that normally represents a
                                square matrix.

    Keyword Arguments:
        axes (dict):    a dictionary where the key is an axis to slice along
                        and the value is a tuple representing the slice
                        to make along that axis (default: {{}}).

    Returns:
        numpy.ndarray:  a NumPy array which is a slice of @matrix on the
                        specific axes and slices.
    """
    slices = [slice(None)] * (max(axes.keys()) + 1)
    for key, value in axes.items():
        slices[key] = slice(*value)
    return matrix[tuple(slices)].copy()
