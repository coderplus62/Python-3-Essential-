print('Tuple Data Type\n')

# Tuple is cannot manipulated data

#List
num_list = [1,2,3,4]
#Tuple
num_tuple = (5,6,7,8,8,7,8 )

print(type(num_list))
print(type(num_tuple))

# num_list[3] = 21
# print(num_list)

'''
This will produce error
# cannot adding, append, remove, etc
num_tuple[3] = 22
print((num_tuple))
'''

'''How to know what we can do to the data'''
print(dir(num_list))
print(dir(num_tuple)) # just count and index can be used

print(num_tuple.count(8))
print(num_tuple.index(7))


'''
Tuple is usually used for fixing the data, for exmple ID
Also, Tuple is lighter than list
'''

''' Computing Data Size'''
print('\n '+10*'#'+' Computing Data Size '+10*'#'+'\n')

import sys

list_data = [1,2,3,4,5,'red','green','blue',False,3.14]
tuple_data = (1,2,3,4,5,'red','green','blue',False,3.14)

list_size = sys.getsizeof(list_data)
tuple_size = sys.getsizeof(tuple_data)

print(list_data)
print('Size of data list:', list_size)

print(tuple_data)
print('Size of data tuple:', tuple_size)

print('\n '+10*'#'+' Computing Data Size '+10*'#'+'\n')


''' Computing Time Needed'''
print('\n '+10*'#'+' Computing Time Needed '+10*'#'+'\n')

import timeit

list_time = timeit.timeit(stmt="[1,2,3,4,5,'red','green','blue',False,3.14]",number=100000)
print('Time needed to process list:',list_time)

tuple_time = timeit.timeit(stmt="(1,2,3,4,5,'red','green','blue',False,3.14)",number=100000)
print('Time needed to process tuple:',tuple_time)
