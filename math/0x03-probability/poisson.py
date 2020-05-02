"""Module to represent the Poisson Distribution
"""


class Poisson():
    def __init__(self, data=None, lambtha=1.):
        if not data:
            if lambtha < 0:
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

