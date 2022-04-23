import matplotlib.pyplot as plt
import numpy as np

# 1. Create Data

angles = np.arange(0,360,1)
y = np.sin(np.deg2rad(angles))

# 2. Make Plot

plt.plot(angles,y)
plt.title('Sinusoidal Graph')
plt.text(360,0.1,'angle')
plt.text(190,1,'magnitudo')

plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks(
    [0,90,180,270,360],
    [r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$'])

ax = plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['right'].set_color('none')
# 3. Show Plot

plt.show()