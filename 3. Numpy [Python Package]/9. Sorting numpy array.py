import numpy as np

a_int = np.floor(np.random.rand(1,5)*10)
a = np.random.randint(1,50,10)

# get max and min for both value and location
print('Data matrix: \n',a_int,'\n')
print('Max value    :',a_int.max())
print('Max position :',a_int.argmax())
print('Min value    :',a_int.min())
print('Min position :',a_int.argmin())

# sorting matrix
print('Sorting the matrix: \n',np.sort(a_int))
print('Previous position before sorted: \n',np.argsort(a_int))

''' Multi-Dimension Array '''

print('\n\n',10*'*',' Multi-Dimension Arrays ',10*'*','\n\n')

row = 2
col = 2

b_int = np.floor(np.random.rand(row,col)*10)

# get max and min for both value and location
print('Data matrix: \n',b_int,'\n')
print('Max value    :',b_int.max())
print('Max position :',b_int.argmax())
print('Min value    :',b_int.min())
print('Min position :',b_int.argmin())

# sorting matrix
print('Sorting the matrix: \n',np.sort(b_int))
print('Previous position before sorted: \n',np.argsort(b_int))

''' Multi-Type Array '''

print('\n\n',10*'*',' Multi-Type Arrays ',10*'*','\n\n')

dtype = [('name','S15'),('height',int)]
data = [
        ('codet',166),
        ('lengur',159),
        ('sadem',150)
        ]

h = np.array(data,dtype=dtype)
print('Data             :',h)
print('Sorted by height :',np.sort(h,order='height'))
print('Sorted by name   :',np.sort(h,order='name'))