import numpy as np
import matplotlib.pyplot as plt

# 1. Create Data
def sinusGenerator(amplitudo,frequency,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y
t1,y1 = sinusGenerator(1,1,4,0)

# 2. Make a plot
data_plot1 = plt.plot(t1,y1)

# setting axis, minimum and maximum
plt.axis([0,4,-2,2])

# 3. Show plot
plt.show()