import numpy as np

a = np.array([1,3]) 
b = np.array([2,1])

print(a)
print(b)
print('Dot product  :',np.dot(a,b))
print('Cross product:',np.cross(a,b))
print('Reverse      :',np.cross(b,a),'\n')

a_ = np.array([1,2,0])
b_ = np.array([2,1,0])
print(a_)
print(b_)
print('Dot product  :',np.dot(a_,b_))
print('Cross product:',np.cross(a_,b_))
print('Reverse      :',np.cross(b_,a_))