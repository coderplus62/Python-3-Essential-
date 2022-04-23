import numpy as np

a = np.arange(10)**2
print(a)

# take value from array 'a'
print('The 1st element of a is:',a[0])
print('The 2nd element of a is:',a[1])
print('The last element of a is:',a[-1])

# slicing (take part od array)
print('\nElement 1 - 6 of a is:',a[0:6])
print('\nElement 2 - last of a is:',a[1::])
print('\nElement 1 - 7 of a is:',a[:7])

# iterating

for i in a:
    print(i)