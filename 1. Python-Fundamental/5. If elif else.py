x = 8
y = 9

# checking equality
'''
if x == 8:
    print('value of x is: ', x)

if x is 8:
    print('value of x is: ', x)
'''

# checking non-equality
'''
# 'y is not x' and 'y=!' for unequal
# (y>x) for greater than 
# (y>=x) for greater than or equal
# (y<x) for lower than 
# (y<=x) for lower than or equal 

if y>5:
    print('value of y is greater than 5')
'''

# if inside if (nesting if)
'''
if x == 8:
    print('value of x is: ', x)
    print('run step 1')
    if y > 5:
        print('value of y is greater than 5')
        print('run step 2')
'''

# elif
'''
grade = int(input("Entered your latest grade: "))

print(grade)

if 90 <= grade <= 100:
    print('your grade is A')
elif 80 <= grade < 90:
    print('your grade is B')
elif 70 <= grade < 80:
    print('your grade is C')
else:
    print('error')
'''

# Logic Operation for list and string

zoo = ['cat','dog','monkey','giraffe','buffalo','lion']
my_pet = input('What pet do you have?')

if my_pet in zoo:
    print('Your pet is exist on the zoo')
else:
    print(my_pet+' is not in the zoo')

char = input("What character that you want to find?")
print('\n'+20*'#')
print('Finding character "'+char+'" in the pet\'s name')
print(20*'#'+'\n')

if char in my_pet:
    print('There is "'+char+'" in the pet\'s name')
else:
    print('There is no "'+char+'" in the pet\'s name')
