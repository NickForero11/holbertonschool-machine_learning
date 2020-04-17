#!/usr/bin/env python3
"""Module to compute the concatenation of two 2D matrices"""
cat_arrays = __import__('6-howdy_partner').cat_arrays


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis
    if they're of the same shape.

    Arguments:
        mat1 (list): 2D matrices containing ints/floats.
        mat2 (list): 2D matrices containing ints/floats.

    Keyword Arguments:
        axis {int} -- [description] (default: {0})

    Returns:
        [type] -- [description]
    """

    # Row wise
    if axis == 0:
        response = [vector[:] for vector in (*mat1, *mat2)]
    # Column wise
    elif axis == 1:
        response = []
        for idx in range(len(mat1)):
            response.append(cat_arrays(mat1[idx], mat2[idx]))
    else:
        response = None

    return response
