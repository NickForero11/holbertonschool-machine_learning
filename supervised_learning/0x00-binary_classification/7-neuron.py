#!/usr/bin/env python3
"""Module that contains a basic implementation of a Neuron
that performs binary classification.
"""
import numpy as np
import matplotlib.pyplot as plt


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
                                - nx: number of input features to the neuron.
                                - m: number of examples.

        Returns:
            float: The activated output of the neuron(prediction).
        """
        input_shape = X.shape
        weights_shape = self.W.shape
        # Check if the Input features have the right dimensions.
        if input_shape[0] != weights_shape[1]:
            print("Dimension error")
        else:
            y = (self.W @ X) + self.b
            # Applies the sigmoid function as activation function.
            activated = 1 / (1 + np.exp(-y))
            self.__A = activated
        return self.A

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression.

        Take in account that to avoid division by zero errors,
        1.0000001 - A will be used instead of 1 - A.

        m = the number of labels in Y.

        Arguments:
            Y (numpy.ndarray):  an array with shape (1, m) that contains
                                the correct labels for the input data.
            A (numpy.ndarray):  an array with shape (1, m) containing
                                the activated output of the neuron for each
                                example.

        Returns:
            float: the cost of the model.
        """
        number_of_labels = Y.shape[1]
        cost = np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return (-1 / number_of_labels) * cost

    def evaluate(self, X, Y):
        """Evaluates the neuron’s predictions.

        Take in account that:

        The prediction has a of shape (1, m) containing the predicted labels
        for each example.

        The label values are 1 if the output of the network is >= 0.5 and 0
        otherwise.

        Arguments:
            X (numpy.ndarray):  an array with shape (nx, m) that contains
                                the input data, where:
                                - nx: number of input features to the neuron
                                - m: number of examples.
            Y (numpy.ndarray):  an array with shape (1, m) that contains
                                the correct labels for the input data.

        Returns:
            tuple(numpy.ndarray, float):    the neuron’s prediction and
                                            the cost of the network,
                                            respectively
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return (prediction, cost)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of gradient descent on the neuron.

        Arguments:
            X (numpy.ndarray):  an array with shape (nx, m) that contains
                                the input data, where:
                                - nx: number of input features to the neuron
                                - m: number of examples.
            Y (numpy.ndarray):  an array with shape (1, m) that contains
                                the correct labels for the input data.
            A (numpy.ndarray):  an array with shape (1, m) containing
                                the activated output of the neuron for each
                                example.

        Keyword Arguments:
            alpha (float): is the learning rate (default: {0.05}).
        """
        number_of_labels = Y.shape[1]
        differential_in_z = A - Y
        differential_in_w = (X @ differential_in_z.T) / number_of_labels
        differential_in_b = differential_in_z.sum() / number_of_labels
        self.__W = self.W - (alpha * differential_in_w.T)
        self.__b = self.b - (alpha * differential_in_b)

    def train(
        self, X, Y, iterations=5000, alpha=0.05,
        verbose=True, graph=True, step=100
    ):
        """Trains the neuron with a specific number of iterations.

        Arguments:
            X (numpy.ndarray):  an array with shape (nx, m) that contains
                                the input data, where:
                                - nx: number of input features to the neuron
                                - m: number of examples.
            Y (numpy.ndarray):  an array with shape (1, m) that contains
                                the correct labels for the input data.

        Keyword Arguments:
            iterations (int):   the number of iterations to train over
                                (default: {5000}).
            alpha (float):      the learning rate (default: {0.05}).
            verbose (bool):     a boolean that defines whether or not
                                to print information about the training
                                (default: {True}).
            graph (bool):       a boolean that defines whether or not
                                to graph information about the training
                                once the training has completed
                                (default: {True}).
            step (int):         an integer that indicate after how many
                                iterations its needed to print information
                                about training or take in account the cost,
                                for the graph of the training
                                (default: {100}).

        Raises:
            TypeError:  if iterations isn't an integer.
            ValueError: if iterations isn't a positive integer.
            TypeError:  if alpha isn't a float.
            ValueError: if alpha isn't positive.
            TypeError:  if step isn't an integer.
            ValueError: if step isn't positive or is greater than
                        iterations.

        Returns:
            tuple(numpy.ndarray, float):    the evaluation of the training
                                            data after iterations of
                                            training have occurred.
        """
        # Check Kwargs
        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError('step must be an integer')
            if step < 1 or step > iterations:
                raise ValueError('step must be positive and <= iterations')
        if graph:
            costs = []

        # Start Training
        for iteration in range(iterations):
            A = self.forward_prop(X)
            self.gradient_descent(X, Y, A, alpha)
            if verbose or graph:
                cost = self.cost(Y, A)
                # If needed print data about the cost
                if iteration % step == 0:
                    if verbose:
                        print(
                            'Cost after {} iterations: {}'
                            .format(iteration, cost)
                        )
                    # Save the cost at the current step for the graph
                    if graph:
                        costs.append(cost)

        # Training finished, evaluate and print everything needed
        prediction, cost = self.evaluate(X, Y)
        if verbose:
            print('Cost after {} iterations: {}'.format(iterations, cost))
        if graph:
            costs.append(cost)

        # If needed print the information graph about the training cost
        if graph:
            plt.plot(range(0, iterations + 1, step), costs)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()
        return (prediction, cost)
