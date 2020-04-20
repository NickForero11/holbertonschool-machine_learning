#!/usr/bin/env python3
"""Module to compute element-wise addition, subtraction,
multiplication, and division on a NumPy ndarray.
"""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication,
    and division.

    Arguments:
        mat1 (numpy.ndarray):   a NumPy array that normally represents a square
                                matrix.
        mat2 (numpy.ndarray):   a NumPy array that normally represents a square
                                matrix.

    Returns:
        tuple:  a tuple containing the element-wise sum, difference, product,
        and quotient, respectively.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
