#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# your code here
x = np.arange(0, 11, 2)
plt.plot(y, color='red')
plt.xlim(0, 10)
plt.show()
