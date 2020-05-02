#!/usr/bin/env python3
"""Module to represent the Normal Distribution
"""


class Normal():
    """Class that represents a Normal Distribution.
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes a Normal Distribution.

        Keyword Arguments:
            data (List):    a list of the data to be used
                            to estimate the distribution (default: {None})
            mean (float):   the mean of the distribution (default: {0.})
            stddev (float): the standard deviation of the distribution
                            (default: {1.})

        Raises:
            ValueError: If data isn't given and stddev is not a positive value.
            TypeError:  If data isn't a list.
            ValueError: If data doesn't contain at least two data points.
        """
        if data is None:
            self.mean = float(mean)
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            else:
                self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            else:
                num_of_elements = len(data)
                if num_of_elements < 2:
                    raise ValueError('data must contain multiple values')
                else:
                    self.mean = sum(data) / num_of_elements
                    differences_squared = map(
                        lambda num: ((num - self.mean) ** 2),
                        data
                    )
                    variance = sum(differences_squared) / num_of_elements
                    self.stddev = variance ** 0.5  # it means sqrt(variance)

    def z_score(self, x):
        """Calculates the z-score of a given x-value.

        Arguments:
            x (Int, Float): the x-value as a number.

        Returns:
            float: the z-score of x.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score.

        Arguments:
            z (Int, Float): the z-score.

        Returns:
            float: the x-value of z.
        """
        return (z * self.stddev) + self.mean
