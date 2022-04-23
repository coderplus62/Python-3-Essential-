import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Data (sin(2wt + theta))
# Camel case
def sinusGenerator(amplitudo,frequency,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

# 2. Make a plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'r^')

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3, 'b--')

t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4, 'y-o')
# r = red;

# 3. Show plot
plt.show()


# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "*"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin_diamond
# "|"	vline
# "_"	hline