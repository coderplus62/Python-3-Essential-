number = 50
'''
# Print value in a range
for i in range(0,21,2):
    # range(a,b,c) -> a = start, b-1 = end, c = step
    # print(range(0,21,2)) -> cannot be a list
    print(i)
'''
num = 20
step = 2
x = 21
# searching the value of x in range
for i in range(0,num,step):
    print(i)
    if i == x:
        print(f'{x} is founded.')
        break # break is used to quit the looping
else:
    print(f'{x} is not founded.')
print('Out of for loop')
