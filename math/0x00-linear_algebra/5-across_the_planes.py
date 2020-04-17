#!/usr/bin/env python3
"""Module to compute the addition of two matrices"""
matrix_shape = __import__('2-size_me_please').matrix_shape
add_arrays = __import__('4-line_up').add_arrays


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise if they're of the same shape.

    Arguments:
        mat1 (list): a 2D matrix containing ints/floats.
        mat2 (list): a 2D matrix containing ints/floats.

    Returns:
        list:   a 2D matrix containing ints/floats with
                the elements of mat 1 and mat2.
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        transposed = list(zip(mat1, mat2))
        return [add_arrays(*pair) for pair in transposed]
