import Calculator
import numpy as numpy

c = Calculator
# print(c.OddOrEven(4))
np = numpy
array = np.array([2, 3])
print(array)

import matplotlib.pyplot as plt
x1 = np.linspace(start=-10, stop=10, num=51)
x2 = np.linspace(start=-10, stop=10, num=101)
print(x1)
plt.figure('a') # plot name
plt.plot(x1, np.absolute(x1)) # plot value for x and y axis
plt.figure('b')
plt.plot(x2, np.absolute(x2))
plt.show()
