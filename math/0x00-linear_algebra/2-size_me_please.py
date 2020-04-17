#!/usr/bin/env python3
"""Module to compute the shape of a matrix"""


def matrix_shape(matrix):
    """Calculates the shape of a matrix.

    Arguments:
        matrix (list): the matrix that will be processed

    Returns:
        tuple:  a tuple that contains the shape of every dimmension
                in the matrix.
    """
    shape = []
    dimension = matrix[:]
    while isinstance(dimension, list):
        size = len(dimension)
        shape.append(size)
        if size > 0:
            dimension = dimension[0]
        else:
            break

    return shape
