init = 0
iteration = 10
x = 21
'''
# while using statement
while num < iteration:
    print('Value of number is:', num)
    num = num + 1
else:
    print('last number of the loop is:', num)
print('Out of while loop')
'''
############
'''
start = True # Boolean variable
num = 20

# while using boolean
while start:
    print('num =', num)
    if num == 100:
        start = False
        print('100 is founded')
    num += 1
'''

num = 0
iteration = 12
'''
# break while
while num < iteration:
    if num == 5:
        print('check point')
        break
    print('Value of number is:', num)
    num = num + 1
else:
    print('last number of the loop is:', num)
print('Out of while loop')
'''

# continue while
while num < iteration:
    if num == 5:
        print('check point at number is:', num)
        num = num + 1
        '''take a note here, if it does not exist, there is infinite loop'''
        continue
    print('Value of number is:', num)
    num = num + 1
else:
    print('last number of the loop is:', num)
print('Out of while loop')