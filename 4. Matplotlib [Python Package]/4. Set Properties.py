import numpy as np
import matplotlib.pyplot as plt

# 1. Create Data
def sinusGenerator(amplitudo,frequency,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)
t3,y3 = sinusGenerator(1,1,4,180)

# 2. Make a plot
data_plot1 = plt.plot(t1,y1)
data_plot2 = plt.plot(t2,y2)
data_plot3 = plt.plot(t3,y3)

# setting properties
plt.setp(data_plot1,color='c', linestyle='-' ,linewidth=1)
plt.setp(data_plot2,color='g', linestyle='-.',linewidth=4)
plt.setp(data_plot3,color='b', linestyle=':' ,linewidth=2)

# 3. Show plot
plt.show()
