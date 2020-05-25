# 0x00. Binary Classification

--------------------------------------------------------------------------------

## Learning Objectives

I learned from this project:

- What is a model?
- What is supervised learning?
- What is a prediction?
- What is a node?
- What is a weight?
- What is a bias?
- What are activation functions?
  - Sigmoid?
  - Tanh?
  - Relu?
  - Softmax?
- What is a layer?
- What is a hidden layer?
- What is Logistic Regression?
- What is a loss function?
- What is a cost function?
- What is forward propagation?
- What is Gradient Descent?
- What is back propagation?
- What is a Computation Graph?
- How to initialize weights/biases
- The importance of vectorization
- How to split up your data

--------------------------------------------------------------------------------

### [0\. Neuron](./0-neuron.py)

Class Neuron that defines a single neuron performing binary classification with this constructor:

```python
def __init__(self, nx)
```

Where:

- nx is the number of input features to the neuron
- If nx is not an integer, raise a TypeError with the exception: nx must be an integer
- If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer

Public instance attributes:

- W: The weights vector for the neuron. Upon instantiation, it should be initialized using a * random normal distribution.
- b: The bias for the neuron. Upon instantiation, it should be initialized to 0.
- A: The activated output of the neuron (prediction). Upon instantiation, it should be * initialized to 0.

### [1\. Privatize Neuron](./1-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 0-neuron.py):

Class constructor:

```python
def __init__(self, nx)
```

Private instance attributes:

- __W: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
- __b: The bias for the neuron. Upon instantiation, it should be initialized to 0.
- __A: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.
- Each private attribute should have a corresponding getter function (no setter function).

### [2\. Neuron Forward Propagation](./2-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 1-neuron.py):

Add the public method `forward_prop(self, X)` that:

1. Calculates the forward propagation of the neuron
2. Updates the private attribute __A
3. The neuron should use a sigmoid activation function
4. Returns the private attribute __A

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples

### [3\. Neuron Cost](./3-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 2-neuron.py):

Add the public method `cost(self, Y, A)` that calculates the cost of the model using logistic regression.

- To avoid division by zero errors, **1.0000001 - A** will be used instead of **1 - A**.

Where:

- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- A is a `numpy.ndarray with shape (1, m)` containing the activated output of the neuron for each example

### [4\. Evaluate Neuron](./4-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 3-neuron.py):

Add the public method `evaluate(self, X, Y)` that:

- Evaluates the neuron's predictions
- The prediction should be a `numpy.ndarray with shape (1, m)` containing the predicted labels for each example
- The label values should be 1 if the output of the network is >= 0.5 and 0 otherwise

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data Returns the neuron's prediction and the cost of the network, respectively

### [5\. Neuron Gradient Descent](./5-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 4-neuron.py):

Add the public method `gradient_descent(self, X, Y, A, alpha=0.05)` that:

- Calculates one pass of gradient descent on the neuron
- Updates the private attributes \__W and \__b

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- A is a `numpy.ndarray with shape (1, m)` containing the activated output of the neuron for each example
- alpha is the learning rate

### [6\. Train Neuron](./6-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 5-neuron.py):

Add the public method `train(self, X, Y, iterations=5000, alpha=0.05)` that:

- Use only one loop
- Trains the neuron
- Updates the private attributes \_\_W, \_\_b, and \_\_A
- Returns the evaluation of the training data after iterations of training have occurred

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- nx is the number of input features to the neuron
- m is the number of examples
- iterations is the number of iterations to train over
- alpha is the learning rate

Taking in account:

- if iterations is not an integer, raise a TypeError with the exception iterations must be an integer
- if iterations is not positive, raise a ValueError with the exception iterations must be a positive integer
- if alpha is not a float, raise a TypeError with the exception alpha must be a float
- if alpha is not positive, raise a ValueError with the exception alpha must be positive

### [7\. Upgrade Train Neuron](./7-neuron.py)

Class Neuron that defines a single neuron performing binary classification (Based on 6-neuron.py):

Update the public method train to `train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100)`:

- Now it trains the neuron by updating the private attributes \_\_W, \_\_b, and __A,
also it returns the evaluation of the training data after iterations of training have occurred

Taking in account that:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- iterations is the number of iterations to train over
  - if iterations is not an integer, raise a TypeError with the exception iterations must be an integer
  - if iterations is not positive, raise a ValueError with the exception iterations must be a positive integer
- alpha is the learning rate
  - if alpha is not a float, raise a TypeError with the exception alpha must be a float
  - if alpha is not positive, raise a ValueError with the exception alpha must be positive
- verbose is a boolean that defines whether or not to print information about the training. If True:
  - print Cost after {iteration} iterations: {cost} every step iterations:
  - Include data from the 0th and last iteration
- graph is a boolean that defines whether or not to graph information about the training once the training has completed. If True:
  - Plot the training data every step iterations as a blue line
  - Label the x-axis as iteration
  - Label the y-axis as cost
  - Title the plot Training Cost
  - Include data from the 0th and last iteration
- Only if either verbose or graph are True:
  - if step is not an integer, raise a TypeError with the exception step must be an integer
  - if step is not positive or is greater than iterations, raise a ValueError with the exception step must be positive and <= iterations
- The 0th iteration represent the state of the neuron before any training has occurred

### [8\. NeuralNetwork](./8-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification:

Class constructor:

```python
def __init__(self, nx, nodes):
```

Where:

- nx is the number of input features
  - If nx is not an integer, raise a TypeError with the exception: nx must be an integer
  - If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer
- nodes is the number of nodes found in the hidden layer
  - If nodes is not an integer, raise a TypeError with the exception: nodes must be an integer
  - If nodes is less than 1, raise a ValueError with the exception: nodes must be a positive integer

Public instance attributes:

- W1: The weights vector for the hidden layer. Upon instantiation, it should be initialized using a random normal distribution.
- b1: The bias for the hidden layer. Upon instantiation, it should be initialized with 0’s.
- A1: The activated output for the hidden layer. Upon instantiation, it should be initialized to 0.
- W2: The weights vector for the output neuron. Upon instantiation, it should be initialized using a random normal distribution.
- b2: The bias for the output neuron. Upon instantiation, it should be initialized to 0.
- A2: The activated output for the output neuron (prediction). Upon instantiation, it should be initialized to 0.

### [9\. Privatize NeuralNetwork](./9-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 8-neural_network.py):

Class constructor:

```python
def __init__(self, nx, nodes):
```

Where:

- nx is the number of input features
  - If nx is not an integer, raise a TypeError with the exception: nx must be an integer
  - If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer
- nodes is the number of nodes found in the hidden layer
  - If nodes is not an integer, raise a TypeError with the exception: nodes must be an integer
  - If nodes is less than 1, raise a ValueError with the exception: nodes must be a positive integer

Private instance attributes:

- W1: The weights vector for the hidden layer. Upon instantiation, it should be initialized using a random normal distribution.
- b1: The bias for the hidden layer. Upon instantiation, it should be initialized with 0’s.
- A1: The activated output for the hidden layer. Upon instantiation, it should be initialized to 0.
- W2: The weights vector for the output neuron. Upon instantiation, it should be initialized using a random normal distribution.
- b2: The bias for the output neuron. Upon instantiation, it should be initialized to 0.
- A2: The activated output for the output neuron (prediction). Upon instantiation, it should be initialized to 0.
- Each private attribute have a corresponding getter function (no setter function).

### [10\. NeuralNetwork Forward Propagation](./10-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 9-neural_network.py):

Add the public method `forward_prop(self, X)` that:

- Calculates the forward propagation of the neural network
- Updates the private attributes \_\_A1 and \_\_A2
- Returns the private attributes \_\_A1 and \_\_A2, respectively

Where:

- X is a numpy.ndarray with shape (nx, m) that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- The neurons should use a sigmoid activation function

### [11\. NeuralNetwork Cost](./11-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 10-neural_network.py):

Add the public method `cost(self, Y, A)` that:

- Calculates the cost of the model using logistic regression
- Returns the cost

Where:

- Y is a numpy.ndarray with shape (1, m) that contains the correct labels for the input data
- A is a numpy.ndarray with shape (1, m) containing the activated output of the neuron for each example
- To avoid division by zero errors, `1.0000001 - A` will be used instead of `1 - A`

### [12\. Evaluate NeuralNetwork](./12-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 11-neural_network.py):

Add the public method `evaluate(self, X, Y)` that:

- Evaluates the neural network’s predictions
- Returns the neuron’s prediction and the cost of the network, respectively

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- The prediction is a `numpy.ndarray with shape (1, m)` containing the predicted labels for each example
- The label values is 1 if the output of the network is >= 0.5 and 0 otherwise

### [13\. NeuralNetwork Gradient Descent](./13-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 12-neural_network.py):

Add the public method `gradient_descent(self, X, Y, A1, A2, alpha=0.05)` that:

- Calculates one pass of gradient descent on the neural network
- Updates the private attributes \_\_W1, \_\_b1, \_\_W2, and \_\_b2

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- A1 is the output of the hidden layer
- A2 is the predicted output
- alpha is the learning rate

### [14\. Train NeuralNetwork](./14-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 13-neural_network.py):

Add the public method `train(self, X, Y, iterations=5000, alpha=0.05)` that:

- Trains the neural network
- Updates the private attributes \_\_W1, \_\_b1, \_\_A1, \_\_W2, \_\_b2, and \_\_A2
- Use only one loop
- Returns the evaluation of the training data after iterations of training have occurred

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- iterations is the number of iterations to train over
  - if iterations is not an integer, raise a TypeError with the exception iterations must be an integer
  - if iterations is not positive, raise a ValueError with the exception iterations must be a positive integer
- alpha is the learning rate
  - if alpha is not a float, raise a TypeError with the exception alpha must be a float
  - if alpha is not positive, raise a ValueError with the exception alpha must be positive

### [15\. Upgrade Train NeuralNetwork](./15-neural_network.py)

Class NeuralNetwork that defines a neural network with one hidden layer performing binary classification (based on 14-neural_network.py):

Update the public method train to `train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100)` that:

- Trains the neural network
- Updates the private attributes \_\_W1, \_\_b1, \_\_A1, \_\_W2, \_\_b2, and \_\_A2
- Returns the evaluation of the training data after iterations of training have occurred

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- iterations is the number of iterations to train over
  - if iterations is not an integer, raise a TypeError with the exception iterations must be an integer
  - if iterations is not positive, raise a ValueError with the exception iterations must be a positive integer
- alpha is the learning rate
  - if alpha is not a float, raise a TypeError with the exception alpha must be a float
  - if alpha is not positive, raise a ValueError with the exception alpha must be positive
- verbose is a boolean that defines whether or not to print information about the training. If True, print Cost after {iteration} iterations: {cost} every step iterations:
  - Include data from the 0th and last iteration
- graph is a boolean that defines whether or not to graph information about the training once the training has completed. If True:
  - Plot the training data every step iterations as a blue line
  - Label the x-axis as iteration
  - Label the y-axis as cost
  - Title the plot Training Cost
  - Include data from the 0th and last iteration
- Only if either verbose or graph are True:
  - if step is not an integer, raise a TypeError with the exception step must be an integer
  - if step is not positive and less than or equal to iterations, raise a ValueError with the exception step must be positive and <= iterations
- The 0th iteration should represent the state of the neuron before any training has occurred
- Use only one loop

### [16\. DeepNeuralNetwork](./16-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification:

Class constructor:

```python
def __init__(self, nx, layers):
```

Where:

- nx is the number of input features
  - If nx is not an integer, raise a TypeError with the exception: nx must be an integer
  - If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer
- layers is a list representing the number of nodes in each layer of the network
  - If layers is not a list, raise a TypeError with the exception: layers must be a list of positive integers
  - The first value in layers represents the number of nodes in the first layer, …
  - If the elements in layers are not all positive integers, raise a TypeError with the exception layers must be a list of positive integers
- Use only one loop

Public instance attributes:

- L: The number of layers in the neural network.
- cache: A dictionary to hold all intermediary values of the network. Upon instantiation, it should be set to an empty dictionary.
- weights: A dictionary to hold all weights and biases of the network. Upon instantiation:
  - The weights of the network should be initialized using the He et al. method and saved in the weights dictionary using the key W{l} where {l} is the hidden layer the weight belongs to
  - The biases of the network should be initialized to 0’s and saved in the weights dictionary using the key b{l} where {l} is the hidden layer the bias belongs to

### [17\. Privatize DeepNeuralNetwork](./17-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 16-deep_neural_network.py):

Class constructor:

```Python
def __init__(self, nx, layers):
```

Where:

- nx is the number of input features
  - If nx is not an integer, raise a TypeError with the exception: nx must be an integer
  - If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer
- layers is a list representing the number of nodes in each layer of the network
  - If layers is not a list, raise a TypeError with the exception: layers must be a list of positive integers
  - The first value in layers represents the number of nodes in the first layer, …
  - If the elements in layers are not all positive integers, raise a TypeError with the exception layers must be a list of positive integers
- Each private attribute have a corresponding getter function (no setter function).
- Use only one loop

Private instance attributes:

- \_\_L: The number of layers in the neural network.
- \_\_cache: A dictionary to hold all intermediary values of the network. Upon instantiation, it should be set to an empty dictionary.
- \_\_weights: A dictionary to hold all weights and biased of the network. Upon instantiation:
  - The weights of the network should be initialized using the He et al. method and saved in the \_\_weights dictionary using the key W{l} where {l} is the hidden layer the weight belongs to
  - The biases of the network should be initialized to 0‘s and saved in the \_\_weights dictionary using the key b{l} where {l} is the hidden layer the bias belongs to

### [18\. DeepNeuralNetwork Forward Propagation](./18-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 17-deep_neural_network.py):

Add the public method `forward_prop(self, X)` that:

- Calculates the forward propagation of the neural network
- All neurons use a sigmoid activation function
- Use only one loop
- Returns the output of the neural network and the cache, respectively
- Updates the private attribute \_\_cache:
  - The activated outputs of each layer should be saved in the \_\_cache dictionary using the key A{l} where {l} is the hidden layer the activated output belongs to
  - X should be saved to the cache dictionary using the key A0

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
- nx is the number of input features to the neuron
- m is the number of examples

### [19\. DeepNeuralNetwork Cost](./19-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 18-deep_neural_network.py):

Add the public method `cost(self, Y, A)` that calculates the cost of the model using logistic regression.

Where:

- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- A is a `numpy.ndarray with shape (1, m)` containing the activated output of the neuron for each example
- To avoid division by zero errors, `1.0000001 - A` will be used instead of `1 - A`

### [20\. Evaluate DeepNeuralNetwork](./20-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 19-deep_neural_network.py):

Add the public method `evaluate(self, X, Y)` that:

- Evaluates the neural network’s predictions
- Returns the neuron’s prediction and the cost of the network, respectively
  - The prediction should be a `numpy.ndarray with shape (1, m)` containing the predicted labels for each example
  - The label values should be 1 if the output of the network is >= 0.5 and 0 otherwise

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
  - nx is the number of input features to the neuron
  - m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data

### [21\. DeepNeuralNetwork Gradient Descent](./21-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 20-deep_neural_network.py):

Add the public method `gradient_descent(self, Y, cache, alpha=0.05)` that:

- Calculates one pass of gradient descent on the neural network
- Updates the private attribute \_\_weights
- Use only one loop

Where:

- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- cache is a dictionary containing all the intermediary values of the network
- alpha is the learning rate

### [22\. Train DeepNeuralNetwork](./22-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 21-deep_neural_network.py):

Add the public method `train(self, X, Y, iterations=5000, alpha=0.05)` that:

- Trains the deep neural network
- Updates the private attributes \_\_weights and \_\_cache
- Returns the evaluation of the training data after iterations of training have occurred
- Use only one loop

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
  - nx is the number of input features to the neuron
  - m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- iterations is the number of iterations to train over
  - if iterations is not an integer, raise a TypeError with the exception iterations must be an integer
  - if iterations is not positive, raise a ValueError with the exception iterations must be a positive integer
- alpha is the learning rate
  - if alpha is not a float, raise a TypeError with the exception alpha must be a float
  - if alpha is not positive, raise a ValueError with the exception alpha must be positive

### [23\. Upgrade Train DeepNeuralNetwork](./23-deep_neural_network.py)

Class DeepNeuralNetwork that defines a deep neural network performing binary classification (based on 22-deep_neural_network.py):

Update the public method train to train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100) that:

- Trains the deep neural network by updating the private attributes \_\_weights and \_\_cache
- Use only one loop
- Returns the evaluation of the training data after iterations of training have occurred

Where:

- X is a `numpy.ndarray with shape (nx, m)` that contains the input data
  - nx is the number of input features to the neuron
  - m is the number of examples
- Y is a `numpy.ndarray with shape (1, m)` that contains the correct labels for the input data
- iterations is the number of iterations to train over
  - if iterations is not an integer, raise a TypeError with the exception iterations must be an integer
  - if iterations is not positive, raise a ValueError with the exception iterations must be a positive integer
- alpha is the learning rate
  - if alpha is not a float, raise a TypeError with the exception alpha must be a float
  - if alpha is not positive, raise a ValueError with the exception alpha must be positive
- verbose is a boolean that defines whether or not to print information about the training. If True, print Cost after {iteration} iterations: {cost} every step iterations:
  - Include data from the 0th and last iteration
- graph is a boolean that defines whether or not to graph information about the training once the training has completed. If True:
  - Plot the training data every step iterations as a blue line
  - Label the x-axis as iteration
  - Label the y-axis as cost
  - Title the plot Training Cost
  - Include data from the 0th and last iteration
- Only if either verbose or graph are True:
  - if step is not an integer, raise a TypeError with the exception step must be an integer
  - if step is not positive and less than or equal to iterations, raise a ValueError with the exception step must be positive and <= iterations
- The 0th iteration represent the state of the neuron before any training has occurred

--------------------------------------------------------------------------------

## Author

- **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)
