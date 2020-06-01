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
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for the weights vector of the neuron.

        Returns:
            numpy.ndarray: The weights vector for the neuron.
        """
        return self.__W

    @property
    def b(self):
        """Getter for the bias of the neuron.

        Returns:
            float: The bias for the neuron.
        """
        return self.__b

    @property
    def A(self):
        """Getter for the prediction of the neuron.

        Returns:
            float: The activated output of the neuron.
        """
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron.

        Take in account that the neuron will use
        the sigmoid activation function.

        Arguments:
            X (numpy.ndarray):  an array with shape (nx, m) that contains
                                the input data, where:
                                - nx: number of input features to the neuron
                                - m: number of examples

        Returns:
            float: The activated output of the neuron(prediction).
        """
        input_shape = X.shape
        weights_shape = self.W.shape
        # Check if the Input features have the right dimensions.
        if input_shape[0] != weights_shape[1]:
            print("Dimension error")
        else:
            y = (np.dot(self.W, X)) + self.b
            # Applies the sigmoid function as activation function.
            activated = 1 / (1 + np.exp(-y))
            self.__A = activated
        return self.A
