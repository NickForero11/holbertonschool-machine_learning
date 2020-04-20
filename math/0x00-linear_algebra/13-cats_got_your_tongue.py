#!/usr/bin/env python3
"""Module to compute the concatenation of two matrices along a specific axis.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two NumPy Arrays along a specific axis.

    Arguments:
        mat1 (numpy.ndarray):   a NumPy array that normally represents a square
                                matrix.
        mat2 (numpy.ndarray):   a NumPy array that normally represents a square
                                matrix.

    Keyword Arguments:
        axis (int): specifies in which dimension will be concatenated
                    the Numpy Arrays (default: {0}).

    Returns:
        numpy.ndarray:  a NumPy array which is the concatenation
                        of @mat1 and @mat2.
    """
    return np.concatenate((mat1, mat2), axis=axis)
