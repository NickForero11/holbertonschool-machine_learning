#!/usr/bin/env python3
"""Module to compute the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """Compute the transpose of a 2D matrix.

    Arguments:
        matrix (list):    A 2D list/matrix where all elements in the same
                          dimension are of the same type/shape.

    Returns:
        list: a 2D list/matrix.
    """
    response = [
        [vector[row] for vector in matrix]
        for row in range(len(matrix[0]))
    ]
    return [list(vector) for vector in zip(*matrix)]
