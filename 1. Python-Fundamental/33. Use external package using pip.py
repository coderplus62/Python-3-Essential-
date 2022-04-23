from PIL import Image

im = Image.open("Photo 1.jpg")

print("format file: " + im.format)
print("ukuran file: " + str(im.size))
print("mode file: " + im.mode)

im.show()


''' Differentiation between numpy and list '''

import numpy as np

a = [1,2,3,4]
b = [5,6,7,8]

print(a+b)

a_np = np.array(a)
b_np = np.array(b)

print(a_np+b_np)