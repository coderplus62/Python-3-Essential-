import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

a_mat = np.zeros((2,3))
b_mat = np.ones((2,3))
# stacking matrix (menumpuk)
h = np.hstack((a,b))
v = np.vstack((a,b))
print(h)
print(v)

h_mat = np.hstack((a_mat,b_mat))
v_mat = np.vstack((a_mat,b_mat))
print(h_mat)
print(v_mat)