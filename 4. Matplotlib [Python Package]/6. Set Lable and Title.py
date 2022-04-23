import numpy as np
import matplotlib.pyplot as plt

# 1. Create Data
def sinusGenerator(amplitudo,frequency,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frequency = 1
theta = 0
tAkhir = 4

t,y = sinusGenerator(amplitudo,frequency,tAkhir,theta)

# 2. Make a plot
title = 'Sinusoidal Graphic\n'
function = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta)$' + '\n'
parameter1 = r'$ A = $' + str(amplitudo) + ' cm, '
parameter2 = r'$ \omega = $' + str(frequency) + r'$\mathit{Hz}$' + ', '
parameter3 = r'$ \theta = $' + str(theta) + r'$^{o} $'

data_plot1 = plt.plot(t,y)

plt.title(title+function+parameter1+parameter2+parameter3)
plt.xlabel('Time (s)')
plt.ylabel('magnitude (cm)')

# 3. Show plot
plt.show()