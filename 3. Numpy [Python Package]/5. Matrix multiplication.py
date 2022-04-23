import numpy as np

m1 = np.array(([2,2],[4,3]))
m2 = np.array(([3,3],[1,3]))
o = np.ones([2,1])

# element multiplication
m_mul = m1*m2

# matrix multiplication
m_dot = m1.dot(m2)
''' matrix size should be same '''
m_dot2 = np.dot(m1,m2)
m_dot3 = m1.dot(o)
print('element multiplication:\n',m_mul)
print(m_dot)
print(m_dot2)
print(m_dot3)