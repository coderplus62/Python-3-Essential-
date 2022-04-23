import numpy as np
import matplotlib.pyplot as plt

# 1. Create Data
def sinusGenerator(amplitudo,frequency,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)

plt.plot(t1,y1)
plt.text(2,0.5,r'$ y = \mathcal{A}.sin(2 \omega t)$')
plt.text(2,0.4,r'$\mathcal{A} = 1 cm, \omega = 1 Hz)$')

plt.show()