#!/usr/bin/env python3
"""Module to represent the Exponential Distribution
"""


class Exponential():
    """Class Exponential that represents an Exponential Distribution.
    """

    def __init__(self, data=None, lambtha=1.):
        """Initializes a Exponential Distribution.

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
                    self.lambtha = num_of_elements / sum(data)
