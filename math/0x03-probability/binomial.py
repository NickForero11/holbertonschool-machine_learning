#!/usr/bin/env python3
"""Module to represent the Binomial Distribution
"""


class Binomial():
    """Class that represents a Binomial Distribution.
    """

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes a Binomial Distribution.

        Keyword Arguments:
            data (List):    a list of the data to be used to estimate
                            the distribution (default: {None})
            n (Int):        the number of Bernoulli trials (default: {1})
            p (Float):      the probability of a “success” (default: {0.5})

        Raises:
            ValueError: If data isn't given and n isn't a positive value.
            ValueError: If data isn't given and p is not a valid probability.
            TypeError:  If data isn't a list.
            ValueError: If data doesn't contain at least two data points.
        """
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            elif p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            else:
                self.n = int(n)
                self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            else:
                num_of_elements = len(data)
                if num_of_elements < 2:
                    raise ValueError('data must contain multiple values')
                else:
                    mean = sum(data) / num_of_elements
                    differences_squared = map(
                        lambda num: ((num - mean) ** 2),
                        data
                    )
                    variance = sum(differences_squared) / num_of_elements
                    # Calculate p
                    p = 1 - (variance / mean)
                    # Calculate n
                    n = mean / p
                    # round n to the nearest int
                    self.n = round(n)
                    # Recalculate p to get more precision
                    self.p = float(mean / self.n)
