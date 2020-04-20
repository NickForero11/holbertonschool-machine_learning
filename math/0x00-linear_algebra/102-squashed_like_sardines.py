#!/usr/bin/env python3
"""Dummy module.
"""
matrix_shape = __import__('2-size_me_please').matrix_shape
cat_arrays = __import__('6-howdy_partner').cat_arrays
cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D


def cat_matrices(mat1, mat2, axis=0):
    """Dummy function"""
    response = None
    if not (len(matrix_shape(mat1)) < axis or len(matrix_shape(mat2)) < axis):
        # Case 1D
        if isinstance(mat1[0], (int, float)):
            response = cat_arrays(mat1, mat2)
        # Case 2D
        elif isinstance(mat1[0][0], (int, float)):
            response = cat_matrices2D(mat1, mat2, axis=axis)
    return response
