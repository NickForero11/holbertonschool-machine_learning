#!/usr/bin/env python3
"""Module that contains a basic implementation of a Neuron
that performs binary classification.
"""
import numpy as np


class Neuron():
    """Class that defines a single neuron performing binary classification.
    """

    def __init__(self, nx):
        """Initialize a Neuron instance according to a number
        of input features.

        Arguments:
            nx (Int): Is the number of input features to the neuron.

        Raises:
            TypeError: If nx is not an integer.
            ValueError: If nx is less than 1.
        """
        # Check if the number of input features have the right format
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        # Initialize the weights, the bias and the activated output
        # of the neuron.
        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0
