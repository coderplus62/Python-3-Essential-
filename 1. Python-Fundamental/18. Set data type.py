init = 0

'''
set in indonesia is HUMAN, so the characteristic is the same
- no indexing
- no same data
- can any data type (int, float, string)
'''

avenger = {'hulk','ironman','spiderman','falcon','wanda'}
#print(avenger)

# add new data
avenger.add('vision')
avenger.add('hulk')    # only 1 'hulk' data
print(avenger)

''' Using other method'''
print('\n '+10*'#'+' Using set() '+10*'#'+'\n')

avenger = set()

avenger.add('ironman')
avenger.add('hulk')
avenger.add('vision')

#print(sorted(avenger))

avenger.add(79)
print(avenger)

''' Using set for union, intersect the data'''
print('\n '+10*'#'+' Using set for union, intersect the data '+10*'#'+'\n')

odd = {1,3,5,7,9}
even = {2,4,6,8,10}
prime = {2,3,5,7,11}

print('odd data:',odd,'\neven data:',even,'\nprime data:',prime,'\n')
print('Union odd and even:',odd.union(even))
print('Union odd and prime:',odd.union(prime))
print('Intersection odd and even:',odd.intersection(even))
print('Intersection odd and prime:',odd.intersection(prime))