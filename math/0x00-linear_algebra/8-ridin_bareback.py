#!/usr/bin/env python3
"""Module to compute the multiplication of two 2D matrices"""
matrix_transpose = __import__('3-flip_me_over').matrix_transpose


def reduce_by_multiplication(data):
    """Multiplies all the elements in a list and returns the total.

    Arguments:
        data (list): a list of integers or floats.

    Returns:
        (int or float): the total of multiplicate every number in data.
    """
    total = 1
    for num in data:
        total *= num
    return total


def dot_product(vector1, vector2):
    """Computes the dot product between two vectors.

    Arguments:
        vector1 (list): a list of integers or floats.
        vector2 (list): a list of integers or floats.

    Returns:
        (int or float): the dot product between vector1 and vector2.
    """
    return [reduce_by_multiplication(pair) for pair in zip(vector1, vector2)]


def mat_mul(mat1, mat2):
    """Compute the multiplication of two 2D matrices.

    Arguments:
        mat1 (list): a 2D matrix containing ints/floats of the same type/shape.
        mat2 (list): a 2D matrix containing ints/floats of the same type/shape.

    Returns:
        (list): a 2D matrix with the rows number of mat1
                and columns number of mat2.
    """

    if len(mat1[0]) == len(mat2):

        mat2 = matrix_transpose(mat2)
        response = []

        for row in range(len(mat1)):
            response.append(
                [
                    sum(dot_product(mat1[row], mat2[column]))
                    for column in range(len(mat2))
                ]
            )

        return response

    else:
        return None
