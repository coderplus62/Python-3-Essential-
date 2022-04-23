import numpy as np

# list
x = [1,2,3,4]
y = [4,5,6,7]

# array numpy
x_np = np.array([1,2,3,4])
y_np = np.array([4,5,6,7])

# addition
list_add = x + y
array_add = x_np + y_np

# subtraction
list_sub = x - y
array_sub = x_np - y_np

# multiplication
#list_mul = x * y -> error
array_mul = x_np * y_np

# division
#list_div = x / y -> error
array_div = x_np / y_np

# power
#list_pow = x ** y -> error
array_pow = x_np ** y_np

# multi dimension array / m
m1 = np.array(([1,2,3],[3,4,5]))
m2 = np.array(([4,5,6],[6,7,8]))

''' The operation is the same with above example'''
