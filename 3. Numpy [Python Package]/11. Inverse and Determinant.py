import numpy as np

A = np.array([(1,-1),(1,1)])
print('Array data: \n',A,'\n')

# inverse matrix

A_inv = np.linalg.inv(A)
print('Inverse of A: \n', A_inv)
print(np.dot(A,A_inv),'\n')

# determinant
det_a = np.linalg.det(A)
print('Determinant of A         : ',det_a)
det_a_inv = np.linalg.det(A_inv)
print('Determinant of inverse A : ',det_a_inv)

''' It is used to solve the linear equation '''
