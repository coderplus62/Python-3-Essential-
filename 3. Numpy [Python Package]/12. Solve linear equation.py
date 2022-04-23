import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array((23,14))

'''
Solving the linear equation:

X = A_inv * Y
'''

A_inv = np.linalg.inv(A)

X = np.dot(A_inv,Y)
print('Solution for X method 1: \n',X)

'''
Using other method
'''

X2 = np.linalg.solve(A,Y)
print('Solution for X method 2: \n',X2)
