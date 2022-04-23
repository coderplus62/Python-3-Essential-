import numpy as np

'''make matrix with data type'''
m = np.array(([2,3,4],[5,6,7]), dtype= int)

'''
m_int = np.array(([2,3,4],[5,6,7]), dtype= int)
print('Matrix int: \n',m_int,'\n')
m_flt = np.array(([2,3,4],[5,6,7]), dtype= float)
print('Matrix float: \n',m_flt,'\n')
m_bol = np.array(([2,3,4],[5,6,7]), dtype= bool)
print('Matrix bool: \n',m_bol,'\n')
'''

''' crate matrix with function '''
# x = np.fromfunction(function=,shape=,type=)

def quadratic(row,col):
    return col**2

def sum(row,col):
    return col+row

x = np.fromfunction(quadratic,(3,10),dtype=int)
y = np.fromfunction(sum,(4,4),dtype=float)
print(y)

''' create matrix/array using iteration/iterable '''
iterator = (x*x for x in range(5))

i = np.fromiter(iterator,dtype=int)
print(i)

''' multi type array '''
data = [('sastra',165),
        ('stepen',175),
        ('adrian',170)
        ]
dtype = [('nama','S255'),('tinggi',int)]

a = np.array(data,dtype=dtype)

print(a)
print(a[0])