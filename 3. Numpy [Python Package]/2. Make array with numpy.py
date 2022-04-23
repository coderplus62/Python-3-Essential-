import numpy as np

# make basic vector
x = np.array([1,2,3,4])
y = np.array([3.4,6,2.4,4])

# make vector using range
v = np.arange(10,20,2)
print('Create array using range:\n',v,'\n')

# make vector using line space
l = np.linspace(10,20,4)
print('Crate array using linespace:\n',l,'\n')

# make multi dimension array / matrix
m = np.array([(1,2,3),(4,5,6)])
print('Create matrix :',m,'\n')

# make zeros matrix
z = np.zeros((3,4))
print('Create zeros matrix:\n',z,'\n')

# make ones matrix
o = np.ones((4,3))
print('Create ones matrix:\n',o,'\n')

# make identity matrix
i = np.identity(3)
print('Create identity matrix [identity]:\n',i,'\n')
e = np.eye(3)
print('Create identity matrix [eye]:\n',e,'\n')
