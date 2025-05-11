#!/usr/bin/env python3
"""Deep Neural Network"""


import numpy as np


class DeepNeuralNetwork:
    """Deep Neural Network"""
    def __init__(self, nx, layers):
        """
        nx: no of input features
        layers: list repr no of nodes
        L: no of layers in NN
        cache: Dict with intermediary values
        weights: Dict to hold weights n biases
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if (
            type(layers) is not list
            or len(layers) < 1
            or min(layers) < 1
        ):
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for layer in range(self.__L):
            if layer == 0:
                self.__weights['W1'] = np.random.randn(
                    layers[0], nx) * np.sqrt(2 / nx)
                self.__weights['b1'] = np.zeros([layers[0], 1])

            else:
                self.__weights['W{}'.format(layer+1)] = np.random.randn(
                    layers[layer],
                    layers[layer-1]) * np.sqrt(2. / layers[layer-1])

                self.__weights['b{}'.format(
                    layer+1)] = np.zeros((layers[layer], 1))

    @property
    def L(self):
        """Getter for L"""
        return self.__L

    @property
    def cache(self):
        """Getter for cache"""
        return self.__cache

    @property
    def weights(self):
        """Getter for weights"""
        return self.__weights
