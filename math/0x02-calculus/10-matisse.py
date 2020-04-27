#!/usr/bin/env python3
"""Module to calculate the derivative of a polynomial.
"""


def poly_derivative(poly):
    """Computes the derivative of a polynomial.

    Arguments:
        poly (list):    is a list of coefficients representing a polynomial
                        the index of the list represents the power of x that
                        the coefficient belongs to.

    Returns:
        list:   a new list of coefficients representing
                the derivative of the polynomial,
                a list with a zero if the derivative is zero or
                None if the polynomial is invalid.
    """
    if not poly or not isinstance(poly, list):
        return None
    invalid_elements = filter(
        lambda item_type: not isinstance(item_type, (int, float)),
        poly
    )
    if list(invalid_elements):
        return None
    else:
        terms = len(poly)
        if terms == 1:
            return [0]
        else:
            return [idx * poly[idx] for idx in range(1, terms)]
