import numpy as np
import matplotlib.pyplot as plt

# 1. Create Data
def sinusGenerator(amplitudo,frequency,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)

# 2. Make a plot
''' Type 1
data_plot1 = plt.plot(t1,y1, label='sin(0)')
data_plot3 = plt.plot(t2,y2, label='sin(0)')
plt.legend()
'''

''' Type 2
data_plot1 = plt.plot(t1,y1, label='sin(0)')
data_plot3 = plt.plot(t2,y2, label='sin(90)')
plt.legend(loc="upper center")
'''

''' Type 3
data_plot1 = plt.plot(t1,y1, label='sin(0)')
data_plot3 = plt.plot(t2,y2, label='sin(90)')
plt.legend(loc="upper center", bbox_to_anchor=(0.5,0.05))
'''

''' Type 4'''
plt.figure(1)
ax = plt.subplot(111)
data_plot1 = plt.plot(t1,y1, label='sin(0)')
data_plot3 = plt.plot(t2,y2, label='sin(90)')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.7, box.height])
plt.legend(loc="upper center", bbox_to_anchor=(1.2,1))


# 3. Show plot
plt.show()