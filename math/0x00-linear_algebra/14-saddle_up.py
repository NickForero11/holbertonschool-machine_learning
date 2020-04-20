#!/usr/bin/env python3
"""Module to compute matrix multiplications.
"""
import numpy as np


def np_matmul(mat1, mat2):
    """Calculate the multiplication of two NumPy Arrays.

    Arguments:
        mat1 (numpy.ndarray):   a NumPy array that normally represents a square
                                matrix.
        mat2 (numpy.ndarray):   a NumPy array that normally represents a square
                                matrix.

    Returns:
        numpy.ndarray:  a NumPy array which is the multiplication
                        of @mat1 and @mat2.
    """
    return np.matmul(mat1, mat2)
