import numpy as np

x = np.array((
            [1,2,3],
            [4,5,6]
            ))
# take shape
print('Matrix shape: \n',x.shape)

# transpose matrix
print('Transpose matrix method 1: \n',x.transpose())
print('Transpose matrix method 2: \n',np.transpose(x))
print('Transpose matrix method 3: \n',x.T)
print('Matrix shape: \n',x.shape,'\n')

# flatten array, change matrix to line vector (single row)
print('Flatten matrix method 1: \n',x.ravel())
print('Flatten matrix method 2: \n',np.ravel(x))
print('Matrix shape: \n',x.shape,'\n')

# reshape
print('Reshaping the matrix:')
print(x.reshape(3,2))
print('Matrix shape: \n',x.shape,'\n')

# resize matrix
print('Resizing the matrix:')
x.resize(3,2)
print(x)
print('Matrix shape: \n',x.shape,'\n')
