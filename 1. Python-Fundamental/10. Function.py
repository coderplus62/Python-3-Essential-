def basic_function():
    print('This is a basic function\n')
def addition_function():
    basic_function()
    a = int(input('type the value of a:'))
    b = int(input('type the value of b:'))
    print(f'addition of {a} and {b} is:',a+b)

# Function with input argument

def speed(distance,time):
    basic_function()
    print(f'Distance input = {distance}, and Time input = {time}')
    print('\n '+10*'*'+' Calculating '+10*'*'+'\n')
    print('Speed =',distance/time)

speed(25,2)