import numpy as np

def circle_area(radius):
    area = np.pi*radius**2
    print('The surface area for circle is:',area)
    return area

def speed(d,t):
    s = d/t
    print('The average speed is:',s)
    return s

def acceleration(v,u,t):
    a = (v-u)/t
    print('The acceleration is:',a)
    return a

def force(m,a):
    f = m*a
    print('The force is:',f)
    return f

def pressure(f,a):
    p = f/a
    print('The pressure is:',p)
    return p
