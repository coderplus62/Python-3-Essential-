i = 0

import numpy as np
import matplotlib.pyplot as plt

'''
Step to create plot:
    1. Create data
    2. Make a plot
    3. Show the plot    
'''

# 1. Create Data
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([1,16,81,256,625])

# 2. Make a plot
plt.plot(x,y)
plt.plot(x,y2)

# 3. Show the plot
plt.show()
