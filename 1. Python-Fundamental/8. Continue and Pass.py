init = 0
num = 20
step = 1
x = 21

for i in range(init,num,step):
    if i == 6:
        print('6 is founded')
        '''
        continue    # iterate to for loop to the next step (skip the command below)
        print('skipped command')
        '''
    print('Current value is: ',i)
else:
    print('End of loop')
print('Out of loop')

for i in range(init,num,step):
    pass    # pass is used for dummy loop and if statement