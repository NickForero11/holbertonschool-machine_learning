#!/usr/bin/env python3
"""Module to represent the Poisson Distribution
"""


def factorial(number):
    """Compute the factorial of a number.

    Arguments:
        number (int): an integer number greater than 0

    Returns:
        int: the factorial of @number.
    """
    result = 1
    while number:
        result *= number
        number -= 1
    return result


class Poisson():
    """Class Poisson that represents a Poisson Distribution.
    """

    def __init__(self, data=None, lambtha=1.):
        """Initializes a Poisson Distribution.

        Keyword Arguments:
            data (List):        a list of the data to be used to estimate
                                the distribution (default: {None})
            lambtha (Float):    the expected number of occurrences
                                in a given time frame (default: {1.})

        Raises:
            ValueError: If data isn't given and lambtha isn't a positive value.
            TypeError:  If data isn't a list.
            ValueError: If data doesn't contain at least two data points.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            else:
                num_of_elements = len(data)
                if num_of_elements < 2:
                    raise ValueError('data must contain multiple values')
                else:
                    self.lambtha = sum(data) / num_of_elements

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of “successes”.

        Arguments:
            k (integer): is the number of “successes”.

        Returns:
            float: the PMF value for k, 0 otherwise
        """
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)
        e = 2.7182818285
        return ((e ** (-self.lambtha) * (self.lambtha ** k)) / factorial(k))
