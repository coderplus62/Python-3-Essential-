import numpy as np
import matplotlib.pyplot as plt

# Create linear equation
# y = 2x + 3

x = np.arange(0,11,1)
y = 2*x + 3

print(x)
print(y)

plt.figure(1)
plt.plot(x,y)
# plt.show()

# Create circle
radius = 7
angle = np.linspace(0,2*np.pi,1000)

x_c = radius*np.cos(angle)
y_c = radius*np.sin(angle)

plt.figure(2)
plt.plot(x_c,y_c)
plt.show()