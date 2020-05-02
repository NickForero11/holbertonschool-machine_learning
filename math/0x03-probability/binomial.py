#!/usr/bin/env python3
"""Module to represent the Binomial Distribution
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

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of “successes”.

        Arguments:
            k (Integer): is the number of “successes”.

        Returns:
            Float: the PMF value for k, 0 otherwise
        """
        # Check parameters
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)

        combination = (
            factorial(self.n) / (factorial(k) * factorial(self.n - k))
        )
        # if you multiplicate the combination with the next as variable
        # it will be a different value due to the floating number precision
        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of “successes”.

        Arguments:
            k (integer): is the number of “successes”.

        Returns:
            float: the CDF value for k, 0 otherwise.
        """
        # Check parameters
        if k < 0:
            return 0
        if not isinstance(k, int):
            k = int(k)

        result = 0
        # Summatory from 0 to k, so k needs to be included in range
        # then add k + 1 as limit of range because its non inclusive
        for index in range(k + 1):
            result += self.pmf(index)
        return result
