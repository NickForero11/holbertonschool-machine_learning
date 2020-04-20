#!/usr/bin/env python3
"""Module to compute the addition of two matrices which can be of up to 3D.
"""
matrix_shape = __import__('2-size_me_please').matrix_shape


def add_matrices(mat1, mat2):
    """Adds two matrices of the same shape.

    Arguments:
        mat1 (list):    a matrix (list of lists) which can be of up to three
                        dimmensions.
        mat2 (list):    a matrix (list of lists) which can be of up to three
                        dimmensions.

    Returns:
        list:   a matrix (list of lists) which is the addition
                of @mat1 and @mat2.
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        if isinstance(mat1[0], list):
            return [add_matrices(*submatrix) for submatrix in zip(mat1, mat2)]
        else:
            return [sum(elem) for elem in zip(mat1, mat2)]
