# Function with return value
def cube_volume(length):
    volume = length**3
    print(f'The volume of cube that has length of {length} is: {volume}')
    return volume

v = cube_volume(3)
print(v)

# Function with return value and multiple argument
def cylinder_volume(radius,height):
    vol = radius**2 * height * 3.14
    print(f'The volume of cylinder that has radius of {radius} and height {height} is: {vol}')
    return vol
c = cylinder_volume(14,3)
print(c)

print('\n'+100*'#'+'\n')

# Using value from previous function
def addition_cube_cylinder(x,y):
    total = x + y
    print(f'Sum of volume cube and cylinder is: {x} + {y} =', total)
    return total
addition_cube_cylinder(v,c)
