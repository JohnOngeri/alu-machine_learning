#!/usr/bin/env python3
"""Deep Neural Network training"""


import numpy as np


class DeepNeuralNetwork:
    '''
    Initialize Deep Neural Network class
    '''
    def __init__(self, nx, layers):
        '''
        Deep Neural Network class constructor
        '''
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list:
            raise TypeError("layers must be a list of positive integers")
        if len(layers) < 1:
            raise TypeError("layers must be a list of positive integers")
        if min(layers) < 1:
            raise TypeError("layers must be a list of positive integers")
        
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(self.__L):
            if i == 0:
                self.__weights['W1'] = np.random.randn(layers[i], nx) * np.sqrt(2 / nx)
                self.__weights['b1'] = np.zeros((layers[i], 1))

            else:
                self.__weights['W{}'.format(i + 1)] = np.random.randn(layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])

                self.__weights['b{}'.format(i + 1)] = np.zeros((layers[i], 1))

    @property
    def L(self):
        '''
        getter function
        '''
        return self.__L
    
    @property
    def cache(self):
        '''
        getter function
        '''
        return self.__cache
    
    @property
    def weights(self):
        '''
        getter function
        '''
        return self.__weights
    
    def forward_prop(self, X):
        '''
        Forward propagation function
        '''
        self.__cache['A0'] = X

        for 1 in range(1, self.__L+1):
            W = self.__weights['W{}'.format(i)]
            b = self.__weights['b{}'.format(i)]
            A = self.__cache['A{}'.format(i-1)]
            Z = np.matmul(W, A) + b
            self.__cache['A{}'.format(i)] = 1 / (1 + np.exp(-Z))

        return self.__cache['A{}'.format(self.__L)], self.__cache    
            
    def cost(self, Y, A):
        """
        Cost of the model using logistic regression
        """
        m = Y.shape[1]
        cost = -np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A))) / m
        return cost

    def evaluate(self. X, Y):
        """
        Evaluates the deep neural network's predictions
        """
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.round(A).astype(int)
        return prediction, cost
    
    def gradient_descent(self, Y, cache, alpha=0.05):
        """
        Calculates one pass of gradient descent on the deep neural network
        """
        m = Y.shape[1]
        dZ = cache['A{}'.format(self.__L)] - Y

        for i in range(self.__L, 0, -1):
            A = cache['A{}'.format(i - 1)]
            dW = np.matmul(dZ, A.T) / m
            db = np.sum(dZ, axis=1, keepdims=True) / m

            W = self.__weights['W{}'.format(i)]
            dZ = np.matmul(W.T, dZ) * (A * (1 - A))
            self.__weights['W{}'.format(i)] = self.__weights['W{}'.format(i)] - (alpha * dW)
            self.__weights['b{}'.format(i)] = self.__weights['b{}'.format(i)] - (alpha * db)

    return self.__weights

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Trains the deep neural network
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        
        cost[]

        for i in range(iterations):
        A, cache = self.forward_prop(X)
            self.gradient_descent(Y, cache, alpha)

            if i % step == 0 or i == iterations - 1:
                cost = self.cost(Y, A)
                costs.append(cost)
                if verbose:
                    print(f"Cost after {i} iterations: {cost}")

        if graph:
            plt.plot(range(0, iterations + 1, step), costs)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()

        return self.evaluate(X, Y)
    
