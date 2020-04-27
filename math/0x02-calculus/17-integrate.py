#!/usr/bin/env python3
"""Module to compute the integral of a polynomial.
"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial.

    Arguments:
        poly (list):    is a list of coefficients representing a polynomial
                        the index of the list represents the power of x that
                        the coefficient belongs to.

    Keyword Arguments:
        C (int):    is an integer representing the integration constant
                    (default: {0})

    Returns:
        list:   a new list of coefficients
                representing the integral of the polynomial,
                a list with the integration constant
                if the polynomial only has one term,
                None if the polynomial or the integration constant is invalid.
    """
    invalid_polynomial = not poly or not isinstance(poly, list)
    invalid_constant = not isinstance(C, (int, float))
    if invalid_polynomial or invalid_constant:
        return None
    invalid_elements = filter(
        lambda item_type: not isinstance(item_type, (int, float)),
        poly
    )
    if list(invalid_elements):
        return None
    else:
        terms = len(poly)
        # If poly = 0 integral => 0x + C => C
        if terms == 1:
            return [C]
        else:
            response = [0]
            for idx in range(terms):
                term = poly[idx] / (idx + 1)
                whole_term = int(term)
                response.append(whole_term if whole_term == term else term)
            # Delete empty coefficients at the end of the list
            while response[-1] == 0:
                response.pop()
            return response
