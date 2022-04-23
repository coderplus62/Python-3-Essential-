i = 0

import numpy as np
import matplotlib.pyplot as plt

'''
x = [1,2,3,4,5]
y = [1,2,3,4,5]

# Initialize plot
plt.plot(x,y)

# Show the plot
plt.show()
'''

# Make a circle
PI = np.pi
angle = np.linspace(0,2*PI,100)
radius = 5

x = radius*np.cos(angle)
y = radius*np.sin(angle)

plt.plot(x,y)
plt.show()